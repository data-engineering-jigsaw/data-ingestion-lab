import os

import fitz
from llama_index.core import Document, VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.storage.storage_context import StorageContext
from llama_index.embeddings.openai import OpenAIEmbedding


def read_doc_text(file_path):
    pass

def build_nodes_from_text(text):
    pass

def build_embeddings(nodes):
    pass

def build_index(nodes):
    pass

def build_query_engine_from(index):
    pass

def persist_data(index, location = "./storage"):
    pass

# index = load_index_from_storage(storage_context, index_id="vector_index")