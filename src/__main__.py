"""
メイン関数
"""

from .config import KEYWORDS, SUBJECT
from .notify import notify
from .search import format_articles_to_result, request_arxiv_articles


def main() -> None:
    # 論文を取得する
    articles = request_arxiv_articles(SUBJECT, KEYWORDS)

    # フォーマットする
    results = format_articles_to_result(articles, KEYWORDS)

    # 通知する
    notify(results)


if __name__ == "__main__":
    main()
