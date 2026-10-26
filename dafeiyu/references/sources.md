# 来源与生成记录

更新日期：2026-10-26。

## 人设

- 参考 [ERUIHNIYHBKBNF/dafeiyu-persona](https://github.com/ERUIHNIYHBKBNF/dafeiyu-persona)，固定提交 `5b08af8353fcfcc1378ea73f33686d669d61703f`。
- 参考性格、语气和示例并改写为 Codex 指令；所谓内心 OS 改成虚构角色小剧场。
- 本适配版按用户偏好增加白米饭为头号心头好，以及损友式回嘴、耍小脾气和低频粗口。
- 保留上游 MIT 许可：LICENSE-persona.txt。

## 当前图片包：generated-v1

- 人物设计依据：用户于本会话提供的 Deepseek Chan 人物设计稿。图中可见署名 `@iamemily2050`；这是对图片上署名的记录，未独立核实其作者身份或授权范围。
- 图片通过 OpenAI 内置 `image_gen.imagegen` 工具按设计稿重新生成，非复制、裁切原图，也不使用原 dsh-meme 图库的图片。
- 共 8 张无文字的透明底插画；使用 Pillow 缩至 384×384 并优化 PNG，保留生成的 alpha 通道。
- 生成工具和完整提示词见 generation.json；文件尺寸、大小、SHA-256 见 ../assets/manifest.json。
- 设定图原文件及生成大图不纳入仓库；仓库包含缩小的成品图片，克隆后可离线使用。
- AI 生成的新图片仍基于该人物设计，不将人物形象声明为本项目原创，也不将第三方人物设计权利重新授权为 MIT。仓库根 MIT 许可适用于技能文本和代码，不涵盖第三方人物设计。

## 旧版图片来源

历史版本使用过 [yyh-001/dsh-meme](https://github.com/yyh-001/dsh-meme) 的 `dafeiyu-001` 图库。当前版本已停用并移除对应图片索引、下载脚本和校验清单，不再依赖该图库；此处仅保留历史来源记录。
