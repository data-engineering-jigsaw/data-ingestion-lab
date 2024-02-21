from llama_index.core.indices.loading import load_index_from_storage

from index import *

file_path = "./data/10k/uber_2021.pdf"
text = read_doc_text(file_path)
# nodes = build_nodes_from_text(text)
# first_node = nodes[0]
# build_embeddings(nodes)
# index = build_index(nodes)
# query_engine = build_query_engine_from(index)
# response = query_engine.query("What is the revenue growth of Uber from 2020 to 2021?")
# response_text = response.response

# # And we can see where this came from with 
# response.source_nodes[0]
# persist_data(index)

