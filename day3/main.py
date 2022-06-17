import uvicorn
from fastapi import FastAPI, Depends

app = FastAPI()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get('/items/')
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


@app.get('/users/')
async def read_users(commons: dict = Depends(common_parameters)):
    return commons


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', reload=True)
