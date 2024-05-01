"""
論文の要約機能を提供するモジュール

- https://python.langchain.com/docs/use_cases/summarization/
- https://python.langchain.com/docs/use_cases/summarization/#option-3.-refine
- https://github.com/langchain-ai/langchain/issues/15741
"""

from langchain.chains.summarize import load_summarize_chain
from langchain_core.prompts import PromptTemplate

from .common import llm
from .loader import load_pdf_as_splitted_docs

summarize_prompt_template = """
末尾に示す論文を日本語で要約してください。要約は以下の観点に則って行ってください。

- その論文はどのような課題を解決したのか
- その課題の背景はどのようなものか
- 先行研究と比べて何が優れているのか
- 技術や手法のキモはどこか
- 提案手法をどうやって有効だと検証したのか
- クローズしていない議論はあるか

#論文
{text}
"""

summarize_prompt = PromptTemplate.from_template(summarize_prompt_template)

refine_template = """
あなたのタスクは、論文についての最終的な要約を作成することです。
以下に、論文の途中までを参照して作成した、現時点での要約を提供します。

#既存の要約
---
{existing_answer}
---

以下は、既存の要約では参照していなかった論文の続き(一部)です。


#論文の続き(一部)
------------
{text}
------------

もし有益な情報が含まれていれば、この論文の続きの文章を参照して既存の要約を洗練させてください。
もしこの論文の続きが有用でない場合は、元の要約をそのまま返してください。
"""

refine_prompt = PromptTemplate.from_template(refine_template)

chain = load_summarize_chain(
    llm=llm,
    chain_type="refine",
    question_prompt=summarize_prompt,
    refine_prompt=refine_prompt,
    return_intermediate_steps=True,
    input_key="input_documents",
    output_key="output_text",
)


def summarize_with_llm(file_path: str) -> str:
    """llm を使ってテキストを要約する

    - file は pdf を前提とする
    - 要約は refine で行う

    Parameters
    ----------
    file_path : str
        ファイルパス

    Returns
    -------
    str
        要約されたテキスト
    """

    splitted_docs = load_pdf_as_splitted_docs(file_path)
    result = chain.invoke({"input_documents": splitted_docs}, return_only_outputs=True)

    return result["output_text"]
