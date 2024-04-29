"""arXiv から論文を検索するモジュール"""

import datetime

import arxiv

from ..config import KEYWORDS, SUBJECT
from ..my_types.my_types import ArticleInfo, taxonomy

client = arxiv.Client()


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
        iterative=False,
    )
    results = client.results(search)
    return list(results)


def get_containing_keywords(abstract: str, keywords: list[str]) -> list[str]:
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


def convert_subjects_category_to_expression(subject: str) -> str:
    """subject を読んでわかる表現に変換する

    Parameters
    ----------
    subject : str
        細分化した学問領域。cs.AI など

    Returns
    -------
    str
        表示用の文字列
    """

    if subject not in taxonomy:
        # 今は cs 系のみ taxonomy に用意しているので、それ以外はそのまま返す
        return subject
    else:
        return subject + ": " + taxonomy[subject]["name"]


def format_search_results_into_articles_info(
    search_results: list[arxiv.Result], keywords: list[str]
) -> list[ArticleInfo]:
    """論文のリストを表示用のデータ形式に変換する

    Parameters
    ----------
    search_results : list[arxiv.Result]
        論文の検索結果のリスト
    keywords : list[str]
        abstract に含まれる可能性のあるワード

    Returns
    -------
    list[ArticleInfo]
        表示用の論文リスト
    """

    articles: list[ArticleInfo] = []

    for search_result in search_results:
        abstract, _subjects = (
            search_result.summary,
            search_result.categories,
        )
        containing_keywords = get_containing_keywords(abstract, keywords)
        subjects = [
            convert_subjects_category_to_expression(subject) for subject in _subjects
        ]

        result = ArticleInfo(
            id=search_result.get_short_id(),
            url=search_result.entry_id,
            title_original=search_result.title,
            # 処理が翻訳機能に依存しないように、この時点では翻訳しないものとする
            title_translated="",
            words=containing_keywords,
            subjects=subjects,
        )
        articles.append(result)

    return articles


def get_article_info_list(
    subject: str = SUBJECT, keywords: list[str] = KEYWORDS
) -> list[ArticleInfo]:
    """学問領域とキーワードを指定して論文を検索する

    Parameters
    ----------
    subject : str
        学問領域
    keywords : list[str]
        abstract に含まれるキーワード

    Returns
    -------
    list[ArticleInfo]
        論文リスト
    """
    search_results = search_arxiv_articles(subject, keywords)
    articles = format_search_results_into_articles_info(search_results, keywords)

    return articles


def find_article(url: str) -> arxiv.Result:
    """
    arXiv の URL から特定の論文を取得する
    """

    entry_id = url.split("arxiv.org/abs/")[-1]
    article = next(client.results(arxiv.Search(id_list=[entry_id])))

    return article
