---
name: review-server
description: サーバサイド（4 層）の変更を、クリーンアーキテクチャ準拠・正確性・規約の観点でレビューするときに使う。読み取り専用。
argument-hint: "任意: レビュー対象や観点（例: 'src/server' / '依存方向'）"
context: fork
agent: sdd-harness:review-server
background: false
---

# サーバコードのレビュー

依頼内容: $ARGUMENTS

あなた（`sdd-harness:review-server`）のエージェント定義に書かれた必読事項・原則・進め方に従って、上記の依頼を実行してください。

- 着手前にプロジェクトの `CLAUDE.md` と `.claude/rules/`（対象領域のルール）を読み、スタック固有の制約を把握する。
- 完了したら、結果（変更 / 作成したファイル、指摘、成果物の場所、引き継ぎ事項）を日本語で簡潔に要約して返す。
