from pathlib import Path
from typing import List,Any
from langchain_community.document_loaders import PyPDFLoader,TextLoader,CSVLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders.excel import UnstructuredExcelLoader
from langchain_community.document_loaders import JSONLoader


def load_all_documents(data_dir:str) ->List[Any]:
    """
    Load all supported files from the data directory and convert to langchain document structure
    Support:PDF,TXT,CSV.EXCEL,WOrd,JSON
    """

    #Use project root data folder
    data_path = Path(data_dir).resolve()
    print(f"[DEBUG] Data Path : {data_path}")
    documents = []

    # PDF files
    pdf_files = list(data_path.glob('**/*.pdf'))
    print(f"[DEBUG] Found {len(pdf_files)} PDF files: {[str(f) for f in pdf_files]}")

    for pdf_file in pdf_files:
        print(f"[DEBUG] Loading PDF: {pdf_file}")
        try:
            loader = PyPDFLoader(str(pdf_file))
            loaded = loader.load()
            print(f"[DEBUG] Loaded {len(loaded)} PDF docs from {pdf_file}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[ERROR] Failed to load PDF {pdf_file}: {e}")

    #Txt files
    text_files = list(data_path.glob('**/*.txt'))
    print(f"[DEBUG] Found {len(text_files)} TXT files: {[str(f) for f in text_files]}")

    for txt_file in text_files:
        print(f"[DEBUG] Loading TXT: {txt_file}")
        try:
            loader = TextLoader(str(txt_file))
            loaded = loader.load()
            print(f"[DEBUG] Loaded {len(loaded)} TXT docs from {txt_file}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[Error] Failed to load TEXT {txt_file} : {e}")

    #CSV files
    csv_files = list(data_path.glob('**/*.csv'))
    print(f"[DEBUG] Found {len(csv_files)} TXT files: {[str(f) for f in csv_files]}")

    for csv_file in csv_files:
        print(f"[DEBUG] Loading TXT: {csv_file}")
        try:
            loader = CSVLoader(str(csv_file))
            loaded = loader.load()
            print(f"[DEBUG] Loaded {len(loaded)} CSV docs from {csv_file}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[Error] Failed to load CSV {csv_file} : {e}")


    #Txt files
    text_files = list(data_path.glob('**/*.txt'))
    print(f"[DEBUG] Found {len(text_files)} TXT files: {[str(f) for f in text_files]}")

    for txt_file in text_files:
        print(f"[DEBUG] Loading TXT: {txt_file}")
        try:
            loader = TextLoader(str(txt_file))
            loaded = loader.load()
            print(f"[DEBUG] Loaded {len(loaded)} TXT docs from {txt_file}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[Error] Failed to load TEXT {txt_file} : {e}")


    # SQL files
    sql_files = list(data_path.glob("**/*.sql"))
    print(
        f"[DEBUG] Found {len(sql_files)} SQL files: "
        f"{[str(f) for f in sql_files]}"
    )

    for sql_file in sql_files:
        print(f"[DEBUG] Loading SQL: {sql_file}")

        try:
            with open(sql_file, "r", encoding="utf-8") as f:
                sql_content = f.read()

            loaded = documents(
                page_content=sql_content,
                metadata={
                    "source": str(sql_file),
                    "file_type": "sql"
                }
            )

            print(f"[DEBUG] Loaded SQL file: {sql_file}")
            documents.append(loaded)

        except Exception as e:
            print(
                f"[ERROR] Failed to load SQL "
                f"{sql_file}: {e}"
            )

    return documents