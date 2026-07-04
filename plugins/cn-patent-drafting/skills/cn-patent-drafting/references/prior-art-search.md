# Prior-Art Search

## When To Search

Search before drafting full claims/specification when the user asks for 查新, novelty, prior-art comparison, claim drafting, authorization risk, or a complete Chinese patent package. Search can be skipped only when the user explicitly says to draft from provided materials without查新; mark novelty statements as provisional.

## Search Sources

Use current public sources and verify each cited item before writing it into a deliverable.

- China-focused patent search: 国家知识产权局中国专利公布公告系统 / CNIPA public patent databases where accessible.
- Stable patent pages: Google Patents, especially for CN publication numbers and machine-readable abstracts.
- Academic search: Google Scholar, Crossref, publisher pages, arXiv, PubMed, or domain-specific databases when relevant.
- Existing user-provided references: open and verify bibliographic details and relation to the invention.

Do not fabricate patent numbers, applicants, titles, dates, abstracts, or URLs. If a source cannot be opened or verified, label it "待复核" and do not rely on it as decisive prior art.

## Query Construction

Before searching, derive 2-8 high-signal search units from the invention:

- professional terms,
- noun phrases,
- method/action phrases,
- key components,
- application scenario plus core mechanism,
- known alternative names.

Avoid using a full Chinese sentence as the only query. Avoid standalone generic words such as 系统, 方法, 模型, 平台, 检索, 优化 unless combined with technical context.

## Search Table

Maintain an internal table with:

| Field | Requirement |
|---|---|
| Source | CNIPA, Google Patents, Scholar, DOI, publisher, etc. |
| Query | Exact query or keywords used |
| Publication/citation | Patent publication number or paper citation |
| Title | Verified title |
| Applicant/assignee/authors | Verified party if available |
| URL | Public URL opened and verified |
| Abstract/core teaching | Digest in your own words; do not paste long abstracts |
| Relevance | Highly relevant, partially relevant, background only |
| Limitation | What the reference does not teach compared with the invention |
| Impact | Which claim/disclosure section it affects |

## Writing Prior Art Into Patent Materials

For 技术交底书 or 说明书 background sections:

- Write an attorney-facing "检索说明" with public database names and representative keywords.
- Do not mention internal tools, browser automation, Codex, WebSearch, or failed search attempts inside the patent document.
- For each closest reference, include a verified URL in notes or a table if the user's template permits.
- Summarize technical solution, scenario, and limitation in your own words.
- End with the essential difference: what the invention combines, changes, constrains, or technically improves.

## If Search Is Blocked

If network/database access is unavailable, continue only if useful and clearly state in the response:

- which searches were not completed,
- which claims or novelty statements are provisional,
- what the user or attorney should verify manually.

Do not hide search limitations inside the draft.
