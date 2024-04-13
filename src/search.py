"""arXiv から論文を検索するモジュール"""

import datetime

import arxiv

from .my_types import Article, Result
from .translate import translate_texts


def make_arxiv_query(subject: str, keywords: list[str]) -> str:
    """arXiv 検索用のクエリを作成する

    Parameters
    ----------
    subject : str
        学問領域

    Returns
    -------
    str
        arXiv 検索のクエリ
    """

    # 2 日前の日付を取得し、YYYYMMDD 形式の文字列に変換
    day_before_yesterday = datetime.datetime.today() - datetime.timedelta(days=2)
    day_before_yesterday_str = day_before_yesterday.strftime("%Y%m%d")
    # datetime format YYYYMMDDHHMMSS

    if len(keywords) == 1:
        query_keywords = f"abs:{keywords[0]}"
    else:
        # OR でつなげてカッコで囲む
        query_keywords = (
            "(" + " OR ".join([f"abs:{keyword}" for keyword in keywords]) + ")"
        )

    return (
        f"cat:{subject}"
        " AND "
        f"{query_keywords}"
        " AND "
        f"submittedDate:[{day_before_yesterday_str}000000 TO {day_before_yesterday_str}235959]"
    )


def request_arxiv_articles(subject: str, keywords: list[str]) -> list[Article]:
    """指定した学問領域とキーワードの arXiv 論文を取得する

    Parameters
    ----------
    subject : str
        学問領域

    Returns
    -------
    list[Article]
        arXiv から取得した論文のリスト
    """
    query = make_arxiv_query(subject, keywords)
    return arxiv.query(
        query=query, max_results=1000, sort_by="submittedDate", iterative=False
    )


def list_containing_keywords(abstract: str, keywords: list[str]) -> list[str]:
    """論文のアブストラクトに含まれているキーワードを列挙する

    Parameters
    ----------
    abstract : str
        論文の要約
    keywords : list[str]
        abstract に含まれる可能性のあるワード

    Returns:
        list[str]: 論文のアブストラクトに含まれるキーワードのリスト
    """

    containing_keywords: list[str] = []

    for keyword in keywords:
        if keyword.lower() in abstract.lower():
            containing_keywords.append(keyword)
    return containing_keywords


def format_articles_to_result(
    articles: list[Article], keywords: list[str]
) -> list[Result]:
    """論文のリストを表示用のデータ形式に変換する

    Parameters
    ----------
    articles : list[Article]
        論文の検索結果のリスト
    keywords : list[str]
        abstract に含まれる可能性のあるワード

    Returns
    -------
    list[Result]
        表示用の論文リスト
    """

    results: list[Result] = []

    # API を叩くのを一回にするために、タイトルだけ先に取り出して翻訳する # FIXME: ダサい
    titles_translated = translate_texts([article["title"] for article in articles])

    for index, article in enumerate(articles):
        url, title, abstract = (
            article["arxiv_url"],
            article["title"],
            article["summary"],
        )
        containing_keywords = list_containing_keywords(abstract, keywords)

        result = Result(
            url=url,
            title_original=title,
            title_translated=titles_translated[index],
            words=containing_keywords,
        )
        results.append(result)

    return results
