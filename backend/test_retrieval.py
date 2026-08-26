from embedder import embed_chunks, embed_text
from chunker import chunk_pages
from pdf_processor import extract_pages
from vector_store import build_index, search_index


pages = extract_pages(
    "science.aec8352_sm (1).pdf",
    "science_sycophantic_ai"
)

chunks = chunk_pages(pages)
embeddings = embed_chunks(chunks)
index = build_index(embeddings)

query = "What does the paper say about sycophantic AI and dependence?"
query_embedding = embed_text(query)

results = search_index(
    index,
    query_embedding,
    chunks,
    top_k=5
)

for result in results:
    print(f"Page {result['page_number']}")
    print(f"Distance: {result['distance']:.4f}")
    print(result["text"][:500])
    print("---")