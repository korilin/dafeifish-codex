# dafeifish-codex 🐋

给 Codex 增加“大肥鱼”蓝色鲸鱼娘的聊天风格，并按语境主动发送本地图片表情包。用户只需要接收图片，无需安装发图按钮或图库管理界面。

## 默认表现

- 俏皮、傲娇、有点耍脾气，爱偷吃和摸鱼，会损友式回嘴、偶尔爆句口，也会认真完成任务。
- 最喜欢吃热腾腾的白米饭，小鱼干是零食。白米饭偏好和较有脾气的互动强度是本适配版按用户偏好补充的设定。
- 闲聊、解释、普通编程、工作进度及结果回复均可主动配图，通常每轮最终回复一张；emoji 不代替图片。
- 日常发图按全局偏好中的 10 项映射直接选图发送，不看图、不做文件探测，不额外读取图片、生成记录或校验清单；无需为发图额外加载技能。
- 默认人设和图片映射直接由全局偏好提供；普通任务不调用人设技能，开场只说明任务行动。用户明确调用技能时，仍遵循环境的技能告知要求。
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

需要 Git。以下命令适用于 macOS / Linux；全部 10 张表情图片已包含在 skill 中，无需单独下载或安装 Python。

```bash
git clone https://github.com/korilin/dafeifish-codex.git
cd dafeifish-codex

mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
# 若目标已有 dafeiyu，请先备份并自行合并，勿覆盖已有定制。
cp -R dafeiyu "${CODEX_HOME:-$HOME/.codex}/skills/"
```

技能不启动服务器。图片随包离线读取，聊天时无需网络选图或下载图片。

要让新会话默认使用，将 [全局偏好模板](examples/global-preferences.md) 追加到自己的全局 `$CODEX_HOME/AGENTS.md`（通常为 `~/.codex/AGENTS.md`），保留已有指令。将其中 `__SKILL_DIR__` 替换为实际安装目录的绝对路径。

模板直接包含人设、口令和 10 项图片映射，日常任务无需先读取或调用人设技能。因此开场可以直接说明“检查源文案并上传，随后核对结果”，不用再补一句“遵循大肥鱼技能的聊天偏好”。如有旧版“每个新会话首次回复前读取 SKILL.md”的全局指令，请用模板替换该段，避免继续触发技能调用。

`$dafeiyu` 仍可显式调用以配置、调整或维护人设与图库；实际调用技能时，运行环境仍可能要求说明所用技能。新开会话验证默认偏好，其他产品或设备不会自动同步。

若配置目录存在 `AGENTS.override.md`，请将这些偏好合并到实际生效的全局指令文件。全局指令发现机制见 [Codex 官方文档](https://learn.chatgpt.com/docs/agent-configuration/agents-md)。配置只影响加载该配置的 Codex 环境，不会自动同步所有设备或产品。

## 内置表情包

10 张白底 PNG，统一 384×384，单张小于 200 KiB。采用 2D 平涂，人物和文字不带白描边；部分表情配黑色短文案。

| 图片 | 使用场景 |
| --- | --- |
| [打招呼](dafeiyu/assets/memes/generated-v1/hello.png) | 挥手问好、收到 |
| [白米饭](dafeiyu/assets/memes/generated-v1/rice.png) | 戴锅盔干饭；开饭！ |
| [认真干活](dafeiyu/assets/memes/generated-v1/work.png) | 本鱼开工；仅限真正开始执行任务，不用于方案、未启动说明、中途或结果汇报 |
| [搞定](dafeiyu/assets/memes/generated-v1/done.png) | 已验证的结果、庆祝 |
| [思考](dafeiyu/assets/memes/generated-v1/think.png) | 分析、疑惑、解释 |
| [气鼓鼓](dafeiyu/assets/memes/generated-v1/angry.png) | 小脾气、傲娇回嘴 |
| [累瘫](dafeiyu/assets/memes/generated-v1/tired.png) | 累了、休息、下班 |
| [比心](dafeiyu/assets/memes/generated-v1/heart.png) | 感谢、鼓励、陪伴；爱你哦 |
| [又急啦？](dafeiyu/assets/memes/generated-v1/hurry.png) | 站姿微笑叉腰、藐视眼；催促或斗嘴时轻度调侃 |
| [错了，错了](dafeiyu/assets/memes/generated-v1/sorry.png) | 抱头蹲防；自己犯错、用户因此生气时认错并纠正 |

![大肥鱼白米饭表情](dafeiyu/assets/memes/generated-v1/rice.png)

## 图片生成与许可

10 张内置表情根据用户提供的人物设计稿，通过 OpenAI 内置 image_gen 工具生成。完整提示词见 [generation.json](dafeiyu/references/generation.json)，图片大小与校验值见 [manifest.json](dafeiyu/assets/manifest.json)。

技能文本和代码采用 [MIT](LICENSE) 许可。人物设计和生成图片不在该 MIT 授权范围内；设计参考记录保留在生成元数据中。

## 结构

```text
dafeiyu/
├── SKILL.md                 # 人设、主动发图与切换规则
├── agents/openai.yaml       # Codex 技能元数据
├── assets/
│   ├── manifest.json        # 图片信息与 SHA-256
│   └── memes/generated-v1/  # 10 张随包白底 PNG 小图
└── references/              # 图库索引与生成提示词
```

图库索引采用相对于技能目录的路径，实际发图时解析成绝对路径，因此技能可放在自定义 CODEX_HOME 下。
