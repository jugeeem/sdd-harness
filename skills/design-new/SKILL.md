---
name: design-new
description: 精緻化された要件から、クリーンアーキテクチャ 4 層 + UI の構成・データモデル・サーバ入口 / コンポーネント設計・影響範囲・実装タスク分解を設計（壁打ち）するときに使う。設計書（.docs/specs/<...>/design.md）は出力するがソースコードは変更しない。
argument-hint: "設計したい機能（例: 'コメント機能'）"
context: fork
agent: sdd-harness:design-new
background: false
---

# 新機能の設計（壁打ち）

依頼内容: $ARGUMENTS

あなた（`sdd-harness:design-new`）のエージェント定義に書かれた必読事項・原則・進め方に従って、上記の依頼を実行してください。

- 着手前にプロジェクトの `CLAUDE.md` と `.claude/rules/`（対象領域のルール）を読み、スタック固有の制約を把握する。
- 完了したら、結果（変更 / 作成したファイル、指摘、成果物の場所、引き継ぎ事項）を日本語で簡潔に要約して返す。
