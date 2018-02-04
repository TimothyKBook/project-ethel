#!python

import ccxt
import secrets
import sys

conn = ccxt.kraken({
        "apiKey" : secrets.publickey,
        "secret" : secrets.privatekey
})

coin_name = sys.argv[1].upper()
pair = coin_name + "/USD"

def greentext(s):
    coloring = '\x1b[1;32;40m'
    ending = '\x1b[0m'
    return coloring + s + ending

def yellowtext(s):
    coloring = '\x1b[1;33;40m'
    ending = '\x1b[0m'
    return coloring + s + ending

def greenbg(s):
    coloring = '\x1b[6;30;42m'
    ending = '\x1b[0m'
    return coloring + s + ending

curr_balance = conn.fetchBalance()['free']
curr_usd = curr_balance['USD']
curr_coin = curr_balance[coin_name]
curr_price = conn.fetchTicker(pair)['last']
curr_value = curr_usd + curr_coin*curr_price

print('')
print("CHECKING IN!  Currently, your wallet holds:")
print(greentext("%5.2f USD").ljust(12, ' ') % curr_usd)
print(yellowtext("%1.6f %s").ljust(12, ' ') % (curr_coin, coin_name))
print('')
print("TOTAL WALLET VALUE:")
print(greenbg("%5.2f USD") % curr_value)
print('')
print("CURRENT PRICE:")
print("%5.2f USD" % curr_price)
