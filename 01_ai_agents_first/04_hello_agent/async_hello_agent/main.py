

import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
import asyncio

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

config = RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True
)

async def main():

    agent = Agent(
        name= "English Teacher",
        instructions= "you are a best English Teacher in the world",
        model= model
    )

    prompt = input("how can i Help you? ")

    result = await Runner.run(agent, prompt, run_config= config)
    print(result.final_output)
    

if __name__ == "__main__":
    asyncio.run(main())
