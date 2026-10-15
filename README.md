# sdd-harness

仕様駆動開発（SDD: Spec-Driven Development）の開発フローを Claude Code のサブエージェント群として提供するプラグインです。
**要件ヒアリング → 要件分析 → 設計 → DB 設計 → 実装 → テスト → レビュー → セキュリティ診断 → Git** の各工程を専任エージェントへ委譲し、成果ドキュメントを `.docs/specs/<日時>-<機能>/` に集約します。応答・成果物はすべて日本語です。

## 設計方針: プラグインは技術スタックを知らない

このプラグインは **工程と役割** だけを提供します。言語・フレームワーク・ORM・UI ライブラリ・品質ゲートのコマンドといった **スタック固有の制約はプロジェクト側の `.claude/rules/` に置く**前提で、各エージェントは作業前に対象領域のルールを読みます。

| 置き場所 | 内容 | 例 |
|---|---|---|
| プラグイン（本リポジトリ） | 工程エージェント・Git エージェント・汎用の背景知識（SDD フロー / クリーンアーキテクチャ原則 / テスト戦略 / Git 規約） | `agents/server-architect.md` |
| プロジェクト `.claude/rules/*.md` | MUST / MUST NOT のスタック制約。frontmatter `paths:` で適用パスを宣言 | 「domain 層で Prisma を import しない」 |
| プロジェクト `.claude/docs/*.md` | スタックの解説（ハンドブック） | 技術選定・認証方式・フロント規約 |
| プロジェクト `CLAUDE.md` | 品質ゲートのコマンド・ディレクトリ構成 | `bunx biome check --write .` |
| プロジェクト `.claude/settings.json` | 権限・環境変数（プラグインは配布できない） | `.env` 読み取り拒否 |

## 提供するもの

### エージェント（`@agent-sdd-harness:<name>`）

| 工程 | エージェント | ソース変更 |
|---|---|---|
| 要件 | `requirements-interviewer` / `requirements-analyst` | しない |
| 設計 | `design-new` / `db-designer` | しない |
| 実装 | `feature-new`（横断）/ `server-architect` / `frontend-developer` / `db-engineer` / `auth-engineer` / `test-engineer` | する |
| レビュー | `review-server` / `review-frontend` | しない（読み取り専用） |
| セキュリティ | `security-scan-server` / `security-scan-frontend` / `security-scan-db` | しない（読み取り専用） |
| Git | `branch-master` / `commit-helper` / `pr-author` / `issue-author` | git 操作のみ |
| ハーネス保守 | `harness-creator` | `.claude/` のみ |

### スキル（`/sdd-harness:<name>`）

- 各エージェントと同名のスキル（`context: fork` で同名エージェントに委譲）。`/sdd-harness:design-new コメント機能` のように引数を渡す。
- `code-review` — 差分の領域に応じて review / security-scan エージェントへ振り分ける総合レビュー。
- 背景知識（ユーザーからは呼ばない。エージェントへ preload）: `sdd-flow` / `clean-architecture` / `testing-strategy` / `git-conventions`。

### フック

- `PreToolUse`（Bash）: `git commit` 実行前に Conventional Commits 規約のリマインダーを注入する（ブロックはしない）。

## インストール

GitHub のマーケットプレイス（本リポジトリ）から:

```bash
claude plugin marketplace add jugeeem/sdd-harness
claude plugin install sdd-harness@jugeeem --scope project
```

チームで使う場合は、プロジェクトの `.claude/settings.json` にマーケットプレイスと有効化を記録しておくと、
リポジトリを信頼した時点で各メンバーにインストールが促されます:

```json
{
  "extraKnownMarketplaces": {
    "jugeeem": {
      "source": { "source": "github", "repo": "jugeeem/sdd-harness" }
    }
  },
  "enabledPlugins": {
    "sdd-harness@jugeeem": true
  }
}
```

更新は `claude plugin marketplace update jugeeem`。

## 開発

```bash
claude --plugin-dir .                 # 1 セッションだけ読み込む（編集後は /reload-plugins）
claude plugin validate --strict .     # プラグイン + マーケットプレイスの構成検証
```

リリース時は `.claude-plugin/plugin.json` の `version` を上げる。

## プロジェクト側で用意するもの（契約）

1. `.claude/rules/*.md` — スタック制約。`paths:` glob で適用範囲を宣言する（無ければ常時ロード）。
2. `.claude/docs/*.md` — スタック解説。
3. `CLAUDE.md` — 品質ゲートのコマンド、応答言語、ディレクトリ構成。
4. `.docs/specs/` — 成果ドキュメントの置き場（ディレクトリは自動作成される）。

詳細は `skills/sdd-flow/SKILL.md` を参照。
