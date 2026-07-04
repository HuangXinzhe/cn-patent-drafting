# Disclosure And Application Drafting

## Deliverable Types

Confirm the deliverable, then draft only what was requested unless the user asks to generate a Chinese invention patent or complete application materials. In that case, create a complete submission-oriented package, not only a single draft.

- 技术交底书: inventor/attorney-facing technical disclosure.
- 权利要求书: independent and dependent claims.
- 说明书: 技术领域, 背景技术, 发明内容, 附图说明, 具体实施方式.
- 摘要: short technical summary, usually around 300 Chinese characters or less unless the user's template says otherwise.
- 说明书附图: formal figure sheets or figure-source drafts for the specification.
- 摘要附图: one representative figure for the abstract, usually selected from the specification drawings.
- 查新笔记: search table and difference analysis.

## Complete Invention Patent Package

When the user asks to "生成发明专利", "撰写完整专利", "提交专利", or "生成申请文件", deliver both the patent draft/summary and separate DOCX files for the submission package. Do not merge everything into one Word file unless the user explicitly asks.

Create a case output directory and include at least:

| File | Required content |
|---|---|
| `00_专利草案总览.md` / `.docx` | Optional overview: invention title, invention points, document list, open issues. |
| `01_技术交底书.md` / `.docx` | Technical disclosure for inventor/attorney communication. |
| `02_权利要求书.md` / `.docx` | Independent and dependent claims. |
| `03_说明书.md` / `.docx` | Technical field, background, invention content, figure description, embodiments. |
| `04_说明书摘要.md` / `.docx` | Abstract text, concise and attorney-facing. |
| `05_说明书附图.md` / `.docx` | Specification drawings, figure titles, reference signs, and diagram sources/placeholders. |
| `06_摘要附图.md` / `.docx` | Abstract figure or selected representative drawing with reference signs. |
| `07_查新与差异化分析.md` / `.docx` | Optional but recommended when prior-art search was performed. |
| `提交文件清单.md` / `.docx` | Checklist of generated files and items requiring inventor/attorney confirmation. |

Use `.md` as editable source when useful, but the user-facing submission package must include the `.docx` counterparts. If the environment cannot create DOCX files, state the blocker clearly, preserve the `.md` sources, and provide the exact conversion path or command needed to generate DOCX files.

For drawings:

- Use Mermaid or another locally available drawing workflow to create source diagrams when the invention is software/system/process oriented.
- Do not fabricate undisclosed structures. If a drawing requires inventor confirmation, include a clear placeholder such as "需发明人确认的图X".
- Keep `说明书附图` and `摘要附图` as separate files even if the abstract figure is selected from the same drawing set.

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

Delivered patent package files should use a case directory and stable document prefixes:

```text
outputs/{规范化案件名}_{YYYYMMDDHHmmss}/
  00_专利草案总览.md/.docx
  01_技术交底书.md/.docx
  02_权利要求书.md/.docx
  03_说明书.md/.docx
  04_说明书摘要.md/.docx
  05_说明书附图.md/.docx
  06_摘要附图.md/.docx
  提交文件清单.md/.docx
```

Use `scripts/make_output_paths.py` to generate the timestamped case directory or main stem when saving files.

For a complete package path map, run:

```bash
python3 scripts/make_output_paths.py --case-name "一种XXX方法及系统" --package --also-docx
```
