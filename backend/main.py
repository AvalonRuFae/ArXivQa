from fastapi import FastAPI
import httpx
import feedparser

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "ok"}