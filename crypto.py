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

def find_all_coin_prices():
    # Load the Coin Market Cap exchange
    coinmarketcap = ccxt.coinmarketcap()

    # Load the market for Coin Market Cap
    markets = coinmarketcap.load_markets()

    for symbol in markets:
        # Only check USD coins
        if (symbol[-3:] == 'USD'):
            price = str(markets[symbol]['info']['price_usd'])
            print(symbol + ' : ' + price)

symbol_price('VEN/USD')