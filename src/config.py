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
    "subject": "cs.*",
    # abstract に含まれるべきワード
    "keywords": ["LLM"],
}

SUBJECT = config["subject"]
KEYWORDS = config["keywords"]

"""
環境変数の設定
"""

# local で実行する場合の環境変数の読み込み
dotenv_path = join(dirname(__file__), "..", ".env.local")
env_values = dotenv_values(dotenv_path)

SLACK_ID: str | None = os.getenv("SLACK_ID") or env_values.get("SLACK_ID", None)
LINE_TOKEN: str | None = os.getenv("LINE_TOKEN") or env_values.get("LINE_TOKEN", None)
DEEPL_AUTH_KEY: str | None = os.getenv("DEEPL_AUTH_KEY") or env_values.get(
    "DEEPL_AUTH_KEY", None
)
