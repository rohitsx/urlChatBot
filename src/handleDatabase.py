from pinecone import Pinecone, inference
from environment import config


def database(data):
    pc = Pinecone(api_key=config.pineconeApi)

    embeddings = inference.embed(
        model="multilingual-e5-large",
        inputs=[d['text'] for d in data],
        parameters={"input_type": "passage", "truncate": "END"})

    print(embeddings)

