from src.rag.chain import generate_answer


def main():

    print("-" * 60)

    while True:

        question = input("\nYou : ")

        if question.lower() in {"exit", "quit"}:
            break

        answer = generate_answer(
            question=question
        )

        print(f"\nAI : {answer}")


if __name__ == "__main__":
    main()