from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
  ChatPromptTemplate,
  SystemMessagePromptTemplate,
  HumanMessagePromptTemplate,
)

# setup an instance of the OpenAI language model
chat = ChatOpenAI(model_name="gpt-4-vision-preview", temperature=0.5)

template = "You are an assistant that helps users find information."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = "{question}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages(
  [system_message_prompt, human_message_prompt])


def getResponse(prompt):
  response = chat(chat_prompt.format_prompt(question=prompt).to_messages())
  return response
