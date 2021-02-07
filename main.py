# -*- config:utf-8 -*-
from flask import Flask, request, abort
 
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os
import random
 
app = Flask(__name__)
 
# Access Token set on LINE Developers
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]
 
line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)
 
 
# For Webhook from Line
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
 
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError as e:
        print(str(e))
        abort(400)
    return 'OK'
 
# Reply the message 
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event)

    if random.choice(range(10)) == 1:
        line_bot_api.reply_message(
            event.reply_token,
            #TextSendMessage(text=event.message.text))
            TextSendMessage(text=nozmon_message()))

def nozmon_message():
    return random.choice(['なんだよ',
                          'うっせーよ',
                          '寿司でも取って帰らせろ！',
                          '鸛鵲楼に登る！',
                          'やめてぇヤツはやめちまえよ！',
                          '留年してそうなヤツはだいたい友達',
                          '単位なら置きっぱなしてきた厚木に',
                          'ちょん切っちまうぞ！',
                          'ウイイレやろうよ',
                          'マダァ？',
                          'はやくぅ'])
 
if __name__ == "__main__":
    #    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
