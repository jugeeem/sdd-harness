---
name: branch-master
description: 規約に沿ったブランチの作成・切り替え・整理を行うときに使う。新規作業の開始時や既定ブランチ（main）上で作業しそうなときに。
argument-hint: "作業内容と関連 Issue 番号（例: '42 ブログ一覧'）"
context: fork
agent: sdd-harness:branch-master
background: false
---

# ブランチの作成・整理

依頼内容: $ARGUMENTS

あなた（`sdd-harness:branch-master`）のエージェント定義に書かれた必読事項・原則・進め方に従って、上記の依頼を実行してください。

- 着手前にプロジェクトの `CLAUDE.md` と `.claude/rules/`（対象領域のルール）を読み、スタック固有の制約を把握する。
- 完了したら、結果（変更 / 作成したファイル、指摘、成果物の場所、引き継ぎ事項）を日本語で簡潔に要約して返す。
