---
name: code-review
description: 変更コード（または指定ファイル）を、クリーンアーキテクチャ・プロジェクト規約・正確性・セキュリティの観点で総合レビューする。差分の領域（サーバ / フロント / DB）に応じて review-server / review-frontend / security-scan-* へ振り分け、結果を統合して返す。
argument-hint: "任意: 重視する観点やファイル（例: '依存方向' / 'src/server' / '認可'）"
---

# 総合コードレビュー

対象: $ARGUMENTS（未指定なら `git status` / `git diff` で現在の変更点を把握する）

## 進め方

1. 変更ファイルを領域に分類する: サーバ 4 層 / フロントエンド / DB スキーマ・マイグレーション / その他。
2. 領域ごとに該当する読み取り専用エージェントへ **並列で**委譲する（Agent ツール、`subagent_type` は次のとおり）:
   - サーバ → `sdd-harness:review-server`、認可・入力検証・秘密情報が絡むなら `sdd-harness:security-scan-server` も。
   - フロントエンド → `sdd-harness:review-frontend`、ユーザー入力描画・外部リンク・環境変数が絡むなら `sdd-harness:security-scan-frontend` も。
   - DB スキーマ / リポジトリ → `sdd-harness:security-scan-db`。
   - 委譲時は、対象ファイル一覧とユーザーが重視する観点を渡す。
3. 返ってきた指摘を統合し、重複を除き、重大度順に並べる。

## 出力形式

指摘ごとに:
- **場所**: ファイル + 行番号
- **重大度**: Critical / Major / Minor / 提案
- **内容**: 問題と影響
- **推奨対応**: 具体的な修正方針

問題がなければ、規約準拠を確認した旨を簡潔にまとめる。日本語で。コードは変更しない。
