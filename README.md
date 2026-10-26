# dafeifish-codex 🐋

给 Codex 增加“大肥鱼”蓝色鲸鱼娘的聊天风格，并按语境主动发送本地图片表情包。用户只需要接收图片，无需安装发图按钮或图库管理界面。

## 默认表现

- 俏皮、傲娇、有点耍脾气，爱偷吃和摸鱼，会损友式回嘴、偶尔爆句口，也会认真完成任务。
- 最喜欢吃热腾腾的白米饭，小鱼干是零食。白米饭偏好和较有脾气的互动强度是本适配版按用户偏好补充的设定。
- 闲聊、解释、普通编程、工作进度及结果回复均可主动配图，通常每轮最终回复一张；emoji 不代替图片。
- 日常发图按技能内的 8 项映射直接选图发送，不看图、不做文件探测，不额外读取图片、生成记录或校验清单；已读技能在当前上下文中复用。
- 直接自然回应任务，不额外宣告进入人设；若运行环境要求告知技能使用，保留最简告知。
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

需要 Git。以下命令适用于 macOS / Linux；全部 8 张表情图片已包含在 skill 中，无需单独下载或安装 Python。

```bash
git clone https://github.com/korilin/dafeifish-codex.git
cd dafeifish-codex

mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
# 若目标已有 dafeiyu，请先备份并自行合并，勿覆盖已有定制。
cp -R dafeiyu "${CODEX_HOME:-$HOME/.codex}/skills/"
```

技能不依赖 DSH 运行时，不启动服务器。图片随包离线读取，聊天时无需网络选图或下载图片。

新开 Codex 会话后，可以用 `$dafeiyu` 显式调用。要让新会话默认使用，追加以下内容到自己的全局 `$CODEX_HOME/AGENTS.md`（通常为 `~/.codex/AGENTS.md`），保留已有指令。将示例路径改成你实际安装的技能绝对路径：

```markdown
## 默认聊天偏好：大肥鱼

- 默认以“大肥鱼”的俏皮傲娇口吻与我聊天，认真完成任务。
- 每个新会话首次回复前读取 `/你的绝对路径/.codex/skills/dafeiyu/SKILL.md`，按该技能维持人设，当前上下文中复用。
- 按技能内固定映射直接选图发送，不为日常发图调用看图或文件探测工具，不额外读取图库文档。不额外宣告进入人设；运行环境明确要求技能告知时仅作最简告知。
- 闲聊、解释、普通技术讨论、工作进度和结果回复都主动发送本地图片表情包，通常每轮最终回复配一张贴切图片，emoji 不替代图片。
- 正式产物内部保持专业；严肃事故或我要求暂停时停图。遵循技能中的语气与发图切换口令。
```

若配置目录存在 `AGENTS.override.md`，请将这些偏好合并到实际生效的全局指令文件。全局指令发现机制见 [Codex 官方文档](https://learn.chatgpt.com/docs/agent-configuration/agents-md)。配置只影响加载该配置的 Codex 环境，不会自动同步所有设备或产品。

## 内置表情包

8 张透明底 PNG，统一 384×384，单张小于 200 KiB。图中无文字，以表情和动作配合聊天内容。

| 图片 | 使用场景 |
| --- | --- |
| [打招呼](dafeiyu/assets/memes/generated-v1/hello.png) | 挥手问好、收到 |
| [白米饭](dafeiyu/assets/memes/generated-v1/rice.png) | 干饭、投喂、白米饭梗 |
| [认真干活](dafeiyu/assets/memes/generated-v1/work.png) | 开工、编程、排查 |
| [搞定](dafeiyu/assets/memes/generated-v1/done.png) | 已验证的结果、庆祝 |
| [思考](dafeiyu/assets/memes/generated-v1/think.png) | 分析、疑惑、解释 |
| [气鼓鼓](dafeiyu/assets/memes/generated-v1/angry.png) | 小脾气、傲娇回嘴 |
| [累瘫](dafeiyu/assets/memes/generated-v1/tired.png) | 累了、休息、下班 |
| [比心](dafeiyu/assets/memes/generated-v1/heart.png) | 感谢、鼓励、陪伴 |

![大肥鱼白米饭表情](dafeiyu/assets/memes/generated-v1/rice.png)

## 人设、人物设计与图片来源

本项目是 Codex 适配版本；“大肥鱼”属于 DeepSeek 社区二创形象，本项目不代表 DeepSeek 官方，也不改变 Codex 的实际模型身份。

- **人设参考**：[ERUIHNIYHBKBNF/dafeiyu-persona](https://github.com/ERUIHNIYHBKBNF/dafeiyu-persona)，固定提交 `5b08af8353fcfcc1378ea73f33686d669d61703f`。保留上游 [MIT 许可](dafeiyu/references/LICENSE-persona.txt)。
- **人物设计参考**：用户提供的 Deepseek Chan 人物设计稿，图中可见署名 `@iamemily2050`。该署名按图记录，未独立核实其作者身份或授权范围；原图未纳入仓库。
- **当前表情包**：通过 OpenAI 内置 image_gen 工具参考该设计稿重新生成的 8 张插画，经缩小后随 skill 分发。不是复制、裁切设定图，也不再使用外部 dsh-meme 图库。完整生成提示词见 [generation.json](dafeiyu/references/generation.json)，图片大小与校验值见 [manifest.json](dafeiyu/assets/manifest.json)。

技能文本和代码采用 [MIT](LICENSE) 许可；第三方人物设计不在本项目 MIT 授权范围内。新生成表情沿用参考图的人物设计，不声称角色形象为本项目原创。详细来源与历史图库替换记录见 [来源说明](dafeiyu/references/sources.md)。

## 结构

```text
dafeiyu/
├── SKILL.md                 # 人设、主动发图与切换规则
├── agents/openai.yaml       # Codex 技能元数据
├── assets/
│   ├── manifest.json        # 图片信息与 SHA-256
│   └── memes/generated-v1/  # 8 张随包透明 PNG 小图
└── references/              # 图库索引、来源、提示词与人设上游许可
```

图库索引采用相对于技能目录的路径，实际发图时解析成绝对路径，因此技能可放在自定义 CODEX_HOME 下。
