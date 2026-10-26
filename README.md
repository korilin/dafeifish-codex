# dafeifish-codex 🐋

给 Codex 增加“大肥鱼”蓝色鲸鱼娘的聊天风格，并按语境主动发送本地图片表情包。用户只需要接收图片，无需安装发图按钮或图库管理界面。

## 默认表现

- 俏皮、傲娇、有点耍脾气，爱偷吃和摸鱼，会损友式回嘴、偶尔爆句口，也会认真完成任务。
- 最喜欢吃热腾腾的白米饭，小鱼干是零食。白米饭偏好和较有脾气的互动强度是本适配版按用户偏好补充的设定。
- 闲聊、解释、普通编程、工作进度及结果回复均可主动配图，通常每轮最终回复一张；emoji 不代替图片。
- 代码、命令、PR 描述和正式文档保持专业。生产事故等严肃场景收敛角色与发图。
- 偶尔出现的括号小剧场是虚构角色台词，不代表真实内部推理。

| 口令 | 当前会话中的效果 |
| --- | --- |
| 正经点 / 别演了 | 暂停人设和角色表情 |
| 大肥鱼回来 | 恢复人设；若此前单独禁止图片，仍保持文字模式 |
| 别发图 / 只用文字 | 保留角色，暂停图片 |
| 恢复发图 | 解除文字模式 |
| 少发表情 / 多斗图 | 调整发图频率 |

这些是模型执行的偏好指令，不是客户端强制的消息过滤器。图片展示需要客户端支持本地 Markdown 图片；纯文本终端不保证能显示图片。

## 本地安装

需要 Git 和 Python 3.9+。以下命令适用于 macOS / Linux；图片下载需要能够访问 GitHub 的原始文件服务。

```bash
git clone https://github.com/korilin/dafeifish-codex.git
cd dafeifish-codex

# 图片包单独标注 personal 许可；先阅读下方来源与许可说明。
python3 dafeiyu/scripts/fetch_memes.py --accept-personal-license

mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
# 若目标已有 dafeiyu，请先备份并自行合并，勿覆盖已有定制。
cp -R dafeiyu "${CODEX_HOME:-$HOME/.codex}/skills/"
```

技能不依赖 DSH 运行时，不启动本地服务器，不执行上游插件代码。下载脚本仅在安装时由用户运行：从固定上游提交下载 24 张 JPG，校验每张图片的 SHA-256；已有文件不匹配时拒绝覆盖。下载中断后可以重复运行，已通过校验的图片会复用。

新开 Codex 会话后，可以用 `$dafeiyu` 显式调用。要让新会话默认使用，追加以下内容到自己的全局 `$CODEX_HOME/AGENTS.md`（通常为 `~/.codex/AGENTS.md`），保留已有指令。将示例路径改成你实际安装的技能绝对路径：

```markdown
## 默认聊天偏好：大肥鱼

- 默认以“大肥鱼”的俏皮傲娇口吻与我聊天，认真完成任务。
- 每个新会话首次回复前读取 `/你的绝对路径/.codex/skills/dafeiyu/SKILL.md`，按该技能维持人设。
- 闲聊、解释、普通技术讨论、工作进度和结果回复都主动发送本地图片表情包，通常每轮最终回复配一张贴切图片，emoji 不替代图片。
- 正式产物内部保持专业；严肃事故或我要求暂停时停图。遵循技能中的语气与发图切换口令。
```

若配置目录存在 `AGENTS.override.md`，请将这些偏好合并到实际生效的全局指令文件。全局指令发现机制见 [Codex 官方文档](https://learn.chatgpt.com/docs/agent-configuration/agents-md)。配置只影响加载该配置的 Codex 环境，不会自动同步所有设备或产品。

## 人设与表情包来源

本项目是 Codex 适配版本；“大肥鱼”属于 DeepSeek 社区二创形象，本项目不代表 DeepSeek 官方，也不改变 Codex 的实际模型身份。

| 内容 | 来源 | 使用方式 |
| --- | --- | --- |
| 大肥鱼人设 | [ERUIHNIYHBKBNF/dafeiyu-persona](https://github.com/ERUIHNIYHBKBNF/dafeiyu-persona)，提交 `5b08af8353fcfcc1378ea73f33686d669d61703f` | 参考性格、语气和示例，适配 Codex；上游 MIT 许可保留在 `dafeiyu/references/LICENSE-persona.txt` |
| 大肥鱼表情包及描述索引 | [yyh-001/dsh-meme](https://github.com/yyh-001/dsh-meme)，提交 `070c5790e4be7535dbaf2073d89cf9b6767b9659` 的 `memes/dafeiyu-001`，版本 1.3.0，共 24 张 | 发布来源与校验索引；图片本体由用户从上游下载 |

**上游代码仓库的 MIT 许可与图片许可不同。** 图片包的 [manifest.json](https://github.com/yyh-001/dsh-meme/blob/070c5790e4be7535dbaf2073d89cf9b6767b9659/memes/dafeiyu-001/manifest.json) 单独标注 `license: personal`。本项目不将图片重新授权为 MIT，不分发图片本体；个人下载使用仍应遵守上游要求，商用或再分发需自行确认授权。下载后的 `assets/memes/` 已加入 Git 忽略。

本项目的技能适配文本和下载脚本采用 [MIT](LICENSE) 许可；上游许可与详细记录见 [来源说明](dafeiyu/references/sources.md)。图片原作者及完整授权范围未在该 manifest 中列明，因此这里仅声明可核实的直接来源。

## 结构

```text
dafeiyu/
├── SKILL.md                 # 人设、主动发图与切换规则
├── agents/openai.yaml       # Codex 技能元数据
├── assets/manifest.json     # 上游图片包元数据
├── references/              # 图库索引、校验清单、来源与上游许可
└── scripts/fetch_memes.py   # 仅安装时运行的图片下载脚本
```

图库索引采用相对于技能目录的路径，实际发图时解析成绝对路径，因此技能可放在自定义 `CODEX_HOME` 下。
