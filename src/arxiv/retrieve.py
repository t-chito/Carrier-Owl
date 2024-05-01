"""
指定した arXiv の論文を取得する機能を提供するモジュール
"""

from os import path

import arxiv

from .common import client


def retrieve_article(url: str) -> arxiv.Result:
    """
    arXiv の URL から特定の論文を取得する
    """

    entry_id = url.split("arxiv.org/abs/")[-1]
    article = next(client.results(arxiv.Search(id_list=[entry_id])))

    return article


def download_pdf(url: str) -> str:
    """指定した URL に対応する論文の PDF をダウンロードする

    Returns
    -------
    str
        ダウンロードした PDF の絶対パス
    """

    article = retrieve_article(url)
    file_path = article.download_pdf()
    return path.abspath(file_path)
