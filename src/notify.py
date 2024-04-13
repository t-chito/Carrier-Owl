import datetime

import requests
import slackweb


def send2app(text: str, slack_id: str, line_token: str) -> None:
    # slack
    if slack_id is not None:
        slack = slackweb.Slack(url=slack_id)
        slack.notify(text=text)

    # line
    if line_token is not None:
        line_notify_api = "https://notify-api.line.me/api/notify"
        headers = {"Authorization": f"Bearer {line_token}"}
        data = {"message": f"message: {text}"}
        requests.post(line_notify_api, headers=headers, data=data)


def notify(results: list, slack_id: str, line_token: str) -> None:
    # 通知
    star = "*" * 80
    today = datetime.date.today()
    n_articles = len(results)
    text = f"{star}\n \t \t {today}\tnum of articles = {n_articles}\n{star}"
    send2app(text, slack_id, line_token)
    # descending
    for result in sorted(results, reverse=True, key=lambda x: x.score):
        url = result.url
        title = result.title
        abstract = result.abstract
        word = result.words
        score = result.score

        text = (
            f"\n score: `{score}`"
            f"\n hit keywords: `{word}`"
            f"\n url: {url}"
            f"\n title:    {title}"
            f"\n abstract:"
            f"\n \t {abstract}"
            f"\n {star}"
        )

        send2app(text, slack_id, line_token)
