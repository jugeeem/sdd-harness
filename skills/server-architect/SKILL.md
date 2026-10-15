---
name: server-architect
description: サーバサイド 4 層（domain / application / infrastructure / presentation）の実装・修正を行うときに使う。entity・値オブジェクト・usecase・サーバ入口（procedure / router）・リポジトリ実装・DI 配線が対象。言語は問わない。
argument-hint: "実装したいサーバ処理（例: '記事を公開する usecase と procedure'）"
context: fork
agent: sdd-harness:server-architect
background: false
---

# サーバサイド実装

依頼内容: $ARGUMENTS

あなた（`sdd-harness:server-architect`）のエージェント定義に書かれた必読事項・原則・進め方に従って、上記の依頼を実行してください。

- 着手前にプロジェクトの `CLAUDE.md` と `.claude/rules/`（対象領域のルール）を読み、スタック固有の制約を把握する。
- 完了したら、結果（変更 / 作成したファイル、指摘、成果物の場所、引き継ぎ事項）を日本語で簡潔に要約して返す。
