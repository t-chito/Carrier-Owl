import argparse
import datetime
import os

import arxiv
import yaml

from .notify import notify
from .search import search_keyword


def get_config() -> dict:
    file_abs_path = os.path.abspath(__file__)
    file_dir = os.path.dirname(file_abs_path)
    config_path = f"{file_dir}/../config.yaml"
    with open(config_path, "r") as yml:
        config = yaml.load(yml, Loader=yaml.FullLoader)
    return config


def main():
    # debug用
    parser = argparse.ArgumentParser()
    parser.add_argument("--slack_id", default=None)
    parser.add_argument("--line_token", default=None)
    args = parser.parse_args()

    config = get_config()
    subject = config["subject"]
    keywords = config["keywords"]
    score_threshold = float(config["score_threshold"])

    day_before_yesterday = datetime.datetime.today() - datetime.timedelta(days=2)
    day_before_yesterday_str = day_before_yesterday.strftime("%Y%m%d")
    # datetime format YYYYMMDDHHMMSS
    arxiv_query = (
        f"({subject}) AND "
        f"submittedDate:"
        f"[{day_before_yesterday_str}000000 TO {day_before_yesterday_str}235959]"
    )
    articles = arxiv.query(
        query=arxiv_query, max_results=1000, sort_by="submittedDate", iterative=False
    )
    print("196")
    results = search_keyword(articles, keywords, score_threshold)

    slack_id = os.getenv("SLACK_ID") or args.slack_id
    line_token = os.getenv("LINE_TOKEN") or args.line_token
    notify(results, slack_id, line_token)


if __name__ == "__main__":
    main()
