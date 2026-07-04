# Disclosure And Application Drafting

## Deliverable Types

Confirm the deliverable, then draft only what was requested unless a complete set is useful.

- 技术交底书: inventor/attorney-facing technical disclosure.
- 权利要求书: independent and dependent claims.
- 说明书: 技术领域, 背景技术, 发明内容, 附图说明, 具体实施方式.
- 摘要: short technical summary, usually around 300 Chinese characters or less unless the user's template says otherwise.
- 摘要附图/附图说明: diagrams and reference signs.
- 查新笔记: search table and difference analysis.

## Technical Disclosure Template

Use this structure for a Chinese invention disclosure unless the user provides a template:

```markdown
# 技术交底书

**案件名称**：一种[技术主题]方法、装置、设备及存储介质

**技术联系人**：
- 姓名：待填写
- 电话：待填写
- 邮箱：待填写

**专利类型**：发明

## 一、技术背景与现有技术
### 1.1 现有技术
### 1.2 现有技术存在的缺点

## 二、本发明所要解决的技术问题

## 三、本发明技术方案的详细阐述
### 3.1 应用场景与总体思路
### 3.2 系统框图
### 3.3 模块/部件功能及关联关系
### 3.4 方法流程
### 3.5 关键参数、公式或条件
### 3.6 可选实施方式

## 四、与现有技术相比的有益效果

## 五、技术关键点和欲保护点

## 六、实施例及可替换方案
```

Use fenced Mermaid for system and flow diagrams when helpful. Keep diagram labels short and consistent with the text.

## Chinese Application Document Structure

### 权利要求书

Draft claims before finalizing the specification if the protection scope is the main task.

```text
1. 一种[方法/装置/系统/设备/介质]，其特征在于，包括：
   [必要技术特征A]；
   [必要技术特征B]；
   [必要技术特征C]，
   其中，[限定核心区别的技术关系]。

2. 根据权利要求1所述的[主题]，其特征在于，[从属限定1]。
```

For software/AI cases, consider parallel independent claims only when supported:

- method claim,
- system/device/apparatus claim with modules,
- electronic device claim,
- computer-readable storage medium claim.

### 说明书

Use this structure:

```markdown
# 说明书

## 技术领域

## 背景技术

## 发明内容
### 要解决的技术问题
### 技术方案
### 有益效果

## 附图说明

## 具体实施方式
```

In "技术方案", mirror the independent claim but expand with support. In "具体实施方式", give enough embodiments, alternatives, parameter ranges, and edge handling so the claim is enabled.

### 摘要

Write one compact paragraph:

- invention subject,
- core technical means,
- main technical effect,
- main application.

Avoid claim numbers, internal notes, exaggerated legal conclusions, or marketing language.

### 附图说明

List figures with concise titles:

```text
图1为本发明实施例提供的系统结构示意图；
图2为本发明实施例提供的方法流程示意图。
```

Use reference signs only if they are consistently used in drawings and text.

## Drafting Style

- Use "本发明实施例", "在一些实施例中", "可选地", "进一步地" to separate mandatory and optional features.
- Do not overuse "显著", "完全", "最优" unless supported by evidence.
- Translate product/company-specific terms into generic technical terms unless the user asks to preserve them.
- Put technical details in the specification; keep benefits in 有益效果 concise and traceable.
- Do not include "自检", "检索工具", "由AI生成", or skill/repository references in the deliverable.

## Output Naming

Delivered patent files should use:

```text
{规范化案件名}_{YYYYMMDDHHmmss}.md
{规范化案件名}_{YYYYMMDDHHmmss}.docx
```

Use `scripts/make_output_paths.py` to generate names when saving files.
