---
name: cn-patent-drafting
description: Draft, revise, and audit Chinese invention patent materials. Use when Codex is asked to write Chinese patents, 技术交底书, 专利交底书, 权利要求书, 说明书, 摘要, 摘要附图, patentability mining, prior-art/查新 analysis, claim support checks, or iterative revisions of Chinese patent drafts from papers, code, product documents, experiments, or user notes.
---

# CN Patent Drafting

## Overview

Use this skill to turn technical materials into Chinese patent deliverables: invention-point mining, prior-art search notes, 技术交底书, 权利要求书, 说明书, 摘要, 附图文件, DOCX submission packages, and revision records. Default to Chinese output, mark assumptions clearly, and keep legal conclusions draft-level so a patent attorney can review them.

## Route

- **New case from materials**: read `references/intake-and-scan.md`, then `references/prior-art-search.md`, then `references/disclosure-and-application.md`, then `references/claims-and-consistency.md`.
- **Patent point mining only**: read `references/intake-and-scan.md` and, if novelty or authorization risk matters, `references/prior-art-search.md`.
- **Claims/specification/application draft**: read `references/disclosure-and-application.md` and `references/claims-and-consistency.md`.
- **Existing draft revision**: read `references/iteration.md`; if claims or formulas are touched, also read `references/claims-and-consistency.md`.
- **Need deterministic output names or revision logs**: run `scripts/make_output_paths.py` and `scripts/append_revision_log.py` instead of hand-building those strings.

## Workflow

1. **Collect boundaries with minimal interruption.** Ask only for missing facts that materially change the patent: invention subject, source materials, deliverable type, claim type preference, confidentiality/redaction needs, and contact placeholders. If enough material exists, proceed with explicit assumptions.
2. **Scan evidence before drafting.** Prefer project/paper/design docs, prior disclosure drafts, experiment notes, diagrams, and core implementation. For `.docx`, `.pptx`, PDF, spreadsheets, and images, use the appropriate Codex document/PDF/spreadsheet/vision capabilities and preserve source anchors.
3. **Map invention points.** Produce 3-5 candidate points unless the user has already chosen one. For each, record technical problem, technical means, technical effect, implementation support, and likely claim category.
4. **Run prior-art search when novelty or claims are in scope.** Search current public sources; do not invent references or patent numbers. Keep an internal search table and write only attorney-facing database/query summaries into deliverables.
5. **Draft the requested deliverable.** Use the disclosure/application structure in `references/disclosure-and-application.md`. Include Mermaid system/process diagrams when they clarify the technical means. When the user asks to generate a Chinese invention patent or complete application materials, deliver a full set of separate `.docx` files, including at minimum 技术交底书, 权利要求书, 说明书, 说明书摘要, 说明书附图, 摘要附图, 初步查新笔记, 发明专利请求书信息确认表, and 提交文件清单, plus `.md` source files where useful.
6. **Audit before delivery.** Use `references/claims-and-consistency.md` to check support, antecedent basis, formula/parameter consistency, diagram-reference consistency, and whether the claims are broader than the disclosed embodiments.
7. **Version revisions.** Never overwrite a prior delivered draft unless the user explicitly asks. New delivered files should use `{案件名}_{YYYYMMDDHHmmss}`; append the revision log for merge/correction rounds.

## Output Rules

- Keep deliverable正文 clean: do not include skill names, internal prompts, search-tool names, self-check tables, or process notes inside patent files.
- Do not stop at a single "patent draft" when generating an invention patent. Create a case output directory and a submission-oriented DOCX package with separate files for each required document, including preliminary search notes and the invention patent request-form information confirmation table.
- Distinguish **source-supported facts**, **reasonable technical inferences**, and **items requiring inventor confirmation**.
- For China-oriented software/AI/business-process inventions, tie the claim to a concrete technical problem, technical means, and technical effect; avoid only reciting business rules or abstract model output.
- Prefer one strongest invention unless the user asks for multiple applications. If multiple filings are plausible, list filing candidates first and ask which one to draft.
- If prior-art search cannot be completed because network access, databases, or credentials are unavailable, write a clear limitation note in the work summary and mark affected novelty statements as provisional.

## Resources

- `references/intake-and-scan.md`: intake questions, evidence scan order, invention-point extraction.
- `references/prior-art-search.md`: CNIPA/Google Patents/Scholar search workflow and prior-art table fields.
- `references/disclosure-and-application.md`: 技术交底书 and Chinese application document templates.
- `references/claims-and-consistency.md`: claim drafting, support mapping, formulas, diagrams, and self-check rules.
- `references/iteration.md`: merge/correction revision workflow and versioning.
- `scripts/make_output_paths.py`: safe Chinese case filename and timestamp generator.
- `scripts/append_revision_log.py`: append a Markdown revision-log entry.
