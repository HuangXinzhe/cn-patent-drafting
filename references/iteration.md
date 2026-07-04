# Iteration Workflow

Use this when the user asks to modify, supplement, merge, correct, strengthen protection points, or continue from an existing patent draft.

## Classify The Revision

- **Merge/supplement**: new material, new embodiment, added data, extra module, expanded scenario.
- **Correction**: factual error, wrong parameter, inconsistent formula, incorrect prior art, terminology issue.
- **Claim strengthening**: adjust 第五章, 权利要求书, or protection focus without adding new technical facts.
- **Full rewrite**: user explicitly asks to rebuild from source or change the invention direction.

## Required Inputs

- The baseline draft path or the latest draft from the conversation.
- The user's revision request or supplemental material.
- Any files mentioned by the user.

If the baseline draft is missing and cannot be inferred, ask for it.

## Revision Rules

- Do not return to full invention mining when the user is clearly revising an existing draft, unless they explicitly ask to restart.
- Preserve unaffected sections.
- Add or rewrite only the sections affected by the revision, then audit cross-section consistency.
- If the revision changes technical substance, decide whether prior-art search and claim support need to be refreshed.
- Never overwrite a delivered draft by default. Save a new timestamped version.

## Output Files

Use:

```bash
python3 scripts/make_output_paths.py --case-name "一种XXX方法及系统" --case-dir outputs/case --also-docx
```

Then write the revised `.md`, generate `.docx` if requested/possible, and append a revision log:

```bash
python3 scripts/append_revision_log.py --case-dir outputs/case --kind merge --user "用户补充了..." --summary "已合并..." --artifacts "xxx.md,xxx.docx"
```

Use `--kind correct` for correction and `--kind rewrite` for rebuilds.

## Response Summary

For merge/supplement, include:

```markdown
## 合并摘要（留档）
```

Use 3-6 Chinese sentences covering modified sections, reason, impact on claims/prior-art conclusions, and consistency checks.

For correction, include:

```markdown
## 纠正摘要（留档）
```

Use 2-5 Chinese sentences covering modified locations, basis, and impact on claims/prior-art conclusions.

For claim strengthening, explain that the change is scope/style emphasis unless new facts were added.
