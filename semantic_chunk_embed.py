#!/usr/bin/env python
from _util import _print
from _util import generate_unique_id
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, default=8000,
                    help="port number, default 8000")
parser.add_argument("--host", type=str, default="localhost",
		    help="host name, default localhost")
parser.add_argument("--key", type=str, default="EMPTY",
                    help="embedding server key, default EMPTY")
parser.add_argument("--dir", type=str, default='cancer_papers',
                    help="directory containing .txt files to parse"
                    )
args = parser.parse_args()
host = args.host
port = args.port
openai_api_key=args.key
directory = args.dir
print(f'using host: {args.host}')
print(f'using port: {args.port}')
print(f'using key: {args.key}')
print(f'using dir: {args.dir}')


from langchain_openai.embeddings import OpenAIEmbeddings
from openai import OpenAI
from langchain_experimental.text_splitter import SemanticChunker
import hashlib
import glob, os


openai_api_base = f"http://{host}:{port}/v1"
print(f'{openai_api_base}')
client = OpenAI(
        api_key=openai_api_key,
        base_url=openai_api_base,
)
models = client.models.list()
model = models.data[0].id
print(f'using model {model}')


embeddings = OpenAIEmbeddings(model=model,
                                  api_key=openai_api_key,
                                  base_url=openai_api_base,
                                  # encoding_format="float"
                                  )
text_splitter = SemanticChunker(embeddings)

_t = _print("done setting up")

import csv
outfile = open('embeddings.csv', 'w')
writer = csv.writer(outfile)

for filepath in glob.glob(os.path.join(directory, "*.txt")):
    print(filepath)

    with open(filepath) as f:
        paper = f.read()
    print (f'paper len {len(paper)}')


    embeddings = OpenAIEmbeddings(model=model,
                                  api_key=openai_api_key,
                                  base_url=openai_api_base,
                                  # encoding_format="float",
                                  # dimensions=1024
                                  )


    text_splitter = SemanticChunker(embeddings)
    docs = text_splitter.create_documents([paper])
    print (f'chunks in daoc {len(docs)}')


    for n in range(0, len(docs) - 1):
        embedding = embeddings.embed_query(docs[n].page_content)
        unique_id = generate_unique_id(docs[n].page_content)
        print (f'{unique_id}\tchunk len {len(docs[n].page_content)}\tembedding len {len(embedding)}')
        # write semantic chunk and embedding to a file
        writer.writerow([unique_id, embedding])

    _t = _print(f'done processing file {filepath} with length {len(paper)}', _t)

# end for filepath in directory
