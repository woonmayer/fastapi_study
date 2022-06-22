from fastapi import FastAPI, Response
from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordBearer

app =  FastAPI()

@app.get('/')
def read_main():
    ...

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
@app.get('/auth_needed')
def auth_needed(response: Response, token: str = Depends(oauth2_scheme)):
    ...
