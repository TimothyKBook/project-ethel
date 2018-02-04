# :older_woman: Project Ethel :older_woman:
An Ethereum trading bot that I hereby **_guarantee will lose all of your money._**

No, really.  If anyone finds this bot via Google please do not use it.  And if you do, I am not responsible for any of your losses (which will be great).

This is just a fun side project for me, to see if I can beat the market via some very, very rudimentary trading tactics.  I am by no means trained in finance, and am fully aware of the foolhardiness of my journey.

That being said, this will be an ongoing WIP, only to be finished when I become discouraged to continue by my bank account.  Below are instructions for using the bot in its current state.

# Secrets
**_IMPORTANT!_**:  This bot will not work as-is.  I am using the Kraken exchange using the `ccxt` API.  In order for the bot to function, you must create a `secrets.py` file with these two lines:
```py
publickey = "YOUR_PUBLIC_KEY"
privatekey = "YOUR_PRIVATE_KEY"
```

You should also include the following two lines if you wish to use the emailer:
```py
myaddress = "YOUR_ADDRESS@gmail.com"
mypassword = "YOUR_GMAIL_PASSWORD"
```

# Knobs
`ethel-bot.py` is the main script to be run.  Tuning parameters are on line 13-19

* `pair`: The currency pair to trade.  Defaults to Ethereum (ETH).  Future updates will allow this to change from the command line.
* `SLEEP_SEC`: The number of seconds between API calls for the current price.
* `short_len`, `long_len`: The lengths of the two moving averages to use.
* `eps`: The percent change at which you are willing to buy/sell.  This should of course be higher than your fees.  Treat as percent, ie, `0.005` is interpretted as "0.5%".
* `use_email`: Whether or not to use emailer.  Right now, I don't think the email utility I'm using works on AWS.
* `phase`:  The initial phase to start in.

# Bonus
I also have the Python/shell script named `query` to quickly query your balance in between log outputs.  This script requires one non-case-sensitive argument: the currency abbreviation.  Example: Simply type `./query eth`.

# TODOs

* Read a finance book and maybe learn how to trade more.
* Allow for knob chaning on command line.
* ????
* Profit!
