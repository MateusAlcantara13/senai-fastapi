from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Minha API", version="1.0.0")


class Item(BaseModel):
    name: str
    price: float


@app.get("/")
async def root():
    return {"status": "ok", "message": "API rodando!"}


@app.get("/health")
async def health():
    return {"status": "healthy"}


@app.post("/items")
async def create_item(item: Item):
    return {"created": item}
