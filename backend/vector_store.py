import faiss
import numpy as np


def build_index(embeddings: np.ndarray):
    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings.astype("float32"))

    return index


def search_index(
    index,
    query_embedding: np.ndarray,
    chunks: list[dict],
    top_k: int = 5
) -> list[dict]:

    distances, indices = index.search(
        query_embedding.astype("float32"),
        top_k
    )

    results = []

    for distance, index_position in zip(distances[0], indices[0]):
        chunk = chunks[index_position].copy()
        chunk["distance"] = float(distance)
        results.append(chunk)

    return results