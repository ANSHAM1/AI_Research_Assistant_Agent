from src.llm.prompts import research_prompt


prompt_value = research_prompt.invoke(
    {
        "message": "Explain RAG."
    }
)


print(type(prompt_value))
print(prompt_value)