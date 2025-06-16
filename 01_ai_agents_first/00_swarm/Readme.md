# 🤖 Exploring Agentic AI with OpenAI Agents SDK

This project explores the core ideas of **Agentic AI**, focusing on how multiple AI agents can collaborate to accomplish complex tasks efficiently. The foundation of this exploration comes from OpenAI’s **Swarm framework** and its evolution into the **Agents SDK**, designed for orchestrating multi-agent systems in real-world applications.

---

## 🚀 What is OpenAI Swarm?

**Swarm** is an experimental framework created by OpenAI to coordinate **multiple lightweight AI agents**. It introduces two main concepts:

- **Agents**: Independent AI workers assigned to specific tasks.
- **Handoffs**: A mechanism that lets agents transfer control to each other when needed.

> Example: In a customer service bot, one agent handles billing, another handles tech issues, and they "handoff" the conversation based on the user's query type.

Swarm makes multi-agent systems simple, scalable, and easy to test.

---

## 🧠 What is the Agents SDK?

The **Agents SDK** is a production-ready evolution of the Swarm framework. It enhances agent coordination, workflow orchestration, and real-world applicability.

### ✅ Key Features:
- Define agents with specific goals or tools
- Handoff tasks between agents intelligently
- Orchestrate complex multi-step workflows
- Trace, debug, and scale the system smoothly

---

## 🧩 Anthropic’s Agent Design Patterns (Implemented via Agents SDK)

OpenAI’s Agents SDK supports several agent design patterns proposed by Anthropic for efficient system architecture:

| Pattern               | Description | Real-world Example |
|----------------------|-------------|--------------------|
| **Prompt Chaining**  | Break down complex tasks into smaller steps | Recipe bot: One agent finds recipe, another creates a shopping list |
| **Routing**          | Direct task to the right agent based on its nature | A language assistant sends Urdu translation tasks to Urdu agent |
| **Parallelization**  | Run multiple subtasks simultaneously | One agent fetches data, another draws graphs, and one writes summary |
| **Orchestrator-Worker** | A manager agent assigns subtasks to others | Orchestrator assigns intro, body, and conclusion writing to 3 agents |
| **Evaluator-Optimizer** | Agents review each other’s work and suggest improvements | A quality checker agent refines answers by giving feedback |

These patterns make your AI agent system smarter, faster, and more modular.

---

## 🔧 Technologies Used

- OpenAI Agents SDK
- Async Python (asyncio)
- Environment config via `dotenv`
- Gemini API (via OpenAI-compatible endpoint)

---

## 📌 Conclusion

This project shows how **Agentic AI** can be practically built using OpenAI’s modern tools and proven design patterns. With Swarm's simplicity and the SDK's power, we can now build collaborative agent systems for real-world, production-level applications.

---

## 📫 Contact

- **Name**: Moiz Ahmed  
- **LinkedIn**: [Moiz Ahmed](https://www.linkedin.com/in/moiz-ahmed905/)  
- **Email**: moizaman905@gmail.com

