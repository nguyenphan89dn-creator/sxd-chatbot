from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

files = [
    "1392.KH.SXD.26.01.2026.signed.signed.signed.signed.pdf",
    "1827.KH.SXD.30.01.2026.signed.signed.signed.pdf",
    "3688.KH.SXD.13.03.2026.signed.signed.signed.pdf",
    "7891.KH.SXD.14.05.2026.signed.signed.signed (1).pdf"
]

docs = []

for file in files:
    loader = PyPDFLoader(file)
    docs.extend(loader.load())

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(docs)

db = Chroma.from_documents(
    chunks,
    OpenAIEmbeddings(),
    persist_directory="./db"
)

print("Done!")
