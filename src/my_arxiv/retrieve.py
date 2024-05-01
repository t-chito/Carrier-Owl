"""
指定した arXiv の論文を取得する機能を提供するモジュール
"""

from os import path

import arxiv

from .common import client


def retrieve_article(url: str) -> arxiv.Result:
    """arXiv の URL から特定の論文を取得する

    Parameters
    ----------
    url : str
        arXiv の URL

    Returns
    -------
    arxiv.Result
        論文データ
    """

    entry_id = url.split("arxiv.org/abs/")[-1]
    article = next(client.results(arxiv.Search(id_list=[entry_id])))

    return article


def download_pdf(article: arxiv.Result, dirpath: str = "./") -> str:
    """指定した article の PDF をダウンロードする

    Parameters
    ----------
    article : arxiv.Result
        論文
    dirpath : str, optional
        ダウンロード先のディレクトリ, by default "./"

    Returns
    -------
    str
        ダウンロードした PDF の絶対パス
    """

    file_path = article.download_pdf(dirpath=dirpath)
    return path.abspath(file_path)
