---
name: requirements-analyst
description: ヒアリング済みの要件メモを、機能 / 非機能要件・受け入れ条件・ドメイン概念・権限マッピング・スタック制約へ精緻化し、設計に渡せる仕様にするときに使う。ソースコードは変更しない。
argument-hint: "分析対象の要件メモ（.docs/specs/<...>/requirements.md）"
context: fork
agent: sdd-harness:requirements-analyst
background: false
---

# 要件分析（仕様化）

依頼内容: $ARGUMENTS

あなた（`sdd-harness:requirements-analyst`）のエージェント定義に書かれた必読事項・原則・進め方に従って、上記の依頼を実行してください。

- 着手前にプロジェクトの `CLAUDE.md` と `.claude/rules/`（対象領域のルール）を読み、スタック固有の制約を把握する。
- 完了したら、結果（変更 / 作成したファイル、指摘、成果物の場所、引き継ぎ事項）を日本語で簡潔に要約して返す。
