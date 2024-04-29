"""
slack のテキストを処理する
"""

import datetime

from ..my_types import ArticleInfo

divider = "-" * 80


def create_dividing_text(num_of_articles: int) -> str:
    """通知の開始・終了部分のテキストを作成する

    Parameters
    ----------
    num_of_articles : int
        論文の数

    Returns
    -------
    str
        通知の開始部分のテキスト
    """
    today = datetime.date.today()
    text = f"{today} : num of articles = {num_of_articles}"
    return f"{divider}\n" f"{text}" f"\n{divider}"


def create_message_text(article: ArticleInfo) -> str:
    """論文情報から通知テキストを作成する

    Parameters
    ----------
    articles : ArticleInfo
        論文情報

    Returns
    -------
    str
        テキスト
    """

    text = (
        f"\n タイトル (原文): *{article.title_original}*"
        f"\n タイトル (翻訳): *{article.title_translated}*"
        f"\n keywords: `{article.words}`"
        f"\n subjects: `{article.subjects}`"
        f"\n URL: {article.url}"
        f"\n {divider}"
    )

    return text
