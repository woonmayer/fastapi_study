from fastapi import FastAPI, Response
from fastapi.param_functions import Depends, Path, Query
from fastapi.security import OAuth2PasswordBearer
from pydantic.main import BaseModel

app =  FastAPI()

@app.get('/')
def read_main():
    ...

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
@app.get('/auth_needed')
def auth_needed(response: Response, token: str = Depends(oauth2_scheme)):
    ...

@app.get('/path_param/{path_param}')
def echo_path_param(path_param: str = Path()):
    return path_param


@app.get('/query_param')
def echo_query_param(q = Query()):
    return {'q': q}


class Product(BaseModel):
    name: str
    code: str


class Option(BaseModel):
    name: str

@app.post('/product')
def create_product(product: Product, option: Option | None = None):
    return product, option

