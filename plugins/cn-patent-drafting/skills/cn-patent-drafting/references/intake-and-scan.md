# Intake And Evidence Scan

## Minimal Intake

Ask only what changes the patent strategy. If the user already provided enough material, proceed and list assumptions.

- 技术主题: one sentence naming the product, algorithm, apparatus, process, compound, or use scenario.
- Desired deliverable: 专利点挖掘, 技术交底书, 权利要求书, 说明书, 摘要, 全套申请文件, or revision.
- Claim category preference: 方法, 系统/装置, 介质/设备, 产品/组合物, 用途, or uncertain.
- Source materials: file paths, repo paths, paper/PDF, experiment notes, architecture diagrams, prior drafts, user notes.
- Redaction level: company/product names, customer data, exact parameters, unpublished results.
- Contact/header placeholders: inventor/contact fields, if the user's template requires them.

## Evidence Priority

Scan in this order and keep source anchors for every important technical fact.

| Priority | Source type | What to extract |
|---|---|---|
| 1 | Existing patent notes, disclosure drafts, invention reports | Claimed novelty, known embodiments, desired protection scope |
| 2 | Design docs, papers, slides, lab notes | Problem, architecture, algorithm/process, experiments, technical effects |
| 3 | Core code or configuration | Actual implementation, data flow, parameters, thresholds, state machines |
| 4 | Product docs, issue discussions, meeting notes | Constraints, deployment conditions, edge cases, user-facing effects |
| 5 | Raw figures/tables | Architecture, process, experimental evidence, parameter ranges |

For `.docx`, `.pptx`, PDF, spreadsheet, or image sources, use the relevant Codex file skills/tools to extract text and figures. Do not skip Office/PDF sources merely because plain text files are available.

## Invention-Point Extraction

Create a candidate table with these fields:

- Candidate title: "一种..." working title.
- Technical problem: a concrete defect in prior systems or known techniques.
- Technical means: the actual structure, sequence, algorithm, parameter relation, material composition, or device cooperation.
- Technical effect: measurable or technically explainable effect, not only commercial value.
- Evidence support: file/path/page/section/function.
- Claim category: method, system/device, computer-readable medium, product, use, etc.
- Disclosure gaps: missing facts to ask the inventor.
- Risk: abstract idea, insufficient implementation, prior-art proximity, unsupported effect, or unclear boundary.

## Patentability Heuristics For China-Oriented Drafts

- Prefer "technical problem - technical means - technical effect" framing.
- For software, AI, data processing, and business-adjacent inventions, anchor the invention in concrete data processing, system resources, model training/inference control, device interaction, reliability, speed, storage, security, or other technical effects.
- Avoid presenting pure rules, human decisions, business logic, presentation formats, or desired results as the inventive feature.
- Tie each broad claim element to at least one disclosed embodiment and one technical effect.
- Separate indispensable features from optional optimizations before drafting claims.

## Candidate Selection

Default to one strongest filing unless the user asks for multiple. Choose based on:

- the clearest technical contribution,
- the strongest evidence support,
- the most defensible distinction from searched prior art,
- whether the technical effect can be explained without overclaiming,
- whether the scope can be broadened without losing support.

When multiple filings are plausible, present a short filing map: title, core difference, likely independent claim, and why it should or should not be separated.
