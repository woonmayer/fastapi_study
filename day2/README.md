# FastAPI tutorial for study

- requirements
  - Python 3.10
    - `brew install python@3.10`
  - poetry
    - `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`

```bash
poetry env use /opt/homebrew/opt/python@3.10/bin/python3
poetry install
poetry build

docker build . -t day2
docker run -p 8000:8000 day2
```
