"""通知関連の関数を提供するモジュール"""

import datetime

import requests
import slackweb

from .config import LINE_TOKEN, SLACK_ID
from .my_types import ArticleInfo


def send2app(text: str) -> None:
    """slack または line に通知を送る

    Parameters
    ----------
    text : str
        通知するメッセージ
    """
    # slack
    if SLACK_ID:
        slack = slackweb.Slack(url=SLACK_ID)
        slack.notify(text=text)

    # line
    if LINE_TOKEN:
        line_notify_api = "https://notify-api.line.me/api/notify"
        headers = {"Authorization": f"Bearer {LINE_TOKEN}"}
        data = {"message": f"message: {text}"}
        requests.post(line_notify_api, headers=headers, data=data)


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
    send2app(dividing_text)

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

        send2app(text)

    # 通知の終了部分
    send2app(dividing_text)
