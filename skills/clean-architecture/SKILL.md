---
name: clean-architecture
description: 4 層クリーンアーキテクチャ（domain / application / infrastructure / presentation）の依存方向・層ごとの責務・DI・Clock port・エラーハンドリングの原則。言語 / フレームワーク非依存の共通基準で、設計・実装・レビュー系エージェントが前提として読む。
user-invocable: false
---

# クリーンアーキテクチャの原則（スタック非依存）

> この原則は言語 / フレームワークに依存しない。具体的なライブラリ名・ディレクトリ・禁止 import はプロジェクトの `.claude/rules/` と `.claude/docs/` が定める。本スキルの原則とプロジェクトの rules が食い違う場合は **rules を優先**する。

## 4 層と依存方向

```
presentation  ──→  application (usecase)  ──→  domain
      │                     │                    ▲
      └──────→ infrastructure ───────────────────┘
               (domain / application の interface を実装)
```

| 層 | 責務 | 依存してよい対象 |
|---|---|---|
| **domain** | エンティティ、値オブジェクト、ドメインサービス、リポジトリ **interface**、ドメインエラー | **何にも依存しない**（純粋な言語機能のみ） |
| **application** | ユースケース（interactor）、入出力 DTO、外部能力の **port interface**（Clock / AuthService / Logger 等） | domain のみ |
| **infrastructure** | リポジトリ実装、外部サービスクライアント、Clock 実装、**DI コンポジションルート** | domain / application（interface を実装するため） |
| **presentation** | サーバの入口（RPC procedure / HTTP router 等）、入出力スキーマ、認証 / 認可 middleware、エラーマッピング | application（usecase）。infrastructure は DI 経由でのみ受け取る |

## 依存性のルール

1. **依存は常に内向き**。逆向きの import は違反。
2. domain は他のどの層・どのライブラリにも依存しない。ORM / フレームワーク / RPC / UI ライブラリを domain に import した時点で違反。
3. application は具象を知らない。必要な外部能力は **port interface** として application 内に定義し、infrastructure が実装する。
4. presentation はビジネスロジックを書かない。**入力検証 → usecase 呼び出し → 出力整形** のみ。
5. 層境界をまたぐデータは **DTO / プレーンオブジェクト**。ORM のモデル型を application / presentation / UI に漏らさない（infrastructure の mapper で変換）。

## DI / コンポジションルート

- 具象クラスの生成（`new` 相当）は **infrastructure の DI モジュール内だけ**で行う。usecase や presentation で ORM クライアント等を直接生成しない。
- presentation は DI から組み立て済みの usecase を受け取って呼ぶ。
- テストでは fake リポジトリ / port を注入して usecase を単体検証できる構成にする。

## 時刻

- 「現在時刻」は **`Clock` port 経由**で取得する。domain / application で `new Date()` / `datetime.now()` 相当を直接呼ばない。
- 永続化は UTC、表示 / 入力境界で基準タイムゾーンへ変換する（基準タイムゾーンはプロジェクトの rules が定める）。

## エラーハンドリング

- domain / application は **ドメインエラー**（`DomainError` 系）で失敗を表現する。HTTP ステータス / RPC エラーを知らない。
- presentation でドメインエラー → プロトコルのエラーへ **一元的に**マッピングする（マッピング表を 1 箇所に置く）。

## 認可

- 認可判定は presentation の middleware に集約する（`requireAuth` / `requireRole(...)`）。
- usecase 内に「このユーザーは admin か？」を散らさない。必要なら `actor` を usecase に渡し、ドメインの認可ルールとして表現する。
- 書き込み系の入口は **必ずサーバ側でロールを再検証**する。UI の出し分けに依存しない。

## 新規ユースケースの追加手順

1. domain にエンティティ / 値オブジェクト / リポジトリ interface / ドメインエラー（不足分）を追加。
2. application に usecase（`execute(input) -> output`）と入出力 DTO、必要な port を追加。
3. infrastructure にリポジトリ / port の実装を追加し、DI に配線。
4. presentation に入出力スキーマと入口（procedure / router）を追加し、登録。
5. usecase の単体テスト（fake 注入）を書く。

## レビューで弾く違反

- domain / application から ORM・フレームワーク・RPC・UI ライブラリを import。
- presentation に条件分岐の塊や永続化判断。
- ORM モデル型を usecase の戻り値や UI に直接渡す。
- usecase / domain で現在時刻を直接取得。
- リポジトリ実装を domain / application に置く。
- DI 以外の場所で具象を生成。
