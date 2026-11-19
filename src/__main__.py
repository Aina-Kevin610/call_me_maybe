import numpy as np
from llm_sdk import Small_LLM_Model


def main():
    llm = Small_LLM_Model()
    prompt = "repond avec un fichier json contenant [name, description, parametres(avec ses type en dict)], voici la question [What is the sum of 2 and 3?]"
    ids = llm.encode(prompt)[0].tolist()
    for _ in range(150):
        logits = llm.get_logits_from_input_ids(ids)
        next_t = np.argmax(logits)
        ids.append(next_t)
    print(llm.decode(ids))


if __name__ == "__main__":
    main()
