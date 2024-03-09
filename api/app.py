import os
from dotenv import load_dotenv
import pathway as pw
from llm_app import chunk_texts
from common.openapi_helper import openai_chat_completion
from common.embedder import embeddings,index_embeddings
from common.prompt import prompt

load_dotenv()

data_folder_path = os.environ.get("LOCAL_FOLDER_PATH","./data/")

def run(host,port,device: str = "cpu"):
    query, response_writer = pw.io.http.rest_connector(
        host=host,
        port=port,
        schema=QueryInputSchema,
        autocommit_duration_ms=50,
    )

    finance_data = pw.io.fs.read(
        data_folder_path,
        mode="streaming",
        format= 'plaintext_by_file',
        autocommit_duration_ms=50,
    )

    #Chunks
    documents = finance_data.select(chunks=chunk_texts(pw.this.data))
    documents = documents.flatten(pw.this.chunks).rename_columns(chunk=pw.this.chunks)


    #Embeddings
    embedded_data = embeddings(context=documents, data_to_embed=pw.this.chunk)

    #Index Embeddings
    index = index_embeddings(embedded_data)

    #query embedding
    embedded_query = embeddings(context=query, data_to_embed= pw.this.query)

    #prompt generation & models response:
    responses = prompt(index, embedded_query, pw.this.query)

    # Give a response to the api call
    response_writer(responses)

    pw.run()


class QueryInputSchema(pw.Schema):
    query: str

class DataInputSchema(pw.Schema):
    doc: str

