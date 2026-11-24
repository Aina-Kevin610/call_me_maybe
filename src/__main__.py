import numpy as np
from typing import Any
import sys
from llm_sdk import Small_LLM_Model
from .parser import parser
from pprint import pprint


def read(prompt: str, llm: Small_LLM_Model) -> list[int]:
    tokens = list(llm.encode(prompt)[0])
    for _ in range (20):
        logits = np.array(llm.get_logits_from_input_ids(tokens))
        best_tokens = np.argmax(logits)
        tokens.append(best_tokens)
    return tokens

def output(filename: str, content: list[dict[str, Any]]) -> None:
    with open(filename, 'w') as f:
        f.write(str(content))


def main():
    result = ""
    prompt, definition = parser(sys.argv[4], sys.argv[2])

    llm = Small_LLM_Model()

    pprint(definition)
    # output("output", result)

    

if __name__ == "__main__":
    main()
