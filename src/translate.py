"""和訳を行うモジュール"""

import requests

API_KEY: str = "7c672a7a-6c0a-4893-bf87-67450b6ee072:fx"


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
        "auth_key": API_KEY,
        "text": text,
        "source_lang": source_lang,
        "target_lang": target_lang,
    }

    response = requests.post(
        "https://api-free.deepl.com/v2/translate", data=request_params
    ).json()
    result = response["translations"][0]["text"]

    return result
