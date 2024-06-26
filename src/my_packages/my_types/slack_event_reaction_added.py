# generated by datamodel-codegen:
#   filename:  slack_event_reaction_added.json
#   timestamp: 2024-04-28T11:43:35+00:00

from __future__ import annotations

from typing import List

from typing_extensions import TypedDict


class Item(TypedDict):
    type: str
    channel: str
    ts: str


class Event(TypedDict):
    type: str
    user: str
    reaction: str
    item_user: str
    item: Item
    event_ts: str


class Authorization(TypedDict):
    enterprise_id: str
    team_id: str
    user_id: str
    is_bot: bool
    is_enterprise_install: bool


class Model(TypedDict):
    type: str
    token: str
    team_id: str
    api_app_id: str
    event: Event
    event_context: str
    event_id: str
    event_time: int
    authorizations: List[Authorization]
    is_ext_shared_channel: bool
    context_team_id: str
    context_enterprise_id: None
