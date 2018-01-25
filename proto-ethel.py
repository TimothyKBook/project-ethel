import sys
import numpy as np
from poloniex import Poloniex
import time, datetime

pol = Poloniex()
pair = "USDT_ETH"
SLEEP_SEC = 30
short_ave = 10
long_ave  = 50

w = {"n_usd" : 1000,
     "n_eth" : 0,
     "prev_usd" : 1000,
     "prev_eth" : 0}

phase = ''
thresh = 1.02
prices = []

eps = 1

def getPrice(pair = pair, conn = pol):
    return float(conn.returnTicker()[pair]['last'])

def shouldBuy(w, p, th):
    should_buy = w['n_usd'] / p > w['prev_eth'] * thresh
    return(should_buy)

def shouldSell(w, p, th):
    should_sell = w['n_eth'] * p > w['prev_usd'] * thresh
    return(should_sell)

def buyMessage(w, p):
    coloring = '\x1b[5;30;43m'
    ending = '\x1b[0m'
    buy_str = "Buying ETH.  Wallet contains %1.8f ETH (%5.2f USD)" % (w['n_eth'], w['n_usd'])
    print(coloring + buy_str + ending + '\n')

def sellMessage(w, p):
    coloring = '\x1b[6;30;42m'
    ending = '\x1b[0m'
    sell_str = "Selling ETH. Wallet contains %5.2f USD (%1.8f ETH)" % (w['n_usd'], w['n_eth'])
    print(coloring + sell_str + ending + '\n')

while True:

   curr_price = getPrice()

   if len(prices) < long_ave:
       print("%i: Warming up..." % len(prices))
       prices.append(curr_price)
       time.sleep(SLEEP_SEC)
       continue

   ma_short = np.mean(prices[-short_ave:])
   ma_long = np.mean(prices[-long_ave:])
   prices.append(curr_price)

   if len(prices) % 20 == 0:
       print("CHECKIN %i: %1.8f ETH --- %5.2f USD" % (len(prices), w['n_eth'], w['n_usd']))
       print("CURRENT PRICE       : %5.2f USD" % curr_price)
       print("CURRENT SHORT MA    : %5.2f USD" % ma_short)
       print("CURRENT LONG  MA    : %5.2f USD" % ma_long)
       print("CURRENT WALLET VALUE: %5.2f USD" % (w['n_eth'] * curr_price + w['n_usd']))
       print('\n')

   if (ma_short > ma_long + eps) & (phase != 'buy') & shouldBuy(w, curr_price, thresh):
        phase = 'buy'
        w['prev_usd'] = w['n_usd']
        w['n_eth'] += w['n_usd'] / curr_price
        w['n_usd'] = 0
        buyMessage(w, curr_price)
   
   if (ma_short < ma_long - eps) & (phase != 'sell') & shouldSell(w, curr_price, thresh):
       phase = 'sell'
       w['prev_eth'] = w['n_eth']
       w['n_usd'] += w['n_eth'] * curr_price
       w['n_eth'] = 0
       sellMessage(w, curr_price)

   time.sleep(SLEEP_SEC)


