from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent

# Direct Ollama integration via LangChain
model = ChatOllama(model="llama3.2")

# Create a simple agent that can use tools (if provided)
agent = create_react_agent(model, tools=[])

response = agent.invoke({"messages": [("user", "Summarize the history of the internet.")]})
print(response["messages"][-1].content)