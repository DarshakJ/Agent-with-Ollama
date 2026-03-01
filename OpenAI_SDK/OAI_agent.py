from openai import OpenAI

# 1. Initialize the client to point to Ollama's local server
# Ollama's OpenAI-compatible endpoint is /v1
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # Required by the SDK, but ignored by Ollama
)

def summarization_agent(text_to_summarize):
    """
    An agent that takes a long text and returns a concise summary 
    using the Llama 3.2 model.
    """
    try:
        response = client.chat.completions.create(
            model="llama3.2",
            messages=[
                {
                    "role": "system", 
                    "content": "You are a professional research assistant. Your task is to provide a concise, bulleted summary of the provided text."
                },
                {
                    "role": "user", 
                    "content": f"Please summarize the following text:\n\n{text_to_summarize}"
                }
            ],
            temperature=0.3, # Lower temperature for more focused summaries
        )
        
        return response.choices[0].message.content

    except Exception as e:
        return f"An error occurred: {e}"

# --- Example Usage ---
if __name__ == "__main__":
    sample_text = """
    Artificial intelligence (AI) is intelligence demonstrated by machines, 
    as opposed to natural intelligence displayed by animals including humans. 
    AI research has been defined as the field of study of intelligent agents, 
    which refers to any system that perceives its environment and takes actions 
    that maximize its chance of achieving its goals.
    """
    
    print("--- Summary Agent Output ---")
    summary = summarization_agent(sample_text)
    print(summary)