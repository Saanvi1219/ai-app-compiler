from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pathlib import Path

from backend.pipeline.compiler import compile_app
from backend.evaluation.evaluator import run_evaluation


app = FastAPI(
    title="Compiler Studio"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://ai-app-compiler-b5yf.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


BASE_DIR = Path(
    __file__
).resolve().parent.parent


app.mount(
    "/frontend",
    StaticFiles(
        directory=BASE_DIR/"frontend"
    ),
    name="frontend"
)


class GenerateRequest(
    BaseModel
):

    prompt:str



@app.get(
    "/",
    response_class=HTMLResponse
)
def home():

    html = (
        BASE_DIR/
        "frontend"/
        "index.html"
    ).read_text(

        encoding="utf-8"

    )


    html = html.replace(

        '/style.css',

        '/frontend/style.css'

    )


    html = html.replace(

        '/app.js',

        '/frontend/app.js'

    )


    return html




@app.post("/generate")
def generate(
    request:GenerateRequest
):

    try:

        result = compile_app(
            request.prompt
        )

        if result is None:

            return {

                "pipeline":[],

                "app":{},

                "validation":{

                    "valid":False,

                    "errors":[

                        {

                            "type":"generation_error",

                            "message":
                            "No architecture generated"

                        }

                    ]

                },

                "repair_log":[],

                "runtime":{},

                "insight":{

                    "confidence":0,

                    "chaos":100

                },

                "metrics":{

                    "success":False,

                    "latency_ms":0,

                    "retries":0,

                    "repair_count":0

                }

            }


        return result


    except Exception as e:

        return {

            "pipeline":[],

            "app":{},

            "validation":{

                "valid":False,

                "errors":[

                    {

                        "type":"server_error",

                        "message":str(e)

                    }

                ]

            },

            "repair_log":[],

            "runtime":{},

            "insight":{

                "confidence":0,

                "chaos":100

            },

            "metrics":{

                "success":False,

                "latency_ms":0,

                "retries":0,

                "repair_count":0

            }

        }




@app.get("/evaluate")
def evaluate():

    return run_evaluation()