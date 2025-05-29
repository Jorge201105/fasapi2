from typing import Union

from fastapi import FastAPI # type: ignore

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/complete")
def read_root():
    return {"Hhola": "World"}
