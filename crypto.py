import ccxt

# Load the Coin Market Cap exchange
coinmarketcap = ccxt.coinmarketcap()

# Load the market for Coin Market Cap
markets = coinmarketcap.load_markets()

# Get the price of bitcoin
price = markets['BTC/USD']['info']['price_usd']

# Print it out
print(price)

