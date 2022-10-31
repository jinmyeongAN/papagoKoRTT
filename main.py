from fastapi import FastAPI

app = FastAPI()


@app.get("/papago")
async def root():
    return {"message": "Hello World"}
