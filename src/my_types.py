"""
型定義を提供するモジュール
"""

from dataclasses import dataclass
from typing import TypedDict


@dataclass
class Result:
    url: str
    title: str
    abstract: str
    words: list[str]
    score: float = 0.0


# see https://note.nkmk.me/python-arxiv-api-download-rss/


class Article(TypedDict):
    arxiv_url: str
    title: str
    summary: str


Keywords = dict[str, int]


class Config(TypedDict):
    subject: str
    keywords: Keywords
    score_threshold: int
