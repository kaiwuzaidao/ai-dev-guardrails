# AI 开发不失控

一个从 Kaiwu 提炼出来的 Agent Skill。给 AI 一个已有项目，它会沿真实调用方找出容易被改坏的行为，复用项目自己的测试工具，把约定变成下次改代码时能跑的检查。适用于服务、前端、库、命令行工具和批处理，运行技能无需安装 Kaiwu。

例如，导出工具把订单号 `"007"` 写成了数字 `7`。程序仍然正常退出，但旧脚本再也关联不到这笔订单。这个仓库附带一个可运行的例子：它从命令行喂入订单号，按旧脚本的方式读取结果，因此能发现字段改名或前导零丢失，同时允许新增字段。[查看用例](skills/ai-dev-guardrails/examples/cli-contract/test_report.py)

*A stack-independent Agent Skill for AI-assisted development. Identify the contracts real consumers rely on, turn costly regressions into executable checks, and leave the next maintainer with reproducible evidence.*

## 安装到所有本地项目

安装单位是 [skills/ai-dev-guardrails](skills/ai-dev-guardrails) 整个目录。使用 Codex 自带的技能安装器时，可以直接输入：

```text
用 $skill-installer 安装 https://github.com/kaiwuzaidao/ai-dev-guardrails/tree/v0.1.0/skills/ai-dev-guardrails
```

也可以在 macOS 或 Linux 手动安装。先把指定版本克隆到一个会长期保留的位置：

```sh
git clone --depth 1 --branch v0.1.0 https://github.com/kaiwuzaidao/ai-dev-guardrails.git
cd ai-dev-guardrails
```

然后从仓库根目录执行对应的两行命令，把技能链接到工具的用户目录：

```sh
# Codex
mkdir -p "$HOME/.agents/skills"
ln -s "$PWD/skills/ai-dev-guardrails" "$HOME/.agents/skills/"

# Claude Code
mkdir -p "$HOME/.claude/skills"
ln -s "$PWD/skills/ai-dev-guardrails" "$HOME/.claude/skills/"
```

也可把技能目录直接复制到相应位置。给团队随仓分发时，使用项目内的 `.agents/skills/`（Codex）或 `.claude/skills/`（Claude Code）。其他能读取 Markdown 的工具可从 [SKILL.md](skills/ai-dev-guardrails/SKILL.md) 开始。[Codex 技能目录](https://developers.openai.com/codex/skills/) · [Claude Code 技能目录](https://code.claude.com/docs/en/skills)

## 在项目里怎么用

在目标项目打开新会话。Codex 使用 `$ai-dev-guardrails`，Claude Code 使用 `/ai-dev-guardrails`。可以直接复制下面任意一句：

- **只做评审**　「用 $ai-dev-guardrails 审一下这次改动。找出旧调用方会受影响的地方，列出证据和缺失的用例，先不改代码。」
- **接入项目**　「用 $ai-dev-guardrails 给这个老项目补第一条门禁。从最近修过的回归入手，复用现有测试和 CI，证明它能拦住旧错误。」
- **接力开发**　「用 $ai-dev-guardrails 接手这个分支。核对哪些行为已经验证、本地和 CI 各跑了什么，再继续完成尚未验证的部分。」

## 跑一次例子

在本仓库根目录执行以下命令，只需 Python 3 标准库。GitHub Actions 运行同一组测试。

```sh
cd skills/ai-dev-guardrails
python3 -B -m unittest discover -s examples/cli-contract -p 'test_*.py' -v
```

要看它怎样拦住错误，可在临时副本中把公开字段 `id` 改名后重跑。要在自己的项目落地，参考[第一条规则的接入示例](skills/ai-dev-guardrails/references/adoption.md)。

## 哪些做法来自 Kaiwu

| Kaiwu 的做法 | 其他项目可以怎么用 |
| --- | --- |
| 约束按风险分成 MUST、WARN、DEFAULT，可豁免项有负责人和到期日 | 区分会破坏业务的错误、需要提醒的偏离和团队偏好。[ADR 0020](https://github.com/kaiwuzaidao/kaiwu-system-service/blob/0b3033c77cf41f024b78ad0a761d71c7e00bea19/docs/adr/0020-risk-tiered-engineering-constraints.md) |
| 生成基础骨架，业务代码由团队在自己的仓库持续维护 | 确定哪些文件由生成器拥有，让业务仓自己审阅模板升级，用仓内规则接手开发。[ADR 0038](https://github.com/kaiwuzaidao/kaiwu-system-service/blob/0b3033c77cf41f024b78ad0a761d71c7e00bea19/docs/adr/0038-deterministic-scaffold-and-ai-tool-development.md) |
| 业务规则有对应场景，仓库提供本地验证入口 | 同时验证成功、拒绝或冲突的结果，使换人换模型后仍能按同一条命令验收。[业务场景](https://github.com/kaiwuzaidao/kaiwu-web-starter/blob/dba51f7f43ec5cc44b6166d57e4ae2b150d16d5c/docs/acceptance-scenarios.md) · [校验入口模板](https://github.com/kaiwuzaidao/kaiwu-system-service/blob/0b3033c77cf41f024b78ad0a761d71c7e00bea19/kaiwu-system-domain/src/main/resources/templates/project/backend/verify.sh.ftl) |
| 用稳定业务键和移交基线识别环境间的配置漂移 | 先展示目标环境可能被覆盖的差异，再处理删除、授权等有副作用的操作。[ADR 0042](https://github.com/kaiwuzaidao/kaiwu-system-service/blob/0b3033c77cf41f024b78ad0a761d71c7e00bea19/docs/adr/0042-project-config-handover.md) |

采用 [Apache License 2.0](LICENSE) 开源。
