"""設定ファイル"""

import os
from os.path import dirname, join

from dotenv import dotenv_values

from .my_types import Config

"""
検索、フィルタ設定
"""

config: Config = {
    # arxivの学問領域の指定
    "subject": "cat:cs.*",
    # 検索キーワードと重み
    "keywords": {
        "LLM": 1,
    },
    # 通知の閾値
    "score_threshold": 1,
}

SUBJECT = config["subject"]
KEYWORDS = config["keywords"]
SCORE_THRESHOLD = config["score_threshold"]

"""
環境変数の設定
"""

# local で実行する場合の環境変数の読み込み
dotenv_path = join(dirname(__file__), "..", ".env.local")
env_values = dotenv_values(dotenv_path)

SLACK_ID: str | None = os.getenv("SLACK_ID") or env_values["SLACK_ID"]
LINE_TOKEN: str | None = os.getenv("LINE_TOKEN") or env_values["LINE_TOKEN"]
DEEPL_AUTH_KEY: str | None = os.getenv("DEEPL_AUTH_KEY") or env_values["DEEPL_AUTH_KEY"]
