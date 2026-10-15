---
name: commit-helper
description: 変更を分析し Conventional Commits 規約の日本語メッセージでローカルにコミットするときに使う。ユーザーが明示的にコミットを依頼したときのみ。push・PR はしない。
argument-hint: "任意: コミット意図の補足"
context: fork
agent: sdd-harness:commit-helper
background: false
---

# Conventional Commits でコミット

依頼内容: $ARGUMENTS

あなた（`sdd-harness:commit-helper`）のエージェント定義に書かれた必読事項・原則・進め方に従って、上記の依頼を実行してください。

- 着手前にプロジェクトの `CLAUDE.md` と `.claude/rules/`（対象領域のルール）を読み、スタック固有の制約を把握する。
- 完了したら、結果（変更 / 作成したファイル、指摘、成果物の場所、引き継ぎ事項）を日本語で簡潔に要約して返す。
