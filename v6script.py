# Import the ccxt library and the sleep function from the time module
import ccxt
from time import sleep

# Replace EXCHANGE_NAME with the name of the exchange you want to use
exchange_name = 'kucoin'

# Instantiate the Exchange class
exchange = getattr(ccxt, exchange_name)()

# Set sandbox mode to True or False
exchange.set_sandbox_mode(enabled=True)

# Set your API keys
exchange.apiKey = '6394cb0641a5330001d216ca'
exchange.secret = '1765824e-d358-475c-9b54-d383f7f54b45'
exchange.password = 'meowmeow'

# Set the symbol you want to trade on Kucoin
symbol = 'BTC/USDT'

# Set the amount of BTC you want to trade
amount = .1

# Create an infinite loop to trade continuously
while True:
    # Fetch the current ticker information for the symbol
    ticker = exchange.fetch_ticker(symbol)

    # Check the current bid and ask prices
    bid = ticker['bid']
    ask = ticker['ask']

    # Calculate the midpoint of the bid and ask prices
    midpoint = (bid + ask) / 2

    # Set the premium for the sell order
    premium = 0.003

    # Check if there are any open orders
    open_orders = exchange.fetch_open_orders(symbol)
    if not open_orders:
        # Place a limit buy order at the midpoint price
        order_id = exchange.create_order(symbol, 'limit', 'buy', amount, midpoint)

    # Pause for a few seconds and check the status of the open orders
    sleep(5)
    open_orders = exchange.fetch_open_orders(symbol)

    # Check if there are any open orders
    if not open_orders:
        # Place a limit sell order at the midpoint price plus the premium
        order_id = exchange.create_order(symbol, 'limit', 'sell', amount, midpoint * (1 + premium))

    # Pause for a few seconds and check the status of the open orders
    sleep(5)
    open_orders = exchange.fetch_open_orders(symbol)
