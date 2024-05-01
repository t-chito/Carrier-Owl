"""
GCF エントリーポイント
"""

from http import HTTPStatus

import functions_framework
from flask import Request, Response

from .arxiv import download_pdf, retrieve_article
from .deepl import translate_text
from .llm import summarize_with_llm
from .my_types import SlackEventReactionAdded
from .slack import (
    extract_url_from_message,
    reply_to_message,
)

# 処理と、トリガーとなるリアクションの対応表
REACTIONS_MAP = {
    # アブストを取得する
    "ABSTRACT": "eyes",
    # 要約を取得する
    "SUMMARY": "pencil",
}

# 一時ファイルの保存先。GCF は /tmp にだけ書き込み権限がある
TMP_DIR = "/tmp"


@functions_framework.http
def owl_function(request: Request) -> Response:
    """リクエストをいい感じに処理する

    1. 認証リクエストの場合は認証を行う。
    2. 再送されたリクエストの場合、処理をせずに終了する。
    3. 上記以外はリクエストを処理する。

    - https://api.slack.com/apis/connections/events-api#responding
    - https://dev.classmethod.jp/articles/slack-resend-matome/#toc-2

    Parameters
    ----------
    request : Request
        リクエスト

    Returns
    -------
    Response
        レスポンス (なんでも良い)
    """

    body = request.get_json()

    # 認証リクエストの場合は認証を行う
    if body["type"] == "url_verification":
        return create_response({"challenge": body["challenge"]})

    # 再送されたリクエストの場合は処理をせずに終了する
    if int(request.headers.get(key="X-Slack-Retry-Num", default="0")) > 0:
        return OK_RESPONSE

    # データ取得
    data: SlackEventReactionAdded = body
    url = extract_url_from_message(data)
    article = retrieve_article(url)

    # リアクションに応じた処理を行う
    if data["event"]["reaction"] == REACTIONS_MAP["ABSTRACT"]:
        # abstract の和訳を取得する
        result = translate_text(article.summary)
    elif data["event"]["reaction"] == REACTIONS_MAP["SUMMARY"]:
        # 内容の要約を取得する
        file_path = download_pdf(article, TMP_DIR)
        result = summarize_with_llm(file_path)
    else:
        return OK_RESPONSE

    reply_to_message(data, result)

    return OK_RESPONSE


def create_response(
    body: dict | None = None, status_code: HTTPStatus = HTTPStatus.OK
) -> Response:
    """レスポンスを作成する

    Parameters
    ----------
    body : dict | None
        レスポンスの中身

    Returns
    -------
    Response
        レスポンス
    """

    if body is None:
        return Response(status=status_code)

    return Response(response=body, content_type="application/json", status=status_code)


OK_RESPONSE = create_response()
