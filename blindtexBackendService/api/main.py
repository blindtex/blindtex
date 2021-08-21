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

@app.post("/readLatexExpression/", response_model=LatexExpression)
async def read_equation(eq: LatexExpression):
    convertion = {}
    convertion['expression'] = tex2all.read_equation(eq.expression)
    return convertion