from openai import AsyncOpenAI
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

# 1. Create the base OpenAI client configured for Ollama
# Ollama's OpenAI-compatible endpoint is /v1
ollama_client = AsyncOpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama'
)

# 2. Wrap that client in a Provider
# The provider is what 'OpenAIChatModel' now expects
ollama_provider = OpenAIProvider(openai_client=ollama_client)

# 3. Initialize the model using the signature you found
model = OpenAIChatModel(
    model_name='llama3.2',
    provider=ollama_provider
)

# 4. Create and run your agent
agent = Agent(model=model, system_prompt='You are a concise summarizer.')

if __name__ == "__main__":
    result = agent.run_sync('Explain why to use agents over traditional ML')
    print("--- Agent Response ---")
    print(result)