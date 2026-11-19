import ast
from typing import Any


POSSIBLE_TYPE = ["bool", "int", "float", "double", "string", "number"]


def check_type(data: dict[str, Any]) -> None:
    if data["returns"]["type"].lower() not in POSSIBLE_TYPE:
        raise TypeError(f"return value of {data["name"]} is not correct")
    param = data["parameters"]
    for key, value in param.items():
        if value["type"].lower() not in POSSIBLE_TYPE:
            raise TypeError(f"[{data["name"]}] '{key}' type not valid")

def parser(calling: str, definition: str) -> list[dict[str]] | list[dict[str]]:
    with open(calling, 'r') as c:
        prompt = ast.literal_eval(c.read())

    with open(definition, 'r') as d:
        definition = ast.literal_eval(d.read())

    try:
        for type in definition:
            check_type(type)
    except TypeError as e:
        print("ERROR - ", e)

    return prompt, definition