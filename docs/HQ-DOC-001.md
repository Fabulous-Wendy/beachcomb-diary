# HQ-DOC-001 · 文件交付、归档与任务闭环管理规范

- **Project:** Beachcomb Diary — 赶海日记 Game Studio
- **Authority:** 00 · Project HQ / HQ-DEC-009
- **Version:** v1.1
- **Status:** APPROVED — 项目内执行规范
- **Effective date:** 2026-10-10
- **Scope:** 00 · Project HQ、01 · Game Design、02 · Art & UI、03 · Development、04 · QA & Release
- **Canonical path:** `docs/HQ-DOC-001.md`
- **Change control:** 由 00 · Project HQ 审核版本变更；新版本需说明替代版本、有效日期与差异。
- **Distribution:** 各工作区按照项目级说明引用此规范；独立聊天之间的任务结论不能假定会自动同步。

## 一、文件交付与归档（沿用原 HQ-DOC-001 第 1—8 条）

1. 日常进度、审查结论和 Handoff Summary，优先直接在对话内提交，不自动生成重复的 Markdown、PDF 或 ZIP。
2. 只有正式验收成果、可复用设计母版、完整 QA 交付包及重要版本，才需要生成独立文件。
3. 每份正式交付必须标注 Task ID、版本、状态、来源和对应的 GitHub Commit（如适用）。
4. 工作区提交新版本时，须说明替代哪个旧版本，并区分 DRAFT、APPROVED、ARCHIVED。
5. 正式成果应存入指定项目资料库，并在 Project HQ 维护文件索引。
6. 不得仅凭聊天下载链接视为长期归档完成。
7. 临时交接文件不得要求用户反复下载；确需跨工作区传递文件时，应说明原因并尽量复用已有归档。
8. 未经 HQ 批准，不修改正式 GitHub 分支或覆盖已验收资产。

## 二、任务闭环与 Final Summary（v1.1 新增）

9. **每份 HQ 下发的跨工作区任务指令必须包含明确的「Final Summary 回传 HQ」要求**；不能只布置任务而不说明怎样结案。
10. 工作区在任务 **COMPLETE、PARTIAL、BLOCKED 或 HOLD** 时，必须在该工作区对话中主动给出一份简短、可直接复制回 `00 · Project HQ` 的 **Final Summary**。它默认直接写在聊天中，**不另行生成 MD / PDF / ZIP**。
11. Final Summary 至少包含：
    - Task ID / Parent / 基线版本或 GitHub Commit（如适用）；
    - 最终状态（COMPLETE / PARTIAL / BLOCKED / HOLD）及已做、未做事项；
    - 主要交付物及其位置、必要哈希或链接；
    - 测试或审查的客观证据；区分自检与独立 QA；
    - 阻塞、风险、替代旧版本情况及下一步；
    - 需要 HQ 作出的具体决定；
    - 文件下载标识：`📥 必须保存` 或 `无需下载`（并解释原因）。
12. **任务关闭条件：** HQ 收到并审查 Final Summary 后，明确标记 `ACCEPTED`、`REVISE` 或 `HOLD`。工作区自行声明完成不等于 HQ 已验收，CI PASS 不等于游戏 G0 PASS。
13. 工作区对话之间不应假设自动互通。**需要用户协助传递时，只请求用户复制一份 Final Summary 回到 HQ**；不要求转发完整聊天、重复 ZIP 或多份 Handoff 文件。尚未回传的任务在 HQ 视为 `AWAITING FINAL SUMMARY`，不得假定已完成。

## 三、面向用户的重点提示

- **🔴 需要你决定**：必须由用户确认的美术、范围、预算或放行决定。
- **📥 必须保存**：尚未完成可信归档、但有必要长期保留的正式文件；明确名称、保存位置和原因。
- **✅ 已完成**：附可复核依据的已完成动作，不代替完整验收。
- **⏳ 等待／阻塞**：说明阻塞项和责任工作区。
- **无需下载**：默认用于日常讨论、草稿、交接摘要与可在正式资料库稳定访问的文件。

所有工作区尽量简短，优先报告结论、下一步和是否需要用户操作。避免连续生成同名文件并留下 `(1)`、`(2)` 等不明版本。

## 四、存储与变更边界

- GitHub：源码、正式文本规范、文件清单及技术版本证据；所有分支与 Commit 可追溯。
- 设计工具或获批资料库：高分辨率美术母版、独立透明图层、可编辑设计文件；正式归档完成前不可仅依赖聊天附件链接。
- QA 完整离线包：若独立 QA 需在无 GitHub 网络的环境测试，可作为正式测试证据包保存一次，不得以纯摘要替代。
- 正式 `main`、GitHub Pages、AppDeploy 或资源批量替换，仍遵循现有 HQ 发布授权；本规范的归档行为不等于游戏发布许可。
- 不将账号凭据、密钥、隐私数据或无授权文件上传到公开仓库。

## 五、标准任务结案格式（在聊天内）

```text
Final Summary → 00 · Project HQ
Task ID:
Parent / Commit:
Status: COMPLETE | PARTIAL | BLOCKED | HOLD
Completed:
Not completed / Risks:
Evidence / Deliverables:
Replacement or version changes:
HQ Decision Requested:
Download: 📥 必须保存（原因） | 无需下载
```

**Version notes:** v1.1 将既有 8 条文件规则保留不变，新增跨工作区 Final Summary 回传、HQ 结案门槛与用户重点提示。此规范生效不表示任何尚未完成的 G0、UI 或 QA 工作已获得验收。
