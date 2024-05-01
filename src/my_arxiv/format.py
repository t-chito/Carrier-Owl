"""
arXiv の検索結果を表示用のデータ形式に変換する関数を提供するモジュール
"""

import arxiv

from ..my_types.my_types import ArticleInfo, taxonomy


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
        return subject
    else:
        return subject + ": " + taxonomy[subject]


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
