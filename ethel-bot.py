import sys
import ccxt
import time, datetime

from wallet import Wallet
from prices import Prices
from emailer import Emailer
from utilities import shouldBuy, shouldSell, checkin

# .gitignored file that contains API keys, email address and password
import secrets

SLEEP_SEC = 15
short_len = 5
long_len  = 30
eps       = 0.005
use_email = False
phase     = 'buy'

if len(sys.argv) > 1:
    pair = sys.argv[1].upper() + "/USD"
else:
    pair = "ETH/USD"

conn = ccxt.kraken({
        "apiKey" : secrets.publickey,
        "secret" : secrets.privatekey
})

start_usd = conn.fetchBalance()['free'][pair[-3:]]
start_coin = conn.fetchBalance()['free'][pair[:3]]

w = Wallet(start_usd, start_coin, phase)
prices = Prices(conn, pair, short_len, long_len)
if use_email: em = Emailer(secrets.myaddress, secrets.mypassword)

while True:
    if len(prices.prices) < prices.long_len:
        print("%i: Warming up..." % len(prices.prices))
        prices.addCurrentPrice()
        time.sleep(SLEEP_SEC)
        continue

    prices.addCurrentPrice()
    prices.updateMA()

    if len(prices.prices) % 20 == 0:
        checkin(w, prices)

    if shouldBuy(w, prices, eps):
        w.buyCoin(prices)
        if use_email: em.buyEmail(w, prices)

    if shouldSell(w, prices, eps):
        w.sellCoin(prices)
        if use_email: em.sellEmail(w, prices)

    time.sleep(SLEEP_SEC)


