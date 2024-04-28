"""
メイン関数
"""

from .notify import notify
from .search import get_article_info_list
from .translate import translate_texts


def main() -> None:
    articles = get_article_info_list()

    titles_translated = translate_texts(
        [article.title_original for article in articles]
    )

    for index, article in enumerate(articles):
        article.title_translated = titles_translated[index]

    notify(articles)


if __name__ == "__main__":
    main()
