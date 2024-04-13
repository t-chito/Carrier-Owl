"""
型定義を提供するモジュール
"""

from dataclasses import dataclass
from typing import TypedDict


@dataclass
class Result:
    url: str
    title_translated: str
    title_original: str
    words: list[str]


# see https://note.nkmk.me/python-arxiv-api-download-rss/


class Article(TypedDict):
    arxiv_url: str
    title: str
    summary: str


class Config(TypedDict):
    subject: str
    keywords: list[str]
