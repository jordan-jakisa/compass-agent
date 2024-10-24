from swarm import Agent, Swarm
from tavily import TavilyClient


client = Swarm()
tavily_client = TavilyClient(api_key=)
def transfer_to_research_agent():
    return researcher

def do_research(query):
    return tavily_client.get_search_context(query)

director = Agent(
    name="Director",
    instructions="""
            You are the Director Agent of the COMPASS system. Your role is to:
            1. Analyze the given goal: {goal}
            2. Break it down into logical sub-tasks
            3. Determine which specialist agents to involve
            4. Create a clear execution plan
            5. Monitor and adjust the plan as needed

            Respond with:
            1. Goal analysis
            2. Sub-tasks identified
            3. Agent assignments
            4. Execution sequence
            5. Success criteria
            """,
    functions=[transfer_to_research_agent]    
)

researcher = Agent(
    name="Researcher",
        instructions="""
            You are the Research Agent of the COMPASS system. For the task: {task}
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
        """,
    functions=[do_research()]
)



