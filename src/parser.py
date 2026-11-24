import ast
import sys
from typing import Any


POSSIBLE_TYPE = ["bool", "int", "float", "double", "string", "number"]
POSSIBLE_KEY = ["name", "description", "parameters", "returns"]


def check_type(data: dict[str, Any]) -> None:
    """function that check type of data if it's valid or not

    Args:
        data (dict[str, Any]): data to check

    Raises:
        TypeError: in case of the return value is invalid
        TypeError: in case of the parameters value is invalid

    """
    param = data["parameters"]
    for key, value in param.items():
        if "type" not in [key.lower() for key in value.keys()] or len(value) != 1:
            raise TypeError(f"[{data["name"]}] key '{key}' not valid")
    for key, value in param.items():
        if value["type"].lower() not in POSSIBLE_TYPE:
            raise TypeError(f"[{data["name"]}] '{key}:{value}' type not valid")
    if data["returns"]["type"].lower() not in POSSIBLE_TYPE:
            raise TypeError(f"return value of {data["name"]} is not correct")


def parser(calling: str, definition: str) -> list[dict[str]] | list[dict[str]]:
    """function that parse a json file (definition, call test) for the LLM

    Args:
        calling (str): path to the calling.json file
        definition (str): path to the definition.json file

    Returns:
        list[dict[str]] | list[dict[str]]: 2 parsed files, call and definition file
    """
    with open(calling, 'r') as c:
        prompt = ast.literal_eval(c.read())

    with open(definition, 'r') as d:
        definition = ast.literal_eval(d.read())

    try:
        for type in definition:
            check_type(type)
            if len(type) != 4:
                raise TypeError("json not valid (lenght)")
            if set(POSSIBLE_KEY) != set([key for key in type.keys()]):
                raise TypeError(f"json not valid (key)")
    except TypeError as e:
        print("ERROR - ", e)
        sys.exit(1)

    return prompt, definition