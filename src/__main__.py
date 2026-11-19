import numpy as np
import sys
from llm_sdk import Small_LLM_Model
from .parser import parser


def main():
    prompt, definition = parser(sys.argv[4], sys.argv[2])


if __name__ == "__main__":
    main()
