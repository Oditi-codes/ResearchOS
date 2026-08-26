def chunk_pages(
    pages: list[dict],
    chunk_size: int = 1000,
    overlap: int = 200
) -> list[dict]:

    chunks = []

    for page in pages:
        text = page["text"]
        start = 0
        chunk_number = 0

        while start < len(text):
            end = start + chunk_size

            chunks.append({
                "chunk_id": f'{page["document_id"]}_p{page["page_number"]}_c{chunk_number}',
                "document_id": page["document_id"],
                "page_number": page["page_number"],
                "text": text[start:end]
            })

            chunk_number += 1
            start += chunk_size - overlap

    return chunks