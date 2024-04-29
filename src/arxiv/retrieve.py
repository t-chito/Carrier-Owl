"""
指定した arXiv の論文を取得する機能を提供するモジュール
"""

import arxiv

from .common import client


def retrieve_article(url: str) -> arxiv.Result:
    """
    arXiv の URL から特定の論文を取得する
    """

    entry_id = url.split("arxiv.org/abs/")[-1]
    article = next(client.results(arxiv.Search(id_list=[entry_id])))

    return article
