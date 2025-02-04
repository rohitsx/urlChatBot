import urllib.request
from bs4 import BeautifulSoup
from langchain_text_splitters import character
import handleDatabase

def path(url):
    try:
        req = urllib.request.Request(
            'https://medium.com/@suraj_bansal/build-your-own-ai-chatbot-a-beginners-guide-to-rag-and-langchain-0189a18ec401', 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        )
        with urllib.request.urlopen(req) as f:
            html = f.read().decode('utf-8')  
            htmlWithoutTag = BeautifulSoup(html, 'html.parser').get_text()

            text_splitter = character.CharacterTextSplitter(separator=".", chunk_size=1000, chunk_overlap=100)
            texts = text_splitter.split_text(htmlWithoutTag)

            handleDatabase.database(texts)

            print(f"htmlWithoutTag len {len(htmlWithoutTag)} divided, {len(htmlWithoutTag)/len(texts)} per chucks")
            return f"Done for {texts}"
    except Exception as e:
        return f"Error fetching {url}: {e}"


