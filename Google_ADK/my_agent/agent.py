from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm # Corrected importr


# Mock tool implementation
def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city."""
    return {"status": "success", "city": city, "time": "10:30 AM"}

# 1. Define the Ollama Model connection
# "ollama_chat/" ensures the ADK uses the chat-completion API for better tool handling
ollama_model = LiteLlm(model="ollama_chat/llama3.2")

# 2. Update your Agent
root_agent = Agent(
    model=ollama_model,  # Pass the LiteLlm object here
    name='root_agent',
    description="Tells the current time in a specified city.",
    instruction="You are a helpful assistant that tells the current time in cities. Use the 'get_current_time' tool.",
    tools=[get_current_time],
)