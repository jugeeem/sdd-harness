---
name: harness-creator
description: プロジェクトの .claude/rules（paths 付きのスタック制約）・.claude/docs・固有エージェント / スキル・CLAUDE.md を追加・修正するとき、または sdd-harness プラグイン本体を改修するときに使う。ハーネス整備のメタ作業。
argument-hint: "作りたい / 直したいルール・エージェント・ドキュメント"
context: fork
agent: sdd-harness:harness-creator
background: false
---

# ハーネス（ルール / エージェント）の作成・更新

依頼内容: $ARGUMENTS

あなた（`sdd-harness:harness-creator`）のエージェント定義に書かれた必読事項・原則・進め方に従って、上記の依頼を実行してください。

- 着手前にプロジェクトの `CLAUDE.md` と `.claude/rules/`（対象領域のルール）を読み、スタック固有の制約を把握する。
- 完了したら、結果（変更 / 作成したファイル、指摘、成果物の場所、引き継ぎ事項）を日本語で簡潔に要約して返す。
