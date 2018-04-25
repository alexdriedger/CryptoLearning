import ccxt

def symbol_price(symbol):

    # Load the Coin Market Cap exchange
    coinmarketcap = ccxt.coinmarketcap()

    # Load the market for Coin Market Cap
    markets = coinmarketcap.load_markets()

    # Get the price of bitcoin
    price = markets[symbol]['info']['price_usd']

    # Print it out
    print(symbol + ' : ' + price)

symbol_price('BTC/USD')
symbol_price('VEN/USD')
