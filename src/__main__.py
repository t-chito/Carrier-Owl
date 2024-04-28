"""
メイン関数
"""

from .notify import notify
from .search import get_articles


def main() -> None:
    articles = get_articles()
    notify(articles)


if __name__ == "__main__":
    main()
