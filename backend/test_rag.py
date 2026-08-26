from rag import build_context


retrieved_chunks = [
    {
        "chunk_id": "chunk_001",
        "document_id": "science_sycophantic_ai",
        "page_number": 12,
        "text": "Example retrieved passage about sycophantic AI.",
        "distance": 0.76,
    }
]

context = build_context(retrieved_chunks)

print(context)