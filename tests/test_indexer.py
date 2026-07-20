from src.rag.indexer import index_pdf


def main():

    index_pdf(
        "data/pdfs/sample.pdf"
    )


if __name__ == "__main__":
    main()