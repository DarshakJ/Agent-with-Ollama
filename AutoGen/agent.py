import autogen

# 1. Configuration for Ollama
config_list = [
    {
        "model": "llama3.2",
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama",
    }
]

# 2. The Assistant (The Brain)
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list}
)

# 3. The User Proxy (The Executor) - FIXED HERE
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        "work_dir": "coding", # Files will be saved in a folder named 'coding'
        "use_docker": False   # <--- THIS DISABLES THE DOCKER REQUIREMENT
    }
)

# 4. Start the Chat
user_proxy.initiate_chat(
    assistant, 
    message="Write a Python script to calculate the first 10 Fibonacci numbers."
)