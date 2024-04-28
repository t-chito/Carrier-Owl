"""slack への通知機能を提供するモジュール"""

import datetime

from slack_sdk.webhook import WebhookClient

from .config import SLACK_ID
from .my_types import ArticleInfo

# 通知先のチャンネルを指定
webhook = WebhookClient(url=SLACK_ID)


def send_to_slack(text: str) -> None:
    """slack に通知を送る

    Parameters
    ----------
    text : str
        通知するメッセージ
    """
    if SLACK_ID:
        webhook.send(text=text)


divider = "-" * 80


def create_dividing_text(num_of_articles: int) -> str:
    """通知の開始・終了部分のテキストを作成する

    Parameters
    ----------
    num_of_articles : int
        論文の数

    Returns
    -------
    str
        通知の開始部分のテキスト
    """
    today = datetime.date.today()
    text = f"{today} : num of articles = {num_of_articles}"
    return f"{divider}\n" f"{text}" f"\n{divider}"


def notify(articles: list[ArticleInfo]) -> None:
    """結果を整形して通知する

    Parameters
    ----------
    articles : list[ArticleInfo]
        通知内容
    """

    num_of_articles = len(articles)
    dividing_text = create_dividing_text(num_of_articles)

    # 通知の開始部分
    send_to_slack(dividing_text)

    # 結果を通知
    for article in articles:
        text = (
            f"\n タイトル (原文): *{article.title_original}*"
            f"\n タイトル (翻訳): *{article.title_translated}*"
            f"\n keywords: `{article.words}`"
            f"\n subjects: `{article.subjects}`"
            f"\n URL: {article.url}"
            f"\n {divider}"
        )

        send_to_slack(text)

    # 通知の終了部分
    send_to_slack(dividing_text)
