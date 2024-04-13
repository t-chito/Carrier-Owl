"""
型定義を提供するモジュール
"""

from dataclasses import dataclass


@dataclass
class Result:
    url: str
    title: str
    abstract: str
    words: list
    score: float = 0.0
