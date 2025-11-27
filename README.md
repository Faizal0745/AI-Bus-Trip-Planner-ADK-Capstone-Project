🚌 AI Bus Trip Planner (ADK Agent)
A smart AI agent that helps students plan daily bus trips between home and college using Google’s Agent Development Kit (ADK) and Gemini. The agent understands natural language, remembers your usual stops and departure time, and suggests suitable buses from a timetable.

✨ Features
Remembers home stop, college stop, and preferred departure time using agent memory.​

Suggests buses based on origin, destination, and time using custom tools.​

Supports conversational queries like “Plan my usual morning trip” instead of rigid inputs.​

Simple, extensible architecture that can later connect to live transit data.​

🧠 Tech Stack
LLM: Gemini (via Google Generative AI) wrapped by ADK.​

Framework: Google Agent Development Kit (ADK) – LlmAgent, function tools, in‑memory runner.​

Environment: Python 3, Jupyter/Kaggle Notebook.

🧩 Agent Design
Tools
get_bus_options(from_stop, to_stop, after_time)
Returns all buses on the given route departing at or after the specified time from an in‑notebook timetable.

estimate_travel_time(from_stop, to_stop)
Estimates travel duration (e.g., 40 minutes from Home ↔ College).

set_user_profile(home, college, default_departure)
Saves the user’s typical route and departure time in a simple in‑memory profile.

get_user_profile()
Retrieves the stored profile so the agent can answer “Plan my usual morning trip.”

Agent
The LlmAgent is configured with instructions telling it how and when to call each tool, so it can:

Parse natural language queries into concrete tool calls.

Use profile tools for personalization.

Combine timetable lookup with travel‑time estimates in one reply.​

🚀 Getting Started
Prerequisites
Kaggle or Jupyter environment with Python 3.

A Google Generative AI API key stored as GOOGLE_API_KEY in Kaggle secrets (or environment variable).

Setup
python
from google.genai import types
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner

import os
from kaggle_secrets import UserSecretsClient

# Authentication
GOOGLE_API_KEY = UserSecretsClient().get_secret("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

# Retry config
retry_config = types.HttpRetryOptions(
    attempts=5,
    exp_base=7,
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],
)
Define your timetable, tools, agent, and runner (as already done in your notebook).

💻 Usage Examples
python
# 1. Set user profile (memory)
response = await bus_runner.run_debug(
    "My home is Home, my college is College, and I usually leave at 08:30."
)
print("Agent:", response[-1])

# 2. Plan trip using stored profile
response = await bus_runner.run_debug("Plan my usual morning trip.")
print("Agent:", response[-1])

# 3. Direct trip request
response = await bus_runner.run_debug(
    "I want to go from Home to College after 08:45."
)
print("Agent:", response[-1])
📈 Why This Matters
Public transport users often rely on static timetables and guesswork when choosing a bus, especially for routine commutes. By wrapping schedule data in an AI agent with memory, this project shows how everyday planning tasks can become faster and more user‑friendly while keeping the implementation compact and explainable.​

🔮 Future Work
Integrate live city bus APIs for real‑time departures and delays.

Add more stops, multiple routes, and multi‑hop journeys.

Improve robustness to typos and informal language.

Explore multilingual prompts and localized responses for different regions.​
