# kucoin_scalp_trading_bot_using_ccxt
This python script automatically buys and sells orders and checks any open orders before making another order. You can set the premium you want to take from each trade and I purposely. Feel free to add to it. It includes code to use it on the sandbox or live.

**This script uses a single file called v6script.py

Creator: Cody Krecicki https://instagram.com/ckrecicki

To use this script, you need to first have the ccxt library installed. To do this, you can use the following command:


pip install ccxt
Once the library is installed, you can import it in your script using the following line of code:


import ccxt
After importing the ccxt library, you need to instantiate the Exchange class by using the name of the exchange you want to use. In this case, the exchange name is kucoin. To instantiate the Exchange class, you can use the getattr function and pass in the ccxt module and the exchange name as arguments:


exchange = getattr(ccxt, exchange_name)()
Once you have instantiated the Exchange class, you need to set the sandbox mode to True or False depending on whether you want to use the sandbox or live environment. To do this, you can use the set_sandbox_mode method and pass in the enabled parameter with a value of True or False:


exchange.set_sandbox_mode(enabled=True)
Next, you need to set your API keys for the exchange. The script uses the apiKey, secret, and password properties to set the API keys. You can set these properties by assigning your API keys to them:


exchange.apiKey = 'public-key'
exchange.secret = 'private-key'
exchange.password = 'password'
After setting the API keys, you need to set the symbol you want to trade on the exchange. To do this, you can simply assign the symbol to a variable:


symbol = 'BTC/USDT'
Next, you need to set the amount of BTC you want to trade. This value should be assigned to a variable:


amount = 0.1
The script then enters an infinite loop in which it continuously trades on the exchange. In each iteration of the loop, it first fetches the current ticker information for the symbol using the fetch_ticker method:


ticker = exchange.fetch_ticker(symbol)
Next, it checks the current bid and ask prices for the symbol by accessing the bid and ask properties of the ticker object:


bid = ticker['bid']
ask = ticker['ask']
The script then calculates the midpoint of the bid and ask prices by adding them together and dividing by two:


midpoint = (bid + ask) / 2
It also sets a premium for the sell order. This value is used to calculate the price at which the sell order will be placed:


premium = 0.003
The script then checks if there are any open orders on the exchange using the fetch_open_orders method:


open_orders = exchange.fetch_open_orders(symbol)
If there are no open orders, the script places a limit buy order at the midpoint price using the create_order method. This method takes in several parameters, including the symbol, order type, side, amount, and price:


order_id = exchange.create_order(symbol, 'limit', 'buy', amount, midpoint)
After placing the buy order, the script pauses for a few seconds and then checks the status of the open orders again using the fetch_open_orders method. If there are still no open orders, the script places a limit sell order at the midpoint price plus the premium using the create_order method:


order_id = exchange.create_order(symbol, 'limit', 'sell', amount, midpoint * (1 + premium))
The script then pauses for a few seconds and checks the status of the open orders again. This process is repeated indefinitely until the script is stopped.

To run this script, you would need to save it as a Python file and then run it using the following command:


python script.py
Replace script.py with the name of your Python file. This will start the script and it will begin trading on the exchange using the settings you specified.

It is important to note that this script is for illustration purposes only and is not intended for real-world use. Trading on cryptocurrency exchanges involves significant risk, and you should always carefully consider your risk tolerance and trade with caution. Additionally, the code in this script has not been tested and may contain errors or bugs. It is recommended that you thoroughly test and debug the code before using it in a live environment.

Furthermore, the API keys and other sensitive information used in this script are fictional and should not be used in any real-world application. You should always use your own API keys and handle them with care to prevent unauthorized access to your funds.

In summary, to use this script, you need to:

1) Install the ccxt library using the pip install ccxt command.

2) Import the ccxt library and the sleep function from the time module in your Python file.

3) Instantiate the Exchange class using the getattr function and the name of the exchange you want to use.

4) Set the sandbox mode to True or False using the set_sandbox_mode method.

5) Set your API keys using the apiKey, secret, and password properties.

6) Set the symbol you want to trade on the exchange.

7) Set the amount of BTC you want to trade.

8) Enter an infinite loop and continuously trade on the exchange by placing buy and sell orders at the midpoint price.

9) Save the script as a Python file and run it using the python3 v6script.py command.
