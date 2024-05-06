from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def function():
    return { "hello" : "world" }