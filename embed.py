from openai import OpenAI

# Modify OpenAI's API key and API base to use vLLM's API server.

def embed(texts):
    
    openai_api_key = "EMPTY"
    openai_api_base = "http://rbdgx1.cels.anl.gov:8000/v1"

    client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
        api_key=openai_api_key,
        base_url=openai_api_base,
    )

    models = client.models.list()
    model = models.data[0].id
    print(f'Using model: {model}')

    responses = client.embeddings.create(
        input=texts,
        model=model,
        encoding_format="float",
    )
    return responses

    
if __name__ == "__main__":
    texts = [
        "Hello my name is",
        "The best thing about vLLM is that it supports many different models"
    ]
    
    responses = embed(texts)
    for data in responses.data:
        print(data.embedding)  # list of float of len 4096