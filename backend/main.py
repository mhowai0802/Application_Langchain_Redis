from langchain.memory import RedisChatMessageHistory
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_ollama.llms import OllamaLLM
import os



# Example conversation
response = conversation.predict(input="Hi! My name is Alice.")
print(response)

# Messages persist in Redis even after restarting the program
response = conversation.predict(input="What's my name?")
print(response)