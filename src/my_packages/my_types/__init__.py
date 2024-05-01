"""
型提供モジュールの初期化ファイル

SlackEventReactionAdded は

- https://api.slack.com/apis/connections/events-api#events-JSON
- https://api.slack.com/events/reaction_added

を参考にして scripts/slack_event_reaction_added.json を作成し、
それを datamodel-codegen で変換して生成した。
"""

from .my_types import ArticleInfo, Config, taxonomy
from .slack_event_reaction_added import Model as SlackEventReactionAdded
from .slack_url_verification import Model as SlackUrlVerification

SlackPostEvent = SlackEventReactionAdded | SlackUrlVerification

__all__ = [
    "ArticleInfo",
    "Config",
    "taxonomy",
    "SlackEventReactionAdded",
    "SlackEventUrlVerification",
    "SlackPostEvent",
]
