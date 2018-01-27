import sys
import numpy as np
from poloniex import Poloniex
import time, datetime

from wallet import Wallet
from prices import Prices
from emailer import Emailer
from utilities import shouldBuy, shouldSell, checkin

# .gitignored file that contains the two strings used in line 26
import secrets

conn = Poloniex()
pair = "USDT_ETH"
SLEEP_SEC = 30
short_len = 5
long_len  = 20
thresh    = 1.005
eps       = 0.05
start_usd = 1000
start_eth = 0

w = Wallet(start_usd, start_eth, thresh)
prices = Prices(conn, pair, short_len, long_len)
em = Emailer(secrets.myaddress, secrets.mypassword)

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
        w.buyCoin(prices.current_price)
        em.buyEmail(w, prices)

    if shouldSell(w, prices, eps):
        w.sellCoin(prices.current_price)
        em.sellEmail(w, prices)

    time.sleep(SLEEP_SEC)


