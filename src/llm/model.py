from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.output_parsers import StrOutputParser

from src.config import settings
# from src.llm.prompts import research_prompt


llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=settings.GOOGLE_API_KEY,
    temperature=0,
)


# output_parser = StrOutputParser()

# LCEL = LangChain Expression Language
# research_chain = research_prompt | llm | output_parser


# def generate_response(message: str) -> str:
#     return research_chain.invoke(
#         {
#             "message": message,
#         }
#     )


# def generate_response(message: str) -> str:
#     prompt_value = research_prompt.invoke(
#         {
#             "message": message,
#         }
#     )

#     response = llm.invoke(prompt_value)

#     answer = output_parser.invoke(response)

#     return answer