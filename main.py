from flask import Flask
from src import home

app = Flask(__name__)

@app.route("/<url>")
def user(url):
    return home.path(url)
  
if __name__ == "__main__": 
    app.run(debug=True) 
