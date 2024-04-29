"""
slack への返信機能を提供する
"""

from slack_sdk import WebClient

from ..config import SLACK_BOT_TOKEN, SLACK_CHANNEL_ID
from ..my_types import SlackEventReactionAdded

client = WebClient(token=SLACK_BOT_TOKEN)


def identify_parent_ts(data: SlackEventReactionAdded) -> str:
    """親メッセージの ts (id) を特定して返す。

    Parameters
    ----------
    data : SlackEventReactionAdded
        Slack Event API のデータ

    Returns
    -------
    str
        親メッセージの ts (id)
    """
    return data["event"]["item"]["ts"]


def retrieve_parent_message(data: SlackEventReactionAdded) -> str:
    """親メッセージを取得する

    https://api.slack.com/messaging/retrieving#individual_messages

    Parameters
    ----------
    data : SlackEventReactionAdded
        Slack Event API のデータ

    Returns
    -------
    str
        親メッセージのテキスト
    """

    parent_ts = identify_parent_ts(data)

    response = client.conversations_history(
        channel=SLACK_CHANNEL_ID, latest=parent_ts, limit=1, inclusive=True
    )

    return response["messages"][0]["text"]


def reply_to_message(data: SlackEventReactionAdded, text: str) -> None:
    """Slack で特定のメッセージに返信する

    Parameters
    ----------
    data : SlackEventReactionAdded
        元のリクエストデータ
    text : str
        送るテキスト
    """

    parent_ts = identify_parent_ts(data)

    client = WebClient(token=SLACK_BOT_TOKEN)

    client.chat_postMessage(
        channel=SLACK_CHANNEL_ID,
        text=text,
        thread_ts=parent_ts,
    )
