# 通用 AI 开发技能

`ai-dev-guardrails` 用于开发功能、修复缺陷、重构和代码评审。它从用户要完成的操作入手，在当前项目里找到对应实现和调用方，用项目已有的工具验证结果。前端、服务、库、命令行工具和批处理都可以使用。

例如，给导出工具增加一列时，旧脚本仍应能把编号 `"007"` 匹配到原记录。运行随附的用例，改掉编号的字段名会导致失败，增加可选字段则能通过。[查看可运行的例子](skills/ai-dev-guardrails/examples/cli-contract/test_report.py)

## 安装

从本仓库的 **Releases** 下载 `ai-dev-guardrails.zip`。解压后，把包含 `SKILL.md` 的整个 `ai-dev-guardrails` 文件夹放到所用工具的技能目录。也可从源码中直接复制同一目录。[技能文件](skills/ai-dev-guardrails)

| 使用范围 | Codex | Claude Code |
| --- | --- | --- |
| 当前用户的所有本地项目 | `~/.agents/skills/` | `~/.claude/skills/` |
| 随某个项目分发给团队 | 项目内的 `.agents/skills/` | 项目内的 `.claude/skills/` |

习惯用 Codex 安装器的用户，可以在 GitHub 打开对应版本的技能目录，复制浏览器地址，然后输入「用 $skill-installer 安装这个地址的技能」，附上刚复制的链接。[Codex 安装说明](https://developers.openai.com/codex/skills/) · [Claude Code 安装说明](https://code.claude.com/docs/en/skills)

## 在项目里怎么用

在目标项目打开新会话。Codex 使用 `$ai-dev-guardrails`，Claude Code 使用 `/ai-dev-guardrails`。把需求直接接在技能名后面即可。

| 想做什么 | 可以这样说 |
| --- | --- |
| 开发功能 | 给导出命令加一个可选的状态列。保留旧脚本读取编号的方式，完成实现并验证两种输出。 |
| 修复缺陷 | 批任务重试时偶尔重复计数。用一小批数据复现，从任务入口修复，再跑原来的例子。 |
| 重构 | 把价格计算从界面中提出来，保留现有的舍入行为，通过调用方验证重构结果。 |
| 只做评审 | 审一下这个分支，优先找会影响用户或下游的改动。给出文件位置和复验方法，先不改代码。 |

在空项目中，从用户能实际运行的一条路径开始。在已有项目中，沿用所属模块的约定、构建和测试入口。团队需要长期执行某条规则时，再把它加到本地检查和 CI。[如何接入第一条规则](skills/ai-dev-guardrails/references/adoption.md)

## 运行示例

从源码运行时，先进入 `skills/ai-dev-guardrails/`。从发布包运行时，进入解压得到的 `ai-dev-guardrails/`。示例只用 Python 3 标准库，其他语言的项目沿用各自的测试工具。

```sh
python3 -B -m unittest discover -s examples/cli-contract -p 'test_*.py' -v
```

采用 [Apache License 2.0](LICENSE) 开源。
