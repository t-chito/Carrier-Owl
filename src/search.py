from dataclasses import dataclass

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

from .translate import get_translated_text


@dataclass
class Result:
    url: str
    title: str
    abstract: str
    words: list
    score: float = 0.0


def calc_score(abstract: str, keywords: dict) -> tuple[float, list]:
    sum_score = 0.0
    hit_kwd_list = []

    for word in keywords.keys():
        score = keywords[word]
        if word.lower() in abstract.lower():
            sum_score += score
            hit_kwd_list.append(word)
    return sum_score, hit_kwd_list


def search_keyword(articles: list, keywords: dict, score_threshold: float) -> list:
    results = []

    # print(articles)

    # ヘッドレスモードでブラウザを起動
    options = Options()
    options.add_argument("--headless")

    # ブラウザーを起動
    print("GeckoDriverをインストールします。")
    driver_path = GeckoDriverManager().install()
    print(f"GeckoDriverのパス: {driver_path}")

    print("Firefoxをヘッドレスモードで起動します。")
    driver = webdriver.Firefox(executable_path=driver_path, options=options)
    print("Firefoxが正常に起動しました。")

    print("Firefoxの起動をスキップします。")
    print("次の処理を実行します。")
    # print(articles)  # この行が以前に成功していた場合、再度ここで出力を試みます。
    print("articlesの出力後")

    for article in articles:
        print(article)
        url = article["arxiv_url"]
        title = article["title"]
        abstract = article["summary"]
        score, hit_keywords = calc_score(abstract, keywords)
        print(score)
        if (score != 0) and (score >= score_threshold):
            print("1")
            title_trans = get_translated_text("ja", "en", title, driver)
            abstract = abstract.replace("\n", "")
            print("2")
            abstract_trans = get_translated_text("ja", "en", abstract, driver)
            # abstract_trans = textwrap.wrap(abstract_trans, 40)  # 40行で改行
            # abstract_trans = '\n'.join(abstract_trans)
            print("3")
            result = Result(
                url=url,
                title=title_trans,
                abstract=abstract_trans,
                score=score,
                words=hit_keywords,
            )
            print("4")
            results.append(result)
            print("5")

    print("close")
    driver.close()
    print("quit")
    # ブラウザ停止
    driver.quit()
    print("return")
    return results
