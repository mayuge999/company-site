# Daable Corporate Site

## プロジェクト概要
教育一般社団法人向けの信頼感と優しさを重視したコーポレートサイト。

## 主要機能
- トップページ（カルーセル、企業理念、サービス概要）
- サービス紹介（個別指導、グループ学習プログラム）
- 料金プラン（ベーシック、スタンダード、プレミアム）
- お問い合わせフォーム（自動返信機能付き）
- 採用情報（新卒、中途、インターン）
- 会社概要
- ブログ機能

## 技術スタック
- バックエンド: Python/Flask
- フロントエンド: HTML/CSS/JavaScript
- データベース: PostgreSQL
- メール配信: Flask-Mail
- フォーム処理: Flask-WTF
- スタイリング: Bootstrap 5
- アニメーション: AOS.js

## 環境構築
1. 依存パッケージのインストール
```bash
pip install -r requirements.txt
```

2. 環境変数の設定
```
FLASK_SECRET_KEY=your_secret_key
MAIL_USERNAME=your_email
MAIL_PASSWORD=your_app_password
DATABASE_URL=your_database_url
```

3. データベースの初期化
```bash
python
from app import app, db
with app.app_context():
    db.create_all()
```

4. サーバー起動
```bash
python main.py
```

## フォルダ構成
```
├── static/
│   ├── css/
│   └── js/
├── templates/
│   ├── admin/
│   ├── plans/
│   └── recruit/
├── app.py
├── forms.py
├── models.py
└── main.py
```

## API仕様
- POST /contact: お問い合わせフォーム送信
- POST /entry: 採用エントリー送信
