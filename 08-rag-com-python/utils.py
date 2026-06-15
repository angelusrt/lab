import os
import numpy as np
import google.generativeai as genai
import typing

EMBEDDING_MODEL = "models/gemini-embedding-001"
GENERATION_MODEL = "gemini-2.5-flash"

def init():
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])


def _embed_texts(texts: list[str]) -> np.ndarray:
    result = genai.embed_content(
        model=EMBEDDING_MODEL,
        content=texts,
        task_type="retrieval_document",
    )

    return np.array(result["embedding"])

def retrieve(query: str, docs:list[str], top_k: int = 2) -> list[str]:
    doc_embeddings = _embed_texts(docs)

    query_embedding = genai.embed_content(
        model=EMBEDDING_MODEL,
        content=query,
        task_type="retrieval_query",
    )["embedding"]

    query_vec = np.array(query_embedding)

    scores = doc_embeddings @ query_vec / (
        np.linalg.norm(doc_embeddings, axis=1) * np.linalg.norm(query_vec)
    )

    top_indices = np.argsort(scores)[::-1][:top_k]

    return [docs[i] for i in top_indices]

def answer(query: str, context_chunks: list[str], prompt_builder: typing.Callable[[str, str], str]) -> str:
    context = "\n".join(f"- {chunk}" for chunk in context_chunks)

    prompt = prompt_builder(context, query)
    model = genai.GenerativeModel(GENERATION_MODEL)
    response = model.generate_content(
        prompt, 
        generation_config=genai.GenerationConfig(temperature=0)
    )

    return response.text

