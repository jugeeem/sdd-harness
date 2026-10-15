---
name: db-designer
description: DB のデータモデルを設計する段階（エンティティ抽出・リレーション・正規化・インデックス・制約・監査カラム）で使う。設計書は .docs/specs/<...>/db-design.md。実装は db-engineer に渡す。
argument-hint: "設計したいデータ領域（例: 'ブログ記事とタグ・カテゴリのモデル'）"
context: fork
agent: sdd-harness:db-designer
background: false
---

# DB 設計

依頼内容: $ARGUMENTS

あなた（`sdd-harness:db-designer`）のエージェント定義に書かれた必読事項・原則・進め方に従って、上記の依頼を実行してください。

- 着手前にプロジェクトの `CLAUDE.md` と `.claude/rules/`（対象領域のルール）を読み、スタック固有の制約を把握する。
- 完了したら、結果（変更 / 作成したファイル、指摘、成果物の場所、引き継ぎ事項）を日本語で簡潔に要約して返す。
