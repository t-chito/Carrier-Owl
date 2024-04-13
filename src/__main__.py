"""
メイン関数
"""

from .config import KEYWORDS, SCORE_THRESHOLD, SUBJECT
from .notify import notify
from .search import filter_articles, request_arxiv_articles


def main() -> None:
    # 論文を取得する
    articles = request_arxiv_articles(SUBJECT)

    # フィルタする
    results = filter_articles(articles, KEYWORDS, SCORE_THRESHOLD)

    # 通知する
    notify(results)


if __name__ == "__main__":
    main()
