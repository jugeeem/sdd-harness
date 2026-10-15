---
name: auth-engineer
description: 外部 IdP 連携の認証や、ロールベース認可（middleware・AuthService・ロール解決・認可境界）を実装・修正するときに使う。
argument-hint: "認証認可の作業（例: '管理者専用の入口に認可 middleware を追加'）"
context: fork
agent: sdd-harness:auth-engineer
background: false
---

# 認証認可の実装

依頼内容: $ARGUMENTS

あなた（`sdd-harness:auth-engineer`）のエージェント定義に書かれた必読事項・原則・進め方に従って、上記の依頼を実行してください。

- 着手前にプロジェクトの `CLAUDE.md` と `.claude/rules/`（対象領域のルール）を読み、スタック固有の制約を把握する。
- 完了したら、結果（変更 / 作成したファイル、指摘、成果物の場所、引き継ぎ事項）を日本語で簡潔に要約して返す。
