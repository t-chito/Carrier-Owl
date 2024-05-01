"""
メイン関数

TODO: __main__.py と main.py があるので統一したい
"""

from my_packages.arxiv import get_article_info_list
from my_packages.deepl import translate_texts
from my_packages.slack import notify


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
