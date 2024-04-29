from ..my_types import SlackEventReactionAdded
from .handle_text import extract_url_from_message_text
from .notify import notify
from .reply import reply_to_message, retrieve_parent_message


def extract_url_from_message(data: SlackEventReactionAdded) -> str:
    """メッセージから URL を取得する

    Parameters
    ----------
    data : SlackEventReactionAdded
        Slack Event API のデータ

    Returns
    -------
    str
        URL
    """

    parent_message = retrieve_parent_message(data)
    return extract_url_from_message_text(parent_message)


__all__ = ["extract_url_from_message", "notify", "reply_to_message"]
