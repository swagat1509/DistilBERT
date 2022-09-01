import uvicorn
from transformers import pipeline
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Sentiment(BaseModel):
    #sentiment: str
    #sentiment_probability: float
    text: str

nlp = pipeline("sentiment-analysis",model="distilbert-base-uncased-finetuned-sst-2-english", tokenizer="distilbert-base-uncased-finetuned-sst-2-english")

@app.get('/')
def get_root():
    return " Sentiment Analysis App"


#@app.post('/getsentiment')
#def get_sentiment(data: str):
#    return nlp(data)


@app.post('/getsentiment')
def get_sentiment(getsentiment: Sentiment):
    t=nlp(getsentiment.text)
    return t[0]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)