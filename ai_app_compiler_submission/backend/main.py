from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from pathlib import Path

from backend.pipeline.compiler import compile_app
from backend.evaluation.evaluator import run_evaluation

app = FastAPI(
    title="Compiler Studio"
)

BASE_DIR=Path(__file__).resolve().parent.parent

app.mount(
    "/frontend",
    StaticFiles(directory=BASE_DIR/"frontend"),
    name="frontend"
)

class GenerateRequest(BaseModel):
    prompt:str


@app.get("/",response_class=HTMLResponse)
def home():

    html=(BASE_DIR/"frontend"/"index.html").read_text(
        encoding="utf-8"
    )

    html=html.replace(
        '/style.css',
        '/frontend/style.css'
    )

    html=html.replace(
        '/app.js',
        '/frontend/app.js'
    )

    return html



@app.post("/generate")
def generate(
request:GenerateRequest
):

    return compile_app(
        request.prompt
    )



@app.get("/evaluate")
def evaluate():

    return run_evaluation()