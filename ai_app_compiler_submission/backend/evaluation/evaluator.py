
import json
from pathlib import Path
from collections import Counter

from backend.pipeline.compiler import compile_app


def run_evaluation():

    file_path = (
        Path(__file__).parent /
        "prompts.json"
    )

    with open(
        file_path,
        "r"
    ) as file:

        dataset = json.load(file)


    prompts = (

        dataset["normal_prompts"]

        +

        dataset["edge_case_prompts"]

    )


    results = []

    success = 0

    total_latency = 0

    total_retries = 0

    failure_types=[]


    for prompt in prompts:


        result = compile_app(
            prompt
        )


        metrics=result["metrics"]


        results.append({

            "prompt":prompt,

            "success":
            metrics["success"],

            "latency_ms":
            metrics["latency_ms"],

            "repair_count":
            metrics["repair_count"]

        })


        if metrics["success"]:

            success+=1


        else:

            errors=(
                result
                .get(
                    "validation",
                    {}
                )
                .get(
                    "errors",
                    []
                )
            )


            for error in errors:

                failure_types.append(

                    error["type"]

                )


        total_latency += (
            metrics["latency_ms"]
        )


        total_retries += (
            metrics["retries"]
        )



    total = len(prompts)


    return {

        "total_prompts":
        total,


        "success_rate":
        round(
            (success/total)*100,
            2
        ),


        "average_latency_ms":
        round(
            total_latency/total,
            2
        ),


        "average_retries":
        round(
            total_retries/total,
            2
        ),


        "failure_distribution":

        dict(
            Counter(
                failure_types
            )
        ),


        "results":
        results

    }

