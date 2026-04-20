import yfinance as yf

def buscar_preco_atual(ticker: str) -> float:
  Ticker = yf.Ticker(ticker)
  info = Ticker.info
  current_price = info.get('currentPrice') or info.get('regularMarketPrice')

  if current_price is None:
    raise ValueError(f"Não foi possível obter o preço atual para o ticker {ticker}")

  return current_price
