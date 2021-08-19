from typing import Optional

from fastapi import FastAPI
from blindtex import tex2all
from pydantic import BaseModel

class LatexExpression(BaseModel):
    expression: str

app = FastAPI()

@app.get("/")
def read_root():
    return {"Bienvenido a Blindtex. Para más información http://blindtex.org/"}

@app.post("/readLatexExpression/")
async def read_equation(eq: LatexExpression):
    tranformation=tex2all.read_equation(eq.expression)
    return tranformation