from fastapi import FastAPI, Response
from fastapi.param_functions import Depends, Path, Query
from fastapi.security import OAuth2PasswordBearer

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
