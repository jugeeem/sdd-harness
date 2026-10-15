---
name: db-engineer
description: ORM スキーマ定義の変更・マイグレーション・クライアント生成・モデル↔エンティティ mapper・リポジトリ実装（ORM 部分）を行うときに使う。
argument-hint: "DB 変更内容（例: 'Post に tags リレーションを追加'）"
context: fork
agent: sdd-harness:db-engineer
background: false
---

# DB / ORM 実装

依頼内容: $ARGUMENTS

あなた（`sdd-harness:db-engineer`）のエージェント定義に書かれた必読事項・原則・進め方に従って、上記の依頼を実行してください。

- 着手前にプロジェクトの `CLAUDE.md` と `.claude/rules/`（対象領域のルール）を読み、スタック固有の制約を把握する。
- 完了したら、結果（変更 / 作成したファイル、指摘、成果物の場所、引き継ぎ事項）を日本語で簡潔に要約して返す。
