---
name: issue-author
description: バグ報告 / 機能要望の GitHub Issue を規約に沿って日本語で作成するときに使う。起票は承認後。
argument-hint: "Issue 内容（例: '記事公開日が JST でずれる'）"
context: fork
agent: sdd-harness:issue-author
background: false
---

# GitHub Issue の起票

依頼内容: $ARGUMENTS

あなた（`sdd-harness:issue-author`）のエージェント定義に書かれた必読事項・原則・進め方に従って、上記の依頼を実行してください。

- 着手前にプロジェクトの `CLAUDE.md` と `.claude/rules/`（対象領域のルール）を読み、スタック固有の制約を把握する。
- 完了したら、結果（変更 / 作成したファイル、指摘、成果物の場所、引き継ぎ事項）を日本語で簡潔に要約して返す。
