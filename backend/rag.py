def build_context(retrieved_chunks: list[dict]) -> str:
    evidence = []

    for i, chunk in enumerate(retrieved_chunks, start=1):
        evidence.append(
            f"[Source S{i}]\n"
            f"Document: {chunk['document_id']}\n"
            f"Page: {chunk['page_number']}\n"
            f"Chunk: {chunk['chunk_id']}\n"
            f"Text:\n{chunk['text']}"
        )

    return "\n\n".join(evidence)