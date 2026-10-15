---
name: feature-new
description: 設計（design.md）に基づき新機能を domain → application → infrastructure → presentation → frontend → テスト の順で一気通貫に実装するときに使う。
argument-hint: "実装したい機能（できれば design-new の設計付き）"
context: fork
agent: sdd-harness:feature-new
background: false
---

# 新機能のフルスタック実装

依頼内容: $ARGUMENTS

あなた（`sdd-harness:feature-new`）のエージェント定義に書かれた必読事項・原則・進め方に従って、上記の依頼を実行してください。

- 着手前にプロジェクトの `CLAUDE.md` と `.claude/rules/`（対象領域のルール）を読み、スタック固有の制約を把握する。
- 完了したら、結果（変更 / 作成したファイル、指摘、成果物の場所、引き継ぎ事項）を日本語で簡潔に要約して返す。
