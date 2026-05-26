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

    failure_types = []


    for prompt in prompts:


        result = compile_app(
            prompt
        )


        # prevent crash if compile_app returns None
        if result is None:

            results.append({

                "prompt": prompt,

                "success": False,

                "latency_ms": 0,

                "repair_count": 0

            })

            continue


        metrics = result.get(
            "metrics",
            {}
        )


        results.append({

            "prompt": prompt,

            "success":
            metrics.get(
                "success",
                False
            ),

            "latency_ms":
            metrics.get(
                "latency_ms",
                0
            ),

            "repair_count":
            metrics.get(
                "repair_count",
                0
            )

        })


        if metrics.get(
            "success",
            False
        ):

            success += 1


        else:

            errors = (
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

                if isinstance(
                    error,
                    dict
                ):

                    failure_types.append(

                        error.get(
                            "type",
                            "unknown"
                        )

                    )


        total_latency += (
            metrics.get(
                "latency_ms",
                0
            )
        )


        total_retries += (
            metrics.get(
                "retries",
                0
            )
        )


    total = len(prompts)


    return {

        "total_prompts":
        total,


        "success_rate":
        round(
            (success / total) * 100,
            2
        ),


        "average_latency_ms":
        round(
            total_latency / total,
            2
        ),


        "average_retries":
        round(
            total_retries / total,
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