# -*- coding: utf-8 -*-
"""
MCP - Kaggle Competition Search Agent
-------------------------------------
This script integrates Google ADK with Kaggle MCP to query Kaggle datasets
and competitions programmatically. It uses Gemini as the LLM and MCP tools
to fetch structured results (name, url, description, rating).
"""

import os
from kaggle_secrets import UserSecretsClient

# 🔑 Authentication: load Google API key from Kaggle secrets
try:
    GOOGLE_API_KEY = UserSecretsClient().get_secret("GOOGLE_API_KEY")
    os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
    print("✅ Setup and authentication complete.")
except Exception as e:
    print(f"🔑 Authentication Error: Please add 'GOOGLE_API_KEY' to Kaggle secrets. Details: {e}")

# 📦 Imports: ADK components and MCP integration
from google.genai import types
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

print("✅ ADK components imported successfully.")

# 🔄 Retry config: handle transient HTTP errors gracefully
retry_config = types.HttpRetryOptions(
    attempts=5,
    exp_base=7,
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],
)

# 🔗 MCP integration with Kaggle via npx
KAGGLE_MCP_TOOL = McpToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command="npx",
            args=["-y", "mcp-remote", "https://www.kaggle.com/mcp"]
        ),
        timeout=60,  # increased timeout for stability
    )
)

print("✅ MCP Tool created")

# 🧠 Agent instructions: enforce structured JSON output
instruction = """
You are a Kaggle Dataset and Competition Search Agent.
Responsibilities:
- Search Kaggle datasets and competitions using MCP tools.
- Focus only on datasets relevant to the user’s query (e.g., OCR).
- Rank results by popularity and rating.

Output format:
Return a JSON array of up to 3 items, each with:
{
  "name": "Dataset name",
  "url": "Full Kaggle dataset URL (https://www.kaggle.com/...)",
  "description": "1–2 sentence summary",
  "rating": "Community rating or votes"
}

Constraints:
- Always include the full Kaggle dataset URL.
- Keep summaries concise.
- Exclude unrelated datasets.
- If fewer than 3 datasets match, return only those available.
- If none are found, return {"error": "No relevant datasets found"}.
"""

# 🤖 Define the search agent
search_agent = LlmAgent(
    name="search_agent",
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    instruction=instruction,
    tools=[KAGGLE_MCP_TOOL],
    output_key="top_3_competitions",
)

# 🏃 Runner executes the agent in-memory
runner = InMemoryRunner(agent=search_agent)

# 🔎 Query Kaggle datasets (OCR example)
async def main():
    response = await runner.run(
        "List 3 highly rated Kaggle datasets that contain OCR (Optical Character Recognition) data"
    )
    print("📊 Results:")
    print(response)

# ✅ Run safely in Kaggle (no asyncio.run, just await)
import asyncio
asyncio.get_event_loop().run_until_complete(main())
