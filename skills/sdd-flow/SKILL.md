---
name: sdd-flow
description: SDD（仕様駆動開発）の工程・成果物・エージェント分担と、成果ドキュメントを `.docs/specs/<日時>-<機能>/` へ集約する規約。プラグインの各エージェントが前提として読む背景知識。
user-invocable: false
---

# SDD の開発フローと成果物規約

このプラグイン（`sdd-harness`）は、機能開発を **要件 → 設計 → DB 設計 → 実装 → テスト → レビュー → Git** の工程に分け、各工程を専任のサブエージェントへ委譲する。

## 工程とエージェント

| 工程 | エージェント | 成果物 | ソース変更 |
|---|---|---|---|
| 要件ヒアリング（壁打ち） | `sdd-harness:requirements-interviewer` | `requirements.md` | しない |
| 要件分析（仕様化） | `sdd-harness:requirements-analyst` | `requirements.md`（追記・精緻化） | しない |
| 設計（壁打ち） | `sdd-harness:design-new` | `design.md` | しない |
| DB 設計 | `sdd-harness:db-designer` | `db-design.md` | しない |
| 実装（横断） | `sdd-harness:feature-new` | `implementation.md` | する |
| 実装（サーバ） | `sdd-harness:server-architect` | `implementation.md` | する |
| 実装（フロント） | `sdd-harness:frontend-developer` | `implementation.md` | する |
| 実装（DB / ORM） | `sdd-harness:db-engineer` | `implementation.md` | する |
| 実装（認証認可） | `sdd-harness:auth-engineer` | `implementation.md` | する |
| テスト | `sdd-harness:test-engineer` | `test-plan.md` | する（テストのみ） |
| レビュー | `sdd-harness:review-server` / `review-frontend` | 指摘（チャット） | しない |
| セキュリティ診断 | `sdd-harness:security-scan-server` / `-frontend` / `-db` | 指摘（チャット） | しない |
| Git | `sdd-harness:branch-master` / `commit-helper` / `pr-author` / `issue-author` | ブランチ / コミット / PR / Issue | git 操作のみ |
| ハーネス保守 | `sdd-harness:harness-creator` | `.claude/` 配下 | ハーネスのみ |

## プロジェクト側との契約（プラグインが前提とするもの）

プラグインは **技術スタックを知らない**。スタック固有の制約はプロジェクトが次の場所に置く。各エージェントは作業前にこれらを読む。

1. **`.claude/rules/*.md`** — 規範的な制約（MUST / MUST NOT）。frontmatter の `paths:`（glob）で適用パスを宣言すると、該当ファイルを Read / Edit / Write したときに自動で読み込まれる。`paths:` の無いルールは常時読み込まれる。
2. **`.claude/docs/*.md`** — スタックの解説（ハンドブック）。アーキテクチャ・技術選定・認証方式・フロント規約など。
3. **`CLAUDE.md`** — 品質ゲートのコマンド（lint / format / typecheck / test）、ディレクトリ構成、応答言語。
4. **`.docs/specs/`** — 本規約（下記）に従う成果ドキュメントの置き場。

> エージェントは「どの lint / typecheck コマンドを通すか」を自分で決めない。`CLAUDE.md` または rules に書かれたコマンドを使う。

## 成果ドキュメント規約（`.docs/specs/`）

- **MUST** 成果ドキュメント（要件 / 設計 / DB 設計 / 実装サマリ / テスト方針）は `.docs/specs/<YYYYMMDD-HHMMSS>-<feature-slug>/` 配下に出力する。
- **MUST** **1 機能 = 1 ディレクトリ**。後続工程は新しい日時ディレクトリを作らず、既存の同一機能ディレクトリへ追記する。
  - 出力前に `ls .docs/specs/ | grep <feature-slug>` 等で既存を探し、あれば**再利用**する。
  - 新規作成時のみ `date +%Y%m%d-%H%M%S`（`TZ` はプロジェクト設定に従う）で日時を取得する。
  - `<feature-slug>` は機能を表す kebab-case。
- **MUST** 工程別の標準ファイル名: `requirements.md` / `design.md` / `db-design.md` / `implementation.md`（既存があれば追記）/ `test-plan.md`。
- **MUST** 各 Markdown の冒頭に **ステータス / 次工程 / 関連エージェント** を記す。

```markdown
# <機能名> — <工程名>

- **ステータス**: 設計完了（実装待ち）
- **次工程**: feature-new による実装
- **関連エージェント**: design-new → feature-new → test-engineer
```

- **MUST** 実コードは従来どおりプロジェクトのソースツリーに書く。`.docs/specs/` にはドキュメントのみ置く。
- **MUST NOT** 壁打ち系（requirements-interviewer / design-new）と設計系（db-designer）がソースコード・設定・スキーマを作成・編集・削除する。
- **MUST NOT** 既存の `.docs/specs/` ディレクトリやファイルを壊す（同名工程は追記・更新）。
- 例外: ハーネス保守（harness-creator）の成果物は `.claude/` 配下に書き、本規約の対象外。

## 共通の振る舞い

- 応答・コメント・成果物・コミットメッセージは **日本語**。
- 読み取り専用エージェント（review-* / security-scan-*）はファイルを変更しない。Bash も読み取り / 静的解析に限る。
- 書き込み系エージェントは、変更後に `CLAUDE.md` が定める品質ゲートを通す。
- 自分の担当外の変更が必要になったら、自分で踏み込まず担当エージェントへの引き継ぎ事項として報告する。
