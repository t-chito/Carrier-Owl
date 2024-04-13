"""通知関連の関数を提供するモジュール"""

import datetime

import requests
import slackweb

from .config import LINE_TOKEN, SLACK_ID
from .my_types import Result


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


def notify(results: list[Result]) -> None:
    """結果を整形して通知する

    Parameters
    ----------
    results : list[Result]
        検索結果
    """
    # 通知の開始部分
    star = "*" * 80
    today = datetime.date.today()
    n_articles = len(results)
    text = f"{star}\n \t \t {today}\tnum of articles = {n_articles}\n{star}"
    send2app(text)

    # 結果を descending order で通知
    for result in sorted(results, reverse=True, key=lambda x: x.score):
        text = (
            f"\n score: `{result.score}`"
            f"\n hit keywords: `{result.words}`"
            f"\n url: {result.url}"
            f"\n title:    {result.title}"
            f"\n abstract:"
            f"\n \t {result.abstract}"
            f"\n {star}"
        )

        send2app(text)
