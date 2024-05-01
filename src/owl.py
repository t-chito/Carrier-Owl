"""
論文リストを Slack に通知するスクリプト
"""

from my_packages.arxiv import get_article_info_list
from my_packages.deepl import translate_texts
from my_packages.slack import notify


def main() -> None:
    """論文のリストを取得して Slack に通知する"""
    articles = get_article_info_list()

    titles_translated = translate_texts(
        [article.title_original for article in articles]
    )

    for index, article in enumerate(articles):
        article.title_translated = titles_translated[index]

    notify(articles)


if __name__ == "__main__":
    main()
