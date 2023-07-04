# flask を使って index.htmlを表示する API
from flask import Flask, request
import flask
import os
import openai
app=Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return flask.render_template(
        "index.html",
        ai_response=""
        )

@app.route("/chat", methods=["POST"])
def chat():
    # リクエストを受け取る
    user_msg = request.form["user_msg"]

    # user_msgをAOAIに送付する
    openai.api_type = "azure"
    openai.api_base = "https://maaya-test.openai.azure.com/"
    openai.api_version = "2023-03-15-preview"
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.ChatCompletion.create(
        engine="test-maaya-35",
        messages = [{
                  "role": "system",
                  "content": "あなたは銀行の窓口で働いています。お客様からの問い合わせに対応してください。"
              }, {
                  "role": "user",
                  "content": user_msg
              }],
        temperature=0.65,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None)
    
    # responseを返す
    response_msg = response["choices"][0]["message"]["content"]

    return flask.render_template(
        "index.html",
        ai_response=response_msg
        )