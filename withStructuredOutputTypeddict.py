from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated
load_dotenv()

model = ChatOpenAI()
# simple TypedDict
class Review(TypedDict):
    summary : Annotated[str,"A brief summary of the review"]
    sentiment : Annotated[str,"Return Sentiment of the review either negative,positive or neutral"]

structuredModel = model.with_structured_output(Review)

res = structuredModel.invoke("""The hardware is great,but the software feels bloated.There are too many preinstalled apps that i can't remove.Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.""")
print(res)
print(res['summary'])
print(res['sentiment'])
