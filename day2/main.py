import uvicorn
from fastapi import FastAPI, Body, Query, Path
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI()


# RequestBody
# Fields
# List fields
# Nested Models
class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    price: float = Field(gt=0, description="expensive", extra="extra")
    is_offer: bool | None = None
    tags: set[str] = set()
    image: Image | None = None
    # image: Image = None

    # name: str = Field(example="Foo")
    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }


@app.post("/items")
def update_item(item: Item):
    return item


@app.post("/items_without_model")
def update_item_without_model(name: str = Body(), price: float = Body(), is_offer: bool | None = Body()):
    return {'name': name, 'price': price, 'is_offer': is_offer}


# Query Params and String Validation
@app.get("/items/")
def read_items(q: str | None = Query(default=None, max_length=5, regex="^\d{0,5}$", alias='item-query')):
    return q


# Path Params and Numeric Validation
@app.get("/items/{item_id}")
def read_items(*, item_id: int = Path(title="This is item id", ge=1), q: str):
    return item_id, q


# Multiple Parameters
@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
    q: str | None = None,
    item: Item | None = Body(
        # embed=True,
        examples={
            "normal": {
                "summary": "A normal example",
                "description": "A **normal** item works correctly.",
                "value": {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                },
            },
            "converted": {
                "summary": "An example with converted data",
                "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                "value": {
                    "name": "Bar",
                    "price": "35.4",
                },
            },
            "invalid": {
                "summary": "Invalid data is rejected with an error",
                "value": {
                    "name": "Baz",
                    "price": "thirty five point four",
                },
            },
        }
    ),
    optional: int
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if optional:
        results.update({"optional": optional})
    if item:
        results.update({"item": item})
    return results


# Bodies of arbitrary dicts
@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
    print(weights)
    return weights


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', reload=True)
