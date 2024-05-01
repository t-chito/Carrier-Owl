"""
loader と text_splitter を提供するモジュール

- https://python.langchain.com/docs/modules/data_connection/document_loaders/pdf/
- https://python.langchain.com/docs/use_cases/summarization/#option-2.-map-reduce:~:text=Combining%20our%20map%20and%20reduce%20chains%20into%20one%3A
"""

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter


def load_pdf_as_splitted_docs(
    file_path: str, use_splitter: bool = True
) -> list[Document]:
    """pdf ファイルを読み込んで、分割された Document のリストとして返す

    Parameters
    ----------
    file_path : str
        pdf ファイルのパス

    use_splitter : bool
        text_splitter を使うかどうか

    Returns
    -------
    list[Document]
        Document のリスト。splitter を使わない場合は page 単位で分割される
    """
    loader = PyPDFLoader(file_path, extract_images=False)
    docs = loader.load_and_split(text_splitter=text_splitter if use_splitter else None)

    return docs


text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=1000, chunk_overlap=0
)
