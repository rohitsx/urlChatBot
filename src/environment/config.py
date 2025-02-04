import os
from dotenv import load_dotenv

load_dotenv()

groqApi = os.getenv('GROQ_API')
pineconeApi = os.getenv('PINECONE_API')
