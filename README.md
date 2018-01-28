# :older_woman: Project Ethel :older_woman:
An Ethereum trading bot that I hereby **_guarantee will lose all of your money._**

No, really.  If anyone finds this bot via Google please do not use it.  And if you do, I am not responsible for any of your losses (which will be great).

This is just a fun side project for me, to see if I can beat the market via some very, very rudimentary trading tactics.  I am by no means trained in finance, and am fully aware of the foolhardiness of my journey.

That being said, this will be an ongoing WIP, only to be finished when I become discouraged to continue by my bank account.  Below are instructions for using the bot in its current state.

# Secrets
**_IMPORTANT!_**:  This bot will not work as-is.  I am using the Kraken exchange using the `ccxt` API.  In order for the bot to function, you must create a `secrets.py` file with exactly two lines:
```py
publickey = "YOUR_PUBLIC_KEY"
privatekey = "YOUR_PRIVATE_KEY"
```

# Knobs
`proto-ethel.py` is the main script to be run.  I will probably change the name of this file once I fully connect the Poloniex API to my account.  Lines 11 to 14 are the tuning parameters the user would change:

* `pair`: The currency pair to trade.  Right now I'm only playing with USD vs Ethereum, but any pair is possible.  If you use another pair, be aware that the logging will still say "ETH".  I'll change this eventually.  Maybe.
* `SLEEP_SEC`: The number of seconds between API calls for the current price.
* `short_len`, `long_len`: The lengths of the two moving averages to use.
* `thresh`: Condition for buying and selling.  The bot will only sell Ethereum if you will obtain more than `thresh` times as much USD as you had last time.  Same as for buying.  Express as a number near 1 (ie, `1.005` is 0.5%).
* `eps`: The difference in value between long and short moving average to pay attention to.  Express in dollars (ie, `0.05` is 5 cents).

# TODOs

* Read a finance book and maybe learn how to trade more.
* Change printing mechanisms to allow any choice of currency pair.
* ????
* Profit!
