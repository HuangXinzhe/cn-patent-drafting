# CN Patent Drafting Skill

## 中文简介

`cn-patent-drafting` 是一个供 Codex 使用的中国发明专利撰写技能，用于将论文、代码、设计文档、实验记录或零散技术说明整理为专利相关材料。

主要功能：

- 挖掘和筛选可申请的专利点；
- 辅助进行现有技术检索和差异化分析；
- 撰写中国专利技术交底书；
- 起草权利要求书、说明书、说明书摘要、说明书附图和摘要附图；
- 生成提交专利用的成套 `.docx` 文件，而不只输出单个专利草案；
- 检查权利要求支持性、术语一致性、公式参数一致性和保护范围风险；
- 支持在已有草稿基础上增量合并、纠错和保留修订记录。

## 安装

### Codex Desktop Plugin Install

Codex Desktop 也可以将本仓库作为自定义插件市场安装。添加本仓库作为 marketplace source，然后安装 `cn-patent-drafting` 插件：

- Marketplace source: `https://github.com/HuangXinzhe/cn-patent-drafting.git`
- Branch/ref: `main`
- Plugin: `cn-patent-drafting`

插件根目录位于 `plugins/cn-patent-drafting/`。其中 `skills/` 目录包含 `cn-patent-drafting` skill 的实体副本，不使用 symlink，因此更适合 Codex Desktop 在 Windows 等环境中安装和缓存。

安装后重启 Codex，或开启新的 Codex 会话，使 plugin 内的 skill 被重新发现。测试调用：

```text
Use $cn-patent-drafting 帮我根据这些技术材料撰写一份中国发明专利技术交底书。
```

### Root Skill Install

如果只想安装 skill，也可以在 Codex 对话中通过 GitHub 地址安装仓库根目录的 root skill：

```text
Use $skill-installer to install the root skill from this GitHub repository:
https://github.com/HuangXinzhe/cn-patent-drafting

Install it as cn-patent-drafting.
```

如果希望用命令行安装器，也可以使用：

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py" --repo HuangXinzhe/cn-patent-drafting --path . --name cn-patent-drafting
```

### Manual Clone

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
- draft claims, specifications, specification abstracts, specification drawings, and abstract drawings;
- generate separate `.docx` files for a patent submission package, not only a single draft;
- audit claim support, terminology consistency, formulas, parameters, and scope risks;
- revise existing drafts with timestamped versions and revision logs.

## Installation

### Codex Desktop Plugin Install

Codex Desktop can also install this repository as a custom plugin marketplace. Add this repository as the marketplace source and install the `cn-patent-drafting` plugin:

- Marketplace source: `https://github.com/HuangXinzhe/cn-patent-drafting.git`
- Branch/ref: `main`
- Plugin: `cn-patent-drafting`

The plugin root lives at `plugins/cn-patent-drafting/`. Its `skills/` directory contains a materialized copy of the `cn-patent-drafting` skill, not a symlink. This keeps Codex Desktop installs portable on Windows and other environments where plugin caches may not preserve symlinks.

Restart Codex or open a new Codex session after installation so the plugin skill can be discovered. Test the skill:

```text
Use $cn-patent-drafting to turn these technical materials into a Chinese invention patent disclosure.
```

### Root Skill Install

If you only want to install the skill, you can also install the repository root skill from the GitHub URL inside Codex:

```text
Use $skill-installer to install the root skill from this GitHub repository:
https://github.com/HuangXinzhe/cn-patent-drafting

Install it as cn-patent-drafting.
```

You can also use the command-line installer:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py" --repo HuangXinzhe/cn-patent-drafting --path . --name cn-patent-drafting
```

### Manual Clone

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
