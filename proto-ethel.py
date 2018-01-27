import sys
import numpy as np
from poloniex import Poloniex
import time, datetime

from wallet import Wallet
from prices import Prices
from utilities import shouldBuy, shouldSell, checkin

conn = Poloniex()
pair = "USDT_ETH"
SLEEP_SEC = 1
short_len = 2
long_len  = 4
thresh    = 1.005
eps       = 0.05
start_usd = 1000
start_eth = 0

w = Wallet(start_usd, start_eth, thresh = thresh)
prices = Prices(conn, pair, short_len, long_len)

while True:
    if len(prices.prices) < prices.long_len:
        print("%i: Warming up..." % len(prices.prices))
        prices.addCurrentPrice()
        time.sleep(SLEEP_SEC)
        continue

    prices.addCurrentPrice()
    prices.updateMA()

    if len(prices.prices) % 5 == 0:
        checkin(w, prices)

    if shouldBuy(w, prices, eps):
        w.buyCoin(prices.current_price)

    if shouldSell(w, prices, eps):
        w.sellCoin(prices.current_price)

    time.sleep(SLEEP_SEC)


