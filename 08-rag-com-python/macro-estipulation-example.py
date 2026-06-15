import utils

docs = [
    """
    Dia 14-06-2026:

    - 150g de sanduíche de frango, ovo e requeijão + 1 xícara de café com leite
    - [1h academia]
    - 547g de arroz, feijão e salada + 200g de frango
    - 1 scoop de proteína
    - 600g lasanha de carne
    """,
]

template = """
Responda minhas solicitações de nutrição usando APENAS o formato:
proteína: x, gordura: x, carboidrato: x, caloria: x

Sem explicações, sem itens individuais, apenas o total diário em uma linha.

Contexto:\n{}\n
Pergunta:\n{}
"""

if __name__ == "__main__":
    query = "Estipule minhas macros do dia 14 de junho."

    utils.init()
    relevant_chunks = utils.retrieve(query, docs)

    print(f"Question:\n{query}\n")

    print("Retrieved chunks:\n")
    for chunk in relevant_chunks:
        print(f"  → {chunk}")

    answer = utils.answer(
        query, 
        relevant_chunks,
        lambda a, b: template.format(a, b)
    )

    print(f"Answer:\n{answer}\n")
