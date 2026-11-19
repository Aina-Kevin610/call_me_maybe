import numpy as np
import ast
import sys
from llm_sdk import Small_LLM_Model


def parser(calling: str, definition: str) -> list[dict[str]] | list[dict[str]]:
    with open(calling, 'r') as c:
        prompt = ast.literal_eval(c.read())

    with open(definition, 'r') as d:
        definition = ast.literal_eval(d.read())

    return prompt, definition


def main():
    prompt, definition = parser(sys.argv[4], sys.argv[2])


if __name__ == "__main__":
    main()
