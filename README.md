# Project Ethel :older_woman:
An Ethereum trading bot that I hereby **_guarantee will lose all of your money._**

No, really.  If anyone finds this bot via Google please do not use it.  And if you do, I am not responsible for any of your losses (which will be great).

This is just a fun side project for me, to see if I can beat the market via some very, very rudimentary trading tactics.  I am by no means trained in finance, and am fully aware of the foolhardiness of my journey.

That being said, this will be an ongoing WIP, only to be finished when I become discouraged to continue by my bank account.  Below are instructions for using the bot in its current state.

# Knobs
`proto-ethel.py` is the main script to be run.  I will probably change the name of this file once I fully connect the Poloniex API to my account.  Lines 11 to 14 are the tuning parameters the user would change:

* `pair`: The currency pair to trade.  Right now I'm only playing with USD vs Ethereum, but any pair is possible.  I will make this customizable eventually.
* `SLEEP_SEC`: The number of seconds between API calls for the current price.
* `short_len`, `long_len`: The lengths of the two moving averages to use.
* `thresh`: Condition for buying.  The bot will only purchase Ethereum if you will obtain more than `thresh` times as much as you had last time.  Express as a number near 1 (ie, `1.005` is 0.5%).  Admittedly, this should probably be either a sell condition or both a buy/sell condition.  The intelligent investor would no better than me.
* `eps`: The difference in value between long and short moving average to pay attention to.  Express in dollars (ie, `0.05` is 5 cents).
* `start_usd`, `start_eth`: Starting amounts of USD and ETH to work with.
