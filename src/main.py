from swarm import Agent, Swarm
from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

client = Swarm()
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
context_variables = {"task": "Make me rich"}

def transfer_to_research_agent():
    return researcher

def do_research(query=context_variables["task"]):
    result= tavily_client.get_search_context(query)
    print(result)
    return result

def get_instructions():
    task = context_variables["task"]
    return f"""
        You are the Director Agent of the COMPASS system. Your role is to:
        1. Analyze the given goal: {task}
        2. Break it down into logical sub-tasks
        3. Determine which specialist agents to involve
        4. Create a clear execution plan
        5. Monitor and adjust the plan as needed

        Respond with:
        Intructions for the researcher agent to work with.
    """
    
director = Agent(
    name="Director",
    instructions=get_instructions(),
    functions=[get_instructions, transfer_to_research_agent]    
)

researcher = Agent(
    name="Researcher",
        instructions="""
            You are the Research Agent of the COMPASS system.
            1. List key information needed
            2. Identify reliable sources
            3. Gather and cross-reference information
            4. Organize findings by relevance
            5. Rate confidence (1-5) for each finding
            6. Flag uncertainties or gaps

            Format findings as:
            - Topic:
            - Key Findings:
            - Sources:
            - Confidence:
            - Gaps:
            - Select one side hustle to start with
            - Provide a detailed plan of action
        """,
    functions=[do_research]
)

response = client.run(
    agent=director,
    messages=[{"role": "user", "content": "I would like to become rich"}],
    context_variables=context_variables
)

print(response.messages[-1]["content"])



