from langchain_community.llms import Ollama

llm = Ollama(model="openchat")
query = "Which is the purpose of life?"

output = llm.invoke(query)
print(output)
