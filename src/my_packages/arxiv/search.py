"""arXiv から論文を検索するモジュール"""

import datetime

import arxiv

from .common import client


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


def search_arxiv_articles(subject: str, keywords: list[str]) -> list[arxiv.Result]:
    """指定した学問領域とキーワードの arXiv 論文を取得する

    Parameters
    ----------
    subject : str
        学問領域

    Returns
    -------
    list[arxiv.Result]
        arXiv から取得した論文のリスト
    """
    query = make_arxiv_query(subject, keywords)
    search = arxiv.Search(
        query=query,
        max_results=100,
        sort_by=arxiv.SortCriterion.SubmittedDate,
    )
    results = client.results(search)
    return list(results)
