#!/usr/bin/python3

from fastapi import FastAPI

app = FastAPI(title="GC Hackathon", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "Welcome to our discussion forum meant for GC Hackathon participants and a few special creatures"}


