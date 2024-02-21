import os

import fitz
from llama_index.core import Document, VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.storage.storage_context import StorageContext
from llama_index.embeddings.openai import OpenAIEmbedding


def read_doc_text(file_path):
    doc_text = ""
    doc = fitz.open(file_path)
    for doc_idx, page in enumerate(doc):
        page_text = page.get_text("text")
        doc_text += page_text
    return doc_text

def build_nodes_from_text(text):
    documents = [Document(text = text)]
    parser = SentenceSplitter(chunk_size=1024)
    nodes = parser.get_nodes_from_documents(documents)
    return nodes

def build_embeddings(nodes):
    api_key = "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"
    os.environ['OPENAI_API_KEY'] =api_key
    embed_model = OpenAIEmbedding(api_key=api_key)
    for node in nodes:
        node_embedding = embed_model.get_text_embedding(
            node.get_content()
        )
        node.embedding = node_embedding

def build_index(nodes):
    index = VectorStoreIndex(nodes)
    return index

def build_query_engine_from(index):
    query_engine = index.as_query_engine(response_mode="tree_summarize")
    return query_engine

def persist_data(index, location = "./storage"):
    index.set_index_id("vector_index")
    index.storage_context.persist(location)
    storage_context = StorageContext.from_defaults(persist_dir="storage")
    return storage_context

# index = load_index_from_storage(storage_context, index_id="vector_index")