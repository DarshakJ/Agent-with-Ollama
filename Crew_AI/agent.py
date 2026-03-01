from crewai import Agent, Task, Crew, LLM

# Configure Llama 3.2 via Ollama
local_llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434"
)

researcher = Agent(
    role='Researcher',
    goal='Summarize the latest AI trends',
    backstory='A meticulous analyst.',
    llm=local_llm
)

task = Task(description="Write a summary of how AI is transitioning.", agent=researcher, expected_output="A summary.")

crew = Crew(agents=[researcher], tasks=[task])
print(crew.kickoff())