import time
import urllib.parse

from selenium.common.exceptions import NoSuchElementException


def get_translated_text(from_lang: str, to_lang: str, from_text: str, driver) -> str:
    """
    https://qiita.com/fujino-fpu/items/e94d4ff9e7a5784b2987
    """

    sleep_time = 1

    # urlencode
    from_text = urllib.parse.quote(from_text)

    # url作成
    url = (
        "https://www.deepl.com/translator#"
        + from_lang
        + "/"
        + to_lang
        + "/"
        + from_text
    )

    driver.get(url)
    driver.implicitly_wait(10)  # 見つからないときは、10秒まで待つ

    for i in range(30):
        # 指定時間待つ
        time.sleep(sleep_time)
        to_text = get_text_from_driver(driver)

        if to_text:
            break
    if to_text is None:
        return urllib.parse.unquote(from_text)
    return to_text


def get_text_from_driver(driver) -> str | None:
    try:
        elem = driver.find_element_by_class_name("lmt__translations_as_text__text_btn")
    except NoSuchElementException:
        return None
    text = elem.get_attribute("innerHTML")
    return text
