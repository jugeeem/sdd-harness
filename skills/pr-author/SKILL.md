---
name: pr-author
description: 現在のブランチ差分から Conventional Commits 形式のタイトルと日本語 PR 説明文を作り、承認後に push と PR 作成を行うときに使う。
argument-hint: "任意: PR 変更内容の要約"
context: fork
agent: sdd-harness:pr-author
background: false
---

# Pull Request の作成

依頼内容: $ARGUMENTS

あなた（`sdd-harness:pr-author`）のエージェント定義に書かれた必読事項・原則・進め方に従って、上記の依頼を実行してください。

- 着手前にプロジェクトの `CLAUDE.md` と `.claude/rules/`（対象領域のルール）を読み、スタック固有の制約を把握する。
- 完了したら、結果（変更 / 作成したファイル、指摘、成果物の場所、引き継ぎ事項）を日本語で簡潔に要約して返す。
