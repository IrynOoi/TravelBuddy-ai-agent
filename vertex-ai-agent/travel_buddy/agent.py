from google.adk.agents import LlmAgent
from google.adk.tools import agent_tool
from google.adk.tools.google_search_tool import GoogleSearchTool
from google.adk.tools import url_context
from google.adk.tools import VertexAiSearchTool

travel_buddy_agent_google_search_agent = LlmAgent(
  name='TravelBuddy_Agent_google_search_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in performing Google searches.'
  ),
  sub_agents=[],
  instruction='Use the GoogleSearchTool to find information on the web.',
  tools=[
    GoogleSearchTool()
  ],
)
travel_buddy_agent_url_context_agent = LlmAgent(
  name='TravelBuddy_Agent_url_context_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in fetching content from URLs.'
  ),
  sub_agents=[],
  instruction='Use the UrlContextTool to retrieve content from provided URLs.',
  tools=[
    url_context
  ],
)
travel_buddy_agent_vertex_ai_search_agent = LlmAgent(
  name='TravelBuddy_Agent_vertex_ai_search_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in performing Vertex AI Search.'
  ),
  sub_agents=[],
  instruction='Use the VertexAISearchTool to find information using Vertex AI Search.',
  tools=[
    VertexAiSearchTool(
      data_store_id='projects/vertex-ai-agent-488710/locations/global/collections/default_collection/dataStores/malaysia-travel-store_1772191172256'
    )
  ],
)
root_agent = LlmAgent(
  name='TravelBuddy_Agent',
  model='gemini-2.5-flash',
  description=(
      'Help customers answer travel related queries'
  ),
  sub_agents=[],
  instruction='Greet the user warmly and ask about their travel interests.\n\n- Use the \'Alternative Location\' tool if a user asks about a place that doesn\'t exist (like Wakanda).\n\n- Provide concise, helpful itineraries based on the user\'s budget.',
  tools=[
    agent_tool.AgentTool(agent=travel_buddy_agent_google_search_agent),
    agent_tool.AgentTool(agent=travel_buddy_agent_url_context_agent),
    agent_tool.AgentTool(agent=travel_buddy_agent_vertex_ai_search_agent)
  ],
)
