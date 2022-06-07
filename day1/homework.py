import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/send_me_queries/")
def dynamic_query_params(request: Request):
    return request.query_params


if __name__ == '__main__':
    uvicorn.run('homework:app', reload=True)
