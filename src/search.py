import datetime

import arxiv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

from .my_types import Result
from .translate import get_translated_text


def make_arxiv_query(subject: str) -> str:
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
    return (
        f"({subject}) AND "
        f"submittedDate:"
        f"[{day_before_yesterday_str}000000 TO {day_before_yesterday_str}235959]"
    )


def request_arxiv_articles(subject: str) -> list:
    """arXiv から指定した学問領域の論文を取得する

    Parameters
    ----------
    subject : str
        学問領域

    Returns
    -------
    list
        arXiv から取得した論文のリスト
    """
    query = make_arxiv_query(subject)
    return arxiv.query(
        query=query, max_results=1000, sort_by="submittedDate", iterative=False
    )


def calc_score(abstract: str, keywords: dict) -> tuple[float, list]:
    """論文のアブストラクトにキーワードが含まれるかを判定し、スコアを計算する

    キーワードが含まれる場合、重み付けした値でスコアに加算する。

    Parameters
    ----------
    abstract : str
        論文の要約
    keywords : dict
        キーワードと、その重み付けを格納した辞書

    Returns:
        tuple[float, list]: 合算したスコアと、ヒットしたキーワードのリスト
    """

    sum_score = 0.0
    hit_kwd_list = []

    for keyword, weighted_score in keywords.items():
        if keyword.lower() in abstract.lower():
            sum_score += weighted_score
            hit_kwd_list.append(keyword)
    return sum_score, hit_kwd_list


def search_keyword(
    articles: list, keywords: dict, score_threshold: float
) -> list[Result]:
    """論文のリストから、キーワードにマッチする論文を抽出する

    Parameters
    ----------
    articles : list
        論文のリスト
    keywords : dict
        キーワードと、その重み付けを格納した辞書
    score_threshold : float
        スコアの閾値

    Returns
    -------
    list[Result]
        フィルタした論文のリスト
    """
    # ヘッドレスモードでブラウザを起動
    options = Options()
    options.add_argument("--headless")

    # ブラウザーを起動
    driver_path = GeckoDriverManager().install()
    driver = webdriver.Firefox(executable_path=driver_path, options=options)

    results: list[Result] = []

    for article in articles:
        url, title, abstract = (
            article["arxiv_url"],
            article["title"],
            article["summary"],
        )
        score, hit_keywords = calc_score(abstract, keywords)

        if (score != 0) and (score >= score_threshold):
            title_trans = get_translated_text("ja", "en", title, driver)

            abstract = abstract.replace("\n", "")
            abstract_trans = get_translated_text("ja", "en", abstract, driver)

            result = Result(
                url=url,
                title=title_trans,
                abstract=abstract_trans,
                score=score,
                words=hit_keywords,
            )
            results.append(result)

    driver.close()
    driver.quit()
    return results
