import numpy as np

class Prices:
    def __init__(self, conn, pair, short_len, long_len):
        self.prices = []
        self.conn = conn
        self.pair = pair
        self.current_price = None
        self.prev_price = None
        self.ma_short = None
        self.ma_long = None
        self.short_len = short_len
        self.long_len = long_len
        self.initial_price = float(self.conn.fetchTicker(self.pair)['last'])

    def addCurrentPrice(self):
        self.prev_price = self.current_price
        self.current_price = float(self.conn.fetchTicker(self.pair)['last'])
        self.prices.append(self.current_price)

    def updateMA(self):
        self.ma_short = np.mean(self.prices[-self.short_len:])
        self.ma_long = np.mean(self.prices[-self.long_len:])
