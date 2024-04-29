from ..config import KEYWORDS, SUBJECT
from ..my_types.my_types import ArticleInfo
from .format import format_search_results_into_articles_info
from .retrieve import retrieve_article
from .search import search_arxiv_articles


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


__all__ = ["get_article_info_list", "retrieve_article"]
