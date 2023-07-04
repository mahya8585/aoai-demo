# デモ手順
- 空っぽの requirements.txt を作成する
  - requirements.txtの説明
- インターフェースの作成
  - templatesディレクトリ内にindex.htmlを作成
    ```html
        <!-- demoサイト -->
        <!-- 入力したテキストをAPIに送付する -->
        <!DOCTYPE html>
        <html lang="ja">
        <head>
            <meta charset="UTF-8">
            <title>demo</title>
        </head>
        <body>

        <form action="/chat" method="post">
            <input type="text" name="user_msg">
            <button type="submit">GO!</button>
        </form>
        <div id="response">{{ai_response}}</div>

        </body>
        </html>
    ```
- app.pyの作成
  ```python
    from flask import Flask
    from flask import request
    import flask
    app = Flask(__name__)


    @app.route('/')
    def index():
        return flask.render_template(
            'index.html',
            ai_response=''
        )
  ```
- 動作確認
  ```cli
      SET FLASK_APP=app.py
      flask run
  ```
- app.py レスポンスAPIの作成
  - チュートリアルサイトとプレイグラウンドのコード表示機能説明
  - プロンプトエンジニアリングとアプリケーション開発の違いの説明
  - APIKEY -> open ai > キーとエンドポイント
  ```python
    import os
    import openai
    import json


    @app.route('/chat', methods=['POST'])
    def chat():
        user_msg = request.form['user_msg']

        # user_msg を Azure Open AI Service に送信して、返答を取得する
        openai.api_type = 'azure'
        openai.api_base = 'https://maaya-test.openai.azure.com/'
        openai.api_version = '2023-03-15-preview'
        openai.api_key = 'd8d93xxxxxxxxxxxxxxx'

        response = openai.ChatCompletion.create(
            engine='test-maaya-35',
            messages = [{
                    "role": "system",
                    "content": "あなたは銀行の窓口で働いています。お客様からの問い合わせに対応してください。"
                }, {
                    "role": "user",
                    "content": user_msg
                }],
            temperature=0.7,
            max_tokens=800,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None)
        
        # 返答JSONの中から、choicecsの0番目のmessageを取得する
        response_msg = response['choices'][0]['message']['content']

        return flask.render_template(
            'index.html',
            ai_response=response_msg
        )
  ```
- 動作確認
  ```cli
  flask run
  ```

- API KEYの設定変更
  - なぜ変更が必要なのかセキュリティの話
```python
    openai.api_key = os.getenv('OPENAI_API_KEY')
```

- コードコミット

- Web Apps の作成
  - デプロイセンターの作成
- 「待ち時間がながいので完成品はこちらです！」
