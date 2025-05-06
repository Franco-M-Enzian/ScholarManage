# ScholarManage

奨学金を含む収支記録Webアプリケーション「ScholarManage」

## 概要

ScholarManageは、奨学金を含めた収入と支出を手軽に記録し、年に一度提出義務のある「奨学金継続届」の提出をスムーズに進めることを目的としたWebアプリです。収入と支出の登録・編集・削除・一覧表示 (CRUD操作) 機能を実装しています。[cite: 33]

## 使用技術

* **フロントエンド:** Bootstrap [cite: 32]
* **バックエンド:** Python (Django) [cite: 32]
* **データベース:** SQLite3 [cite: 32]
* **デプロイ:** Render [cite: 32]

## 機能と技術的こだわり

* AbstractBaseUser, Permission Mixinを継承したカスタムユーザーモデル定義 [cite: 33]
* アカウント登録フォームにカスタムウィジェットを追加 [cite: 33]
* 抽象基底クラスを使用した他モデルに対する共通フィールドの追加 [cite: 33]
* DBに対するアクセス回数を減少させるためのクエリ処理 [cite: 33]

## 工夫した点

* **収入と支出のカテゴリー設計:** 「奨学金継続届」のカテゴリーと同一にすることで、登録内容を分かりやすくしました。 [cite: 33]
* **登録内容の簡略化:** 日付は年月のみの入力で済むようにしました。 [cite: 33]

## アクセス

* **GitHubリポジトリ:** [https://github.com/smashblooms/ScholarManage](https://github.com/smashblooms/ScholarManage) [cite: 32]
* **デプロイ先URL:** [https://scholarmanage.onrender.com](https://scholarmanage.onrender.com) [cite: 32]

## 期間

2024年9月8日〜9月15日、2024年12月18日〜12月30日 [cite: 32]
