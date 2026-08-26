import pymupdf


def extract_pages(pdf_path: str, document_id: str) -> list[dict]:
    with pymupdf.open(pdf_path) as document:
        pages = []

        for page_number, page in enumerate(document, start=1):
            pages.append({
                "document_id": document_id,
                "page_number": page_number,
                "text": page.get_text()
            })

    return pages