import uvicorn
from fastapi import FastAPI, Body, Query
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


@app.post("/items")
def update_item(item: Item):
    return item


@app.post("/items_without_model")
def update_item_without_model(name: str = Body(), price: float = Body(), is_offer: bool | None = Body()):
    return {'name': name, 'price': price, 'is_offer': is_offer}


@app.get("/items/")
def read_items(q: str | None = Query(default=None, max_length=5, regex="^\d{0,5}$")):
    return q


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
