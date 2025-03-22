# **AI-Powered Multi-Agent System Using Agno Framework** 🚀  

## **Overview**  
This project implements an **AI-powered multi-agent system** using the **Agno framework**, integrating different LLM providers like **OpenAI** and **Groq**. It also enables **real-time web search**, **financial data retrieval**, and **knowledge-based reasoning** through **LLM + tool integration**.  

The system consists of multiple AI agents with specialized tasks, such as:  
✅ **Web Agent** – Fetches real-time search results using **DuckDuckGo**.  
✅ **Finance Agent** – Retrieves stock prices and market insights from **Yahoo Finance**.  
✅ **Memory Agent** – Enhances knowledge retrieval using **vector databases & semantic search**.  

Together, these agents enable a **more intelligent and up-to-date AI system**, overcoming **LLM knowledge cutoffs** by combining **pre-trained knowledge with real-time updates**.  

---

## **1️⃣ Agent Components**  

### **🔹 AI-Powered Web Search Agent (`agent.py`)**  
This agent allows the AI system to **fetch real-time data** using **DuckDuckGo search**. Since LLMs have a **knowledge cutoff**, they **cannot access post-training information**, making real-time search critical for **breaking news, stock updates, and live events**.  

#### **Key Features:**  
- **Overcomes LLM limitations** by retrieving the latest information.  
- **Uses DuckDuckGo for real-time search** (e.g., stock prices, sports results, breaking news).  
- **Combines LLM reasoning with live updates** for more accurate responses.  

#### **How It Works:**  
1. **User Query:** `"What is Tesla's stock price today?"`  
2. **LLM Determines:** Need for real-time data.  
3. **DuckDuckGo Fetches:** The latest stock price.  
4. **LLM Processes:** Summarizes and presents it in a structured format.  

#### **Example Use Cases:**  
✔ **Live sports results:** `"Who won the India vs New Zealand finals in CT 2025?"`  
✔ **Stock market updates:** `"What’s NVIDIA's stock price today?"`  
✔ **Breaking news:** `"What were the key announcements in the latest Apple event?"`  
✔ **Weather forecasts:** `"What’s the weather in New York right now?"`  

---

### **🔹 Multi-Agent Financial & Market Analysis (`multi_agents.py`)**  
This Python script creates a **multi-agent system** that combines:  
✔ **Web Agent for real-time news & stock market trends**  
✔ **Finance Agent for stock prices, fundamentals, and recommendations**  

By combining these **specialized agents**, the system can provide:  
- **Data-driven investment recommendations**  
- **Live market trends + AI-powered financial insights**  
- **Structured reports with sources & tables**  

#### **Key Features:**  
- **Multi-Agent Collaboration:** Each agent specializes in a specific task.  
- **Combines LLM + Real-Time Search:** Overcomes knowledge cutoffs.  
- **Financial Analysis + Market News:** Helps in investment decisions.  
- **Structured Responses:** Uses tables and sources for clarity.  

#### **Example Use Case:**  
📌 **User Query:** *"Analyze Tesla, NVIDIA, and Apple and suggest which stock is best for long-term investment."*  
1. **Web Agent fetches recent financial news** from DuckDuckGo.  
2. **Finance Agent retrieves stock prices, fundamentals, and analyst recommendations.**  
3. **LLM processes the data** and provides a structured investment recommendation.  

🚀 **Outcome:** A **detailed investment report** with **real-time data + AI reasoning.**  

---

### **🔹 AI Memory & Knowledge Retrieval (`agent_memory.py`)**  
This agent **enhances AI knowledge retrieval** using **two key components**:  
1. **Knowledge Base** – Stores structured documents (e.g., PDFs, articles).  
2. **Vector Database** – Enables **semantic search** (meaning-based retrieval).  

#### **Key Differences:**  

| Feature                  | Knowledge Base | Vector Database |
|--------------------------|---------------|----------------|
| **Works Like**           | Wikipedia     | Google Photos (face search) |
| **Retrieves**            | Exact matches | Similar concepts |
| **Example**              | `"Chicken soup recipe"` → Finds exact text | `"Warm broth dish with poultry"` → Finds similar recipes |
| **Use Case**             | Structured text storage | AI-powered similarity search |

🚀 **Final Summary:**  
- **A knowledge base** stores and retrieves structured data.  
- **A vector database** enables **semantic search** based on meaning.  
- **Combining both** allows AI to **retrieve both exact & similar matches** for better accuracy.  

#### **Example Use Case:**  
📌 **Query:** *"Find me a traditional Thai soup recipe."*  
1. **Knowledge Base Check:** If an exact recipe exists, return it.  
2. **Vector Database Check:** If no exact match, search for **similar recipes** based on meaning.  
3. **LLM Summarizes:** Presents the best results with **detailed instructions**.  

🚀 **Result:** AI **retrieves, understands, and suggests** recipes intelligently.  

---

## 2️⃣ Future Enhancements to be done

🚀 **Expand Multi-Agent Capabilities** – Add agents for **healthcare, law, and cybersecurity**.  
📊 **Enhanced Data Visualization** – Use **charts & graphs** for better financial insights.  
🤖 **Automated Portfolio Management** – AI-powered **investment strategies**.  

---

## 3️⃣ Conclusion  

This project showcases how **multi-agent AI systems** can:  
✅ **Combine LLM reasoning with real-time search** for accurate insights.  
✅ **Retrieve structured financial data + AI analysis** for investment decisions.  
✅ **Enhance knowledge retrieval** using **vector databases & semantic search**.  

🚀 **Empowering AI with real-time intelligence!**  
