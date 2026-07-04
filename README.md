# CN Patent Drafting Skill

## 中文简介

`cn-patent-drafting` 是一个供 Codex 使用的中国发明专利撰写技能，用于将论文、代码、设计文档、实验记录或零散技术说明整理为专利相关材料。

主要功能：

- 挖掘和筛选可申请的专利点；
- 辅助进行现有技术检索和差异化分析；
- 撰写中国专利技术交底书；
- 起草权利要求书、说明书、摘要和附图说明；
- 检查权利要求支持性、术语一致性、公式参数一致性和保护范围风险；
- 支持在已有草稿基础上增量合并、纠错和保留修订记录。

## 安装

方式一：在 Codex 中通过 GitHub 地址安装（推荐）。

在 Codex 对话中输入：

```text
Use $skill-installer to install the root skill from https://github.com/HuangXinzhe/cn-patent-drafting as cn-patent-drafting.
```

安装后重启 Codex，或开启新的 Codex 会话，使 skill 被重新发现。

方式二：手动克隆到 Codex 的 skills 目录。

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/HuangXinzhe/cn-patent-drafting.git "${CODEX_HOME:-$HOME/.codex}/skills/cn-patent-drafting"
```

核心功能不需要额外依赖；仓库内脚本仅使用 Python 标准库。

## 使用

在 Codex 中直接用 `$cn-patent-drafting` 调用，并提供技术材料、文件路径或撰写目标。例如：

```text
Use $cn-patent-drafting 帮我根据这些技术材料撰写一份中国发明专利技术交底书。
```

也可以指定更具体的任务：

```text
Use $cn-patent-drafting 帮我基于这篇论文挖掘3个可申请的中国发明专利点。
Use $cn-patent-drafting 帮我检查这份权利要求书和说明书是否存在支持性问题。
Use $cn-patent-drafting 帮我在已有交底书基础上合并这些补充材料，并保留修订记录。
```

## English Overview

`cn-patent-drafting` is a Codex skill for drafting Chinese invention patent materials from papers, source code, design documents, experimental notes, or technical descriptions.

Key capabilities:

- identify and rank patentable invention points;
- support prior-art search and differentiation analysis;
- draft Chinese patent disclosure documents;
- draft claims, specifications, abstracts, and figure descriptions;
- audit claim support, terminology consistency, formulas, parameters, and scope risks;
- revise existing drafts with timestamped versions and revision logs.

## Installation

Option 1: install from the GitHub URL inside Codex (recommended).

Type this in a Codex conversation:

```text
Use $skill-installer to install the root skill from https://github.com/HuangXinzhe/cn-patent-drafting as cn-patent-drafting.
```

Restart Codex or open a new Codex session after installation so the skill can be discovered.

Option 2: manually clone this repository into your Codex skills directory.

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/HuangXinzhe/cn-patent-drafting.git "${CODEX_HOME:-$HOME/.codex}/skills/cn-patent-drafting"
```

The core skill has no extra runtime dependency; bundled helper scripts use only the Python standard library.

## Usage

Invoke the skill in Codex with `$cn-patent-drafting`, then provide your technical materials, file paths, or drafting goal. Example:

```text
Use $cn-patent-drafting to turn these technical materials into a Chinese invention patent disclosure and application draft.
```

More examples:

```text
Use $cn-patent-drafting to identify three Chinese invention patent opportunities from this paper.
Use $cn-patent-drafting to audit whether these claims are fully supported by the specification.
Use $cn-patent-drafting to merge these supplemental materials into the existing disclosure and keep a revision log.
```
