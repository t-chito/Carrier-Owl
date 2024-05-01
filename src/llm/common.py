"""
LLM 呼び出し用のモジュール

https://python.langchain.com/docs/integrations/chat/google_generative_ai/

公式ドキュメント通りに書いても mypy に怒られるが、
動くようなので一旦 ignore で対応する
"""

from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings

from ..config import GOOGLE_API_KEY

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=GOOGLE_API_KEY,  # type: ignore
)  # type: ignore

# https://ai.google.dev/gemini-api/docs/models/gemini?hl=ja&_gl=1*apvnw0*_up*MQ..*_ga*Nzc3MTEzMDkuMTcxNDQ3NDU4Mg..*_ga_P1DBVKWT6V*MTcxNDQ3NDU4MS4xLjAuMTcxNDQ3NDYwOS4wLjAuMzQzMjM0NDM3
# いわく、1.5 だと 1 分あたり 2 クエリまでなので実用には耐えない
# 1.0 の場合は 1 分あたり 60 回のリクエストまで OK
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)  # type: ignore
