from openai import OpenAI , AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, function_tool

#from agents.tracing import set_tracing_disabled

#set_tracing_disabled(True)

@function_tool
def get_weather(city: str) -> str:
    """Get weather for a given city"""
    return f"It's always sunny in {city}"
    
local_model = OpenAIChatCompletionsModel(
    model="minimax-m2.7:cloud",
    openai_client=AsyncOpenAI(
        api_key="ollama",
        base_url="http://localhost:11434/v1"
    )
)

history_agent = Agent(
    name="History Tutor",
    instructions="You answer history questions clearly, concisely",
    model=local_model,
    tools=[get_weather]
)

#query = "Who built badshahi masjid in lahore pakistan"
query = "What is weather in Lahore"
result = Runner.run_sync(history_agent, query)


print(result.final_output)

