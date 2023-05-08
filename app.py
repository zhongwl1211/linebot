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

app = Flask(__name__)

line_bot_api = LineBotApi('MVFiuSEY8fXHj2FXppHMFgaHqrRyx5MXjSPmo8WjO/MhugZBC5vwZzmEH+E1WNpHElSX8VGZmpWc36iUSUfS1h79b5jLIFOWNsxXP+ZyX3W6BI/2GhFo1aeD0ZYFOBEtSflDXgLbZZo3HG7u6SgdtgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('daa61cbc35df778ea83b21e1da988fb1')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r == "抱歉,我不太明白您的意思"

    if msg == 'hi':
        r = 'hi'
    elif msg == '早安':
        r = '早安,祝您有個開心的一天'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()