from crewai import Task
from agents.analyst_agent import analyst_agent

get_stock_analysis = Task(
    description=(
        "Analyze the recent performance of the stock: {stock}. Use the live stock information to retrieve "
        "current price, percentage change, trading volume, and other market data. Provide a summary of how the stock "
        "is performing today and highlighting any key observation from the data."
    ),
    expected_output=(
        "A clear,bullet-pointed summary of:\n"
        "-Current stock price\n"
        "-Daily price change and percentage\n"
        "-Volume and volatility\n"
        "-Any intermediate trends or observations\n"
    ),
    agent=analyst_agent
)
