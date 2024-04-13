"""
メイン関数
"""

import argparse
import os

import yaml

from .my_types import Keywords
from .notify import notify
from .search import filter_articles, request_arxiv_articles


def get_config() -> tuple[str, Keywords, float]:
    """設定ファイルを読み込む

    subject: 学問領域の指定
    keywords: キーワードと重み
    score_threshold: 通知するスコアの閾値

    Returns
    -------
    tuple[str, Keywords, float]
        設定ファイルの内容 (subject, keywords, score_threshold)
    """
    file_abs_path = os.path.abspath(__file__)
    file_dir = os.path.dirname(file_abs_path)
    config_path = f"{file_dir}/../config.yaml"
    with open(config_path, "r") as yml:
        config = yaml.load(yml, Loader=yaml.FullLoader)
    return (
        config["subject"],
        config["keywords"],
        float(config["score_threshold"]),
    )


def get_args() -> argparse.Namespace:
    """コマンドライン引数を取得する

    Returns
    -------
    argparse.Namespace
        コマンドライン引数
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--slack_id", default=None)
    parser.add_argument("--line_token", default=None)
    return parser.parse_args()


def main() -> None:
    # 論文を取得する
    subject, keywords, score_threshold = get_config()
    articles = request_arxiv_articles(subject)

    # フィルタする
    results = filter_articles(articles, keywords, score_threshold)

    # 通知する
    args = get_args()
    slack_id: str | None = os.getenv("SLACK_ID") or args.slack_id
    line_token: str | None = os.getenv("LINE_TOKEN") or args.line_token
    notify(results, slack_id, line_token)


if __name__ == "__main__":
    main()
