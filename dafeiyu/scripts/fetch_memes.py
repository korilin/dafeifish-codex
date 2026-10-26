#!/usr/bin/env python3
"""Fetch the pinned, personal-use upstream pack; never execute upstream code."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import tempfile
from urllib.request import urlopen


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--accept-personal-license', action='store_true',
                        help='Acknowledge the upstream pack is marked personal use')
    parser.add_argument('--dest', type=Path, help='Override the local image directory')
    args = parser.parse_args()
    if not args.accept_personal_license:
        parser.error('Read README.md and the upstream license notice, then pass --accept-personal-license')
    skill = Path(__file__).resolve().parent.parent
    manifest = json.loads((skill / 'references/meme-files.json').read_text())
    destination = (args.dest or skill / 'assets/memes').resolve()
    base = ('https://raw.githubusercontent.com/yyh-001/dsh-meme/'
            + manifest['commit'] + '/' + manifest['upstream_directory'] + '/')

    def download(entry):
        relative = PurePosixPath(entry['path'])
        if relative.is_absolute() or '..' in relative.parts or relative.suffix != '.jpg':
            raise ValueError('Invalid image path: ' + str(relative))
        target = (destination / str(relative)).resolve()
        if not target.is_relative_to(destination):
            raise ValueError('Image path escapes destination')
        expected = entry['sha256']
        if target.is_file() and hashlib.sha256(target.read_bytes()).hexdigest() == expected:
            return 'cached'
        if target.exists():
            raise ValueError('Existing image differs; refusing to overwrite: ' + str(target))
        with urlopen(base + str(relative), timeout=30) as response:
            data = response.read(5 * 1024 * 1024 + 1)
        if len(data) > 5 * 1024 * 1024 or hashlib.sha256(data).hexdigest() != expected:
            raise ValueError('Image size/hash mismatch: ' + str(relative))
        if not data.startswith(b'\xff\xd8\xff'):
            raise ValueError('Expected JPEG: ' + str(relative))
        target.parent.mkdir(parents=True, exist_ok=True)
        # Link a fully written temporary file without overwriting a concurrent write.
        with tempfile.NamedTemporaryFile(dir=target.parent, delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(data)
        try:
            os.link(temporary, target)
        finally:
            temporary.unlink()
        return 'downloaded'

    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(download, manifest['files']))
    print(f"Verified {len(results)} images: {results.count('downloaded')} downloaded, "
          f"{results.count('cached')} cached. Directory: {destination}")


if __name__ == '__main__':
    main()
