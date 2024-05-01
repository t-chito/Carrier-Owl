"""slack への通知機能を提供するモジュール"""

from slack_sdk.webhook import WebhookClient

from ..config import SLACK_ID
from ..my_types import ArticleInfo
from .handle_text import create_dividing_text, create_message_text

# 通知先のチャンネルを指定
webhook = WebhookClient(url=SLACK_ID)


def send_text_to_slack(text: str) -> None:
    """slack にテキストを送る

    Parameters
    ----------
    text : str
        送信するメッセージ
    """
    if SLACK_ID:
        webhook.send(text=text)


def notify(articles: list[ArticleInfo]) -> None:
    """論文情報を通知する

    Parameters
    ----------
    articles : list[ArticleInfo]
        通知する論文情報
    """

    num_of_articles = len(articles)
    dividing_text = create_dividing_text(num_of_articles)

    # 通知の開始部分
    send_text_to_slack(dividing_text)

    # 結果を通知
    for article in articles:
        text = create_message_text(article)
        send_text_to_slack(text)

    # 通知の終了部分
    send_text_to_slack(dividing_text)
