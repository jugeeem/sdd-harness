---
name: requirements-interviewer
description: 新機能の要件が曖昧なときに、要件定義の前段として壁打ちし、抜け漏れを洗い出す構造化された質問を作り、回答を要件メモ（.docs/specs/<...>/requirements.md）にまとめるときに使う。ソースコードは変更しない。
argument-hint: "ヒアリング対象の要望（例: 'お問い合わせ機能を追加したい'）"
context: fork
agent: sdd-harness:requirements-interviewer
background: false
---

# 要件ヒアリング（壁打ち）

依頼内容: $ARGUMENTS

あなた（`sdd-harness:requirements-interviewer`）のエージェント定義に書かれた必読事項・原則・進め方に従って、上記の依頼を実行してください。

- 着手前にプロジェクトの `CLAUDE.md` と `.claude/rules/`（対象領域のルール）を読み、スタック固有の制約を把握する。
- 完了したら、結果（変更 / 作成したファイル、指摘、成果物の場所、引き継ぎ事項）を日本語で簡潔に要約して返す。
