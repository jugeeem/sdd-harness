---
name: test-engineer
description: usecase 単体テスト（fake 注入）・リポジトリのインテグレーション・認可 / 日付境界・入力スキーマ・コンポーネントテストを書くときに使う。言語は問わない。
argument-hint: "テスト対象（例: 'CreatePost usecase' / 'src/server/...'）"
context: fork
agent: sdd-harness:test-engineer
background: false
---

# テスト作成・拡充

依頼内容: $ARGUMENTS

あなた（`sdd-harness:test-engineer`）のエージェント定義に書かれた必読事項・原則・進め方に従って、上記の依頼を実行してください。

- 着手前にプロジェクトの `CLAUDE.md` と `.claude/rules/`（対象領域のルール）を読み、スタック固有の制約を把握する。
- 完了したら、結果（変更 / 作成したファイル、指摘、成果物の場所、引き継ぎ事項）を日本語で簡潔に要約して返す。
