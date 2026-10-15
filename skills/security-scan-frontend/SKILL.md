---
name: security-scan-frontend
description: フロントエンドの脆弱性（XSS・秘密情報露出・CSRF・認可 UI 依存・安全でない外部連携）を診断するときに使う。読み取り専用。
argument-hint: "任意: 診断対象や観点"
context: fork
agent: sdd-harness:security-scan-frontend
background: false
---

# フロントのセキュリティ診断

依頼内容: $ARGUMENTS

あなた（`sdd-harness:security-scan-frontend`）のエージェント定義に書かれた必読事項・原則・進め方に従って、上記の依頼を実行してください。

- 着手前にプロジェクトの `CLAUDE.md` と `.claude/rules/`（対象領域のルール）を読み、スタック固有の制約を把握する。
- 完了したら、結果（変更 / 作成したファイル、指摘、成果物の場所、引き継ぎ事項）を日本語で簡潔に要約して返す。
