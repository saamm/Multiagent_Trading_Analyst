# 💹 Multi-Agent Stock Trading System (CrewAI)

A simple multi-agent system built using **CrewAI** that analyzes stock data and generates trading decisions using real-time market information.

---

## 🚀 Overview

This project simulates a **collaborative AI trading workflow** using two specialized agents:

* **📊 Analyst Agent** → Gathers and interprets live stock data
* **📈 Trader Agent** → Makes Buy/Sell/Hold decisions based on analysis

The system uses real-time stock data via **Yahoo Finance** and processes it through a structured agent pipeline.

---

## 🧠 How It Works

1. User provides a stock name (e.g., `TSLA`)
2. The **Analyst Agent**:
   * Fetches live stock data (price, change, volume, etc.)
   * Summarizes key insights
3. The **Trader Agent**:
   * Uses the analysis
   * Outputs a trading decision:
     * ✅ Buy
     * ❌ Sell
     * 🤝 Hold
    
---

## 🧩 Tech Stack

* **CrewAI** → Multi-agent orchestration
* **LiteLLM / Groq** → LLM backend
* **yfinance** → Real-time stock data
* **Python** → Core implementation

---

## 🏗️ Project Structure

```
Crew_AI_multi_agents/
│
├── agents/
│   ├── analyst_agent.py
│   └── trader_agent.py
│
├── tasks/
│   ├── analyse_task.py
│   └── trader_task.py
│
├── tools/
│   └── stock_research_tool.py
│
├── crew.py
├── main.py
├── requirements.txt
└── .env
```

---

## 🔧 Features

* Multi-agent collaboration using CrewAI
* Real-time stock data via Yahoo Finance (`yfinance`)
* Modular architecture (agents, tasks, tools separation)
* Extensible for more financial indicators or strategies

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd Crew_AI_multi_agents
```

### 2. Create virtual environment (Python 3.12 recommended)

```bash
py -3.12 -m venv venv
.\venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Usage

Run the system:

```bash
python main.py
```

Default example (to be input inside main.py):

```python
run("TESLA")
```

---

## 🧪 Example Output

```
Stock: TSLA
Price: 245.32 USD
Change: +3.45 (1.43%)

Recommendation: BUY
Reason:
- Strong upward momentum
- Positive daily change
- High trading volume
```

---

## 📌 Future Improvements

* Add technical indicators (RSI, MACD, moving averages)
* Introduce risk management agent
* Backtesting on historical data
* Multi-stock portfolio optimization
* Add memory between agents

---

## 📄 License

This project is for educational and experimental purposes.
