# ScholarManage 💰🎓

奨学金を含む収支記録Webアプリケーション「ScholarManage」

## 💡 概要

「ScholarManage」は、奨学金を含めた収入と支出を手軽に記録するだけでなく、年に一度提出義務のある「奨学金継続届」の提出をスムーズに進めることを目的としたWebアプリケーションです。収入と支出の登録・編集・削除・一覧表示 (CRUD操作) 機能や、収入と支出の登録の一覧表示機能を実装しました。

## 💻 使用技術

* **フロントエンド:** Bootstrap
* **バックエンド:** Python (Django)
* **データベース:** SQLite3
* **デプロイ:** Render

## ✨ 機能と技術的こだわり

* AbstractBaseUser, PermissionMixinを継承したカスタムユーザーモデル定義
* アカウント登録フォームにカスタムウィジェットを追加
* 抽象基底クラスを使用した他モデルに対する共通フィールドの追加
* DBに対するアクセス回数を減少させるためのクエリ処理

## 🛠️ 工夫した点

* **収入と支出のカテゴリー設計:** 「奨学金継続届」のカテゴリーと同一にすることで、
  登録内容を分かりやすくするだけでなく、「奨学金継続届」の提出をスムーズに進められるようにしました。
* **登録内容の簡略化:** 収支登録のハードルを下げるため、日付は年月のみの入力で済むようにしました。

## 🔗 アクセス

* **GitHubリポジトリ:** [https://github.com/smashblooms/ScholarManage](https://github.com/smashblooms/ScholarManage)
* **デプロイ先URL:** [https://scholarmanage.onrender.com](https://scholarmanage.onrender.com)

## 🗓️ 開発期間

2024年9月8日〜9月15日、2024年12月18日〜12月30日
