# Claims And Consistency Audit

## Claim Drafting Principles

- Independent claims should contain only indispensable technical features needed to distinguish the invention and solve the technical problem.
- Dependent claims should add meaningful fallback limitations: data preprocessing, module cooperation, thresholds, model/training details, device structure, parameter ranges, exception handling, or specific embodiments.
- Each claim element must be supported by the specification. If support is weak, either add support to the specification or narrow the claim.
- Use clear antecedent basis: introduce an object before referring to "所述对象".
- Avoid result-only features such as "提高准确率" unless tied to the technical means that achieves it.
- Avoid mixing method steps and apparatus structure in one claim unless written as functional modules of an apparatus claim.

## Claim Set Patterns

### Method

```text
1. 一种[技术主题]方法，其特征在于，包括：
获取[对象/数据]；
基于[技术规则/模型/结构]对所述[对象/数据]进行[处理]，得到[中间结果]；
根据[中间结果]执行[核心控制/生成/判断/调度]，得到[技术输出]。
```

### Apparatus/System

```text
1. 一种[技术主题]装置，其特征在于，包括：
获取模块，用于...；
处理模块，用于...；
输出模块，用于...。
```

### Device/Medium

Use device and storage-medium claims only when method support is present:

```text
一种电子设备，包括处理器和存储器，所述存储器存储有计算机程序，所述计算机程序被所述处理器执行时实现权利要求1至N任一项所述的方法。
```

## Support Mapping

Before delivery, build a quick internal map:

| Claim feature | Support section | Figure/step | Notes |
|---|---|---|---|
| Feature A | 具体实施方式/段落 | 图1/S1 | mandatory or optional |

If a feature appears in claims but not in the description, fix the description or remove/narrow the feature.

## Formula And Parameter Rules

- Define symbols before formulas.
- Keep the same symbol form across formulas, parameter tables, examples, and claims.
- Use subscripts for dimensions such as `\mathrm{cpu}`, `\mathrm{mem}`, `\mathrm{io}`; avoid superscripts for field names.
- Do not reuse one letter for different objects.
- Check inequality direction, boundary values, denominator-zero handling, and whether formulas match the described flow.
- If formulas are not necessary for the invention, prefer clear process/relationship descriptions over decorative math.

## Diagram Consistency

- Each drawing referenced in the text should exist.
- Each reference sign used in a drawing should be explained if the document uses reference signs.
- Method steps in claims should correspond to flowchart steps where possible.
- Apparatus modules should correspond to the system diagram and module descriptions.

## Final Audit

Run this audit before delivering:

- If generating a Chinese invention patent package, are separate DOCX files present for 技术交底书, 权利要求书, 说明书, 说明书摘要, 说明书附图, 摘要附图, 初步查新笔记, 发明专利请求书信息确认表, and 提交文件清单?
- Does `发明专利请求书信息确认表` clearly mark unknown applicant, inventor, priority, contact, agency, fee-reduction, and attachment information as 待填写/需确认 rather than inventing it?
- Does `提交文件清单` list every generated file and every item still requiring inventor/attorney confirmation?
- Does the draft state a concrete technical problem?
- Are the technical means enough for a skilled person to implement?
- Are the claimed effects supported by mechanisms or evidence?
- Are prior-art distinctions specific and not exaggerated?
- Is each independent claim broader than, but still supported by, the embodiments?
- Are optional features placed in dependent claims or optional embodiments?
- Are claim terms consistent with specification terms?
- Are all files free of internal process notes, skill names, and self-check tables?

When uncertain, mark "需发明人确认" in the response summary, not inside the formal patent text unless the user wants placeholders.
