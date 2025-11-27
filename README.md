
****AI Bus Trip Planner – ADK Capstone Project****

This project demonstrates an AI-powered bus trip planner agent, created for the Kaggle Capstone Project using the Agent Development Kit (ADK). The agent helps users plan bus journeys from home to college (and back), with features like interactive memory, custom trip scheduling, and dynamic tool invocation.
 
**Key capabilities:**
- Remembers your home, college, and preferred departure time (via memory tool).
- Recommends the best bus based on your request and the latest timetable.
- Allows both direct and natural language queries.
 
---


*Example Conversations*

```
Set user profile (memory)
response = await bus_runner.run_debug(
    "My home is Home, my college is College, and I usually leave at 08:30."
)
print(response[-1])

Plan a trip using your saved preferences
response = await bus_runner.run_debug(
    "Plan my usual morning trip."
)
print(response[-1])
```
The agent will reply with a bus recommendation using its internal tools and memory.


***Implementation***

*This project uses Google’s Agent Development Kit (ADK) with a Gemini model to build a function-calling agent that can read a small in-notebook bus timetable and call custom Python tools. Four core tools are implemented: one to fetch bus options, one to estimate travel time, and two to store and retrieve the user profile (home, college, default departure time). An LlmAgent is configured with instructions to use these tools, and an InMemoryRunner manages the conversation flow so that natural language prompts are transformed into tool calls and final responses.*


***Why this project***

*Many students and commuters rely on fixed bus routes between home and college but do not have an easy way to check the best option for a specific time each day. Timetables are often static, hard to read, and require manual scanning, which is slow and error-prone during busy mornings. An AI agent that understands natural language and remembers personal preferences can make this daily planning faster, more accurate, and more accessible for all age groups.*


***Benefits***

Personalized experience: The agent remembers the user’s home, college, and preferred departure time, so repeated queries become shorter and more natural.

Faster decisions: Instead of scanning tables, users simply ask questions like “Plan my usual morning trip,” and immediately see the recommended bus.

Extensible design: The same architecture can scale to real-time bus APIs or city-wide routes, making it suitable as a starting point for a production transit assistant.


***Conclusion***

*The AI Bus Trip Planner demonstrates how an agent with memory and function tools can solve a focused, real‑world problem: daily bus trip planning between fixed locations. By remembering a user’s usual home and college stops, along with their preferred departure time, the agent reduces repetitive input and makes the experience feel more like talking to a personal assistant than working with a traditional timetable.*

*Although the current prototype relies on a small, static schedule and simple rule-based logic, its architecture is deliberately designed to be extensible. The same pattern of tools and state can be connected to live transit APIs, GPS feeds, and richer user profiles to support dynamic routes, real-time delays, and multiple cities or institutions.*
 
*This project therefore serves as a compact but complete example of how conversational agents can wrap complex transport data in a friendly interface. With further development such as error handling, multilingual support, and integration into mobile or kiosk interfaces—the Bus Trip Planner could evolve from a classroom prototype into a practical assistant for everyday commuters.*


---
