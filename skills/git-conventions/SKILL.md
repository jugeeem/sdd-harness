---
name: git-conventions
description: GitHub Flow のブランチ戦略・Conventional Commits（日本語）・PR / Issue の書式・AI ツール痕跡の禁止など Git 運用規約。Git 系エージェント（branch-master / commit-helper / pr-author / issue-author）が前提として読む。
user-invocable: false
---

# Git ワークフロー規約

> プロジェクトの `.claude/rules/git.md` があればそちらを優先する。本スキルは既定の規約。

## ブランチ戦略（GitHub Flow）

- `main` は常にデプロイ可能に保つ。作業は専用ブランチで行い PR 経由でマージする。
- **MUST NOT** `main` へ直接 push する。
- ブランチ名: `<type>/<issue-number>-<kebab-case-description>`（type: `feature` / `fix` / `hotfix` / `chore` / `docs` / `ci` / `release`）。例: `feature/42-add-blog-list`。
- 関連 Issue が無い場合は Issue を先に起票するか、ユーザーの了解を得て番号を省く。

## コミットメッセージ（Conventional Commits）

```
<type>(<scope>): <subject>

[optional body]

[optional footer]
```

| type | 用途 |
|---|---|
| `feat` | 新機能 |
| `fix` | バグ修正 |
| `docs` | ドキュメントのみ |
| `style` | 整形等（意味に影響しない） |
| `refactor` | リファクタ |
| `test` | テスト |
| `chore` | 補助ツール・依存更新 |
| `ci` | CI 設定 |
| `perf` | パフォーマンス |
| `revert` | リバート |

- scope（任意）はプロジェクトの層・領域名（例: `web` / `domain` / `usecase` / `infra` / `presentation` / `auth` / `ui`）。
- subject は **命令形・日本語・72 文字以内・末尾ピリオドなし**。
- Breaking Change は footer に `BREAKING CHANGE: ...`（または `<type>!:`）。
- 関連 Issue は footer に `Closes #<n>` / `Refs #<n>`。

## PR

- タイトルは `<type>(<scope>): <subject>` 形式（スクワッシュマージで履歴になる）。
- 本文は **概要 / 関連 Issue / 変更内容 / 動作確認** を日本語で書く。
- レビュアーを 1 名以上アサインする。

## Issue

- バグ: 概要 / 再現手順 / 期待 / 実際 / 環境 / 補足。
- 機能要望: 背景・課題 / 提案 / 代替案 / 受け入れ条件 / 補足。
- タイトルに `fix:` / `feat:` プレフィックス、ラベルは `bug` / `enhancement` + `priority: high|medium|low` を提案する。

## エージェント共通の制約

- **MUST** コミット / push / PR 作成 / Issue 起票は **ユーザーが明示的に依頼したときのみ**実行する。
- **MUST** `main` 上で作業を始めそうな場合はまずブランチを切る。
- **MUST NOT** コミット / PR / Issue に Claude・Claude Code・AI などのツール痕跡を残す（`Co-Authored-By` トレーラ・`Generated with Claude Code` フッター・🤖 絵文字等を一切付与しない）。
- **MUST** 秘密情報（`.env`・トークン・鍵）がステージされていないか確認し、あれば中止して警告する。
