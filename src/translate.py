"""和訳を行うモジュール"""

import requests

from .config import DEEPL_AUTH_KEY


def translate_text(text: str, source_lang: str = "EN", target_lang: str = "JA") -> str:
    """テキストを翻訳して返す

    DeepL API で和訳を行う
    - https://qiita.com/yaju/items/bf4613393cd4ee402d17

    Parameters
    ----------
    text : str
        翻訳するテキスト
    source_lang : str, optional
        入力言語, by default "ja"
    target_lang : str, optional
        出力言語, by default "en"

    Returns
    -------
    str
        翻訳されたテキスト
    """

    request_params = {
        "auth_key": DEEPL_AUTH_KEY,
        "text": text,
        "source_lang": source_lang,
        "target_lang": target_lang,
    }

    response = requests.post(
        "https://api-free.deepl.com/v2/translate", data=request_params
    )

    return response.json()["translations"][0]["text"]


def translate_texts(
    texts: list[str], source_lang: str = "EN", target_lang: str = "JA"
) -> list[str]:
    """複数のテキストを翻訳して返す

    Parameters
    ----------
    texts : list[str]
        翻訳するテキスト
    source_lang : str, optional
        入力言語, by default "EN"
    target_lang : str, optional
        出力言語, by default "JA"

    Returns
    -------
    list[str]
        翻訳されたテキスト
    """

    # 空のリストの場合は API を叩くとエラーになるので、空リストを返す
    if len(texts) == 0:
        return []

    request_params = {
        "auth_key": DEEPL_AUTH_KEY,
        "text": texts,
        "source_lang": source_lang,
        "target_lang": target_lang,
    }

    response = requests.post(
        "https://api-free.deepl.com/v2/translate", data=request_params
    )

    results = [res["text"] for res in response.json()["translations"]]

    return results
