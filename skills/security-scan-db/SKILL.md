---
name: security-scan-db
description: DB / ORM 層のセキュリティ（インジェクション・最小権限・ロール権限境界・PII 保護・マイグレーション安全性）を診断するときに使う。読み取り専用。
argument-hint: "任意: 診断対象や観点"
context: fork
agent: sdd-harness:security-scan-db
background: false
---

# DB / ORM のセキュリティ診断

依頼内容: $ARGUMENTS

あなた（`sdd-harness:security-scan-db`）のエージェント定義に書かれた必読事項・原則・進め方に従って、上記の依頼を実行してください。

- 着手前にプロジェクトの `CLAUDE.md` と `.claude/rules/`（対象領域のルール）を読み、スタック固有の制約を把握する。
- 完了したら、結果（変更 / 作成したファイル、指摘、成果物の場所、引き継ぎ事項）を日本語で簡潔に要約して返す。
