from langchain_openai.embeddings import OpenAIEmbeddings
from openai import OpenAI
from langchain_experimental.text_splitter import SemanticChunker


openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"
client = OpenAI(
        api_key=openai_api_key,
        base_url=openai_api_base,
)
models = client.models.list()
model = models.data[0].id
print(model)


embeddings = OpenAIEmbeddings(model=model,
                                  api_key=openai_api_key,
                                  base_url=openai_api_base,
                                  # encoding_format="float"
                                  )
text_splitter = SemanticChunker(embeddings)


fname = 'cancer_papers/10766391.txt'
with open(fname) as f:
    paper = f.read()


embeddings = OpenAIEmbeddings(model=model,
                                  api_key=openai_api_key,
                                  base_url=openai_api_base,
                                  # encoding_format="float"
                                  )

# 1. Create the text splitter
text_splitter = SemanticChunker(embeddings)

# 2. Split the text
docs = text_splitter.create_documents([paper])
# print(docs)

# 3. Embed the semantically chunked text
# query_result = embeddings.embed_query(docs)

print (len(docs))


query_result = embeddings.embed_query(docs)


# This runs after a fresh restart of vllm
query_result = client.embeddings.create(
        input=[prompt],
        model=model,
        encoding_format="float",
)
print(query_result)


for n in range(0, len(docs) - 1):
    query_result = embeddings.embed_query(docs[n].page_content)
    print (f'{len(docs[n].page_content)}\t{len(query_result)}')
    # print (query_result)

