import numpy as np
from llm_sdk import Small_LLM_Model


def main():
    print("Hello from maybe")
    llm = Small_LLM_Model()
    re = "la capitale de la france est?"
    ids = llm.encode(re)[0].tolist()
    for _ in range(15):
        logits = llm.get_logits_from_input_ids(ids)
        next_t = np.argmax(logits)
        ids.append(next_t)
    print(ids)
    print(llm.decode(ids))


if __name__ == "__main__":
    main()
