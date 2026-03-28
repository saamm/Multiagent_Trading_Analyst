import yfinance as yf
from crewai.tools import tool

@tool("Live Stock Information Tool")
def get_stock_price(stock_symbol: str) -> str:
    """
    Retrieves the latest stock price and other relevant info for a given stock symbol using Yahoo Finance
    Parameters:
       stock_symbol (str) : The ticker symbol of the stock (e.g. AAPI, TSLA, MSFT)
    Returns:
        str: A summary of the stock's current price, daily change, and other key data
    """

    stock = yf.Ticker(stock_symbol)
    info = stock.info

    current_price = info.get("regularMarketPrice")
    change = info.get("regularMarketChange")
    change_percent = info.get("regularMarketChangePercent")
    currency = info.get("currency", "USD")

    volume = info.get("regularMarketVolume")
    avg_volume = info.get("averageVolume")

    day_high = info.get("dayHigh")
    day_low = info.get("dayLow")

    if day_high and day_low:
        volatility = round(((day_high - day_low) / current_price) * 100, 2)
    else:
        volatility = None

    if current_price is None:
        return f"Could not fetch price for {stock_symbol}. Please check the symbol"

    return (
        f"Stock: {stock_symbol.upper()}\n"
        f"Price: {current_price} {currency}\n"
        f"Price: {change} ({round(change_percent,2)}%)"
        f"Volume: {volume}\n"
        f"Avg Volume: {avg_volume}\n"
        f"Volatility (approx): {volatility}%"
    )

#print(get_stock_price("AAPL"))
