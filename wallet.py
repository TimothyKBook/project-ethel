class Wallet:
    def __init__(self, start_usd, start_coin, self.phase):
        self.start_usd = self.n_usd = start_usd
        self.start_coin = self.n_coin = start_coin
        self.phase = self.phase
        self.prev_buy = 0
        self.prev_sell = 1e10

    def buyCoin(self, p):
        self.phase = 'buy'
        self.prev_usd = self.n_usd
        self.prev_buy = p.current_price

        buy_amt = (self.n_usd / p.current_price) * 0.98
        p.conn.createMarketBuyOrder(p.pair, buy_amt)

        bal = p.conn.fetchBalance()['free']
        self.n_coin = bal[p.pair[:3]]
        self.n_usd = bal[p.pair[-3:]]
        self.buyMessage(p)

    def sellCoin(self, p):
        self.phase = 'sell'
        self.prev_coin = self.n_coin
        self.prev_sell = p.current_price

        sell_amt = self.n_coin * 0.98
        p.conn.createMarketSellOrder(p.pair, sell_amt)

        bal = p.conn.fetchBalance()['free']
        self.n_coin = bal[p.pair[:3]]
        self.n_usd = bal[p.pair[-3:]]
        self.sellMessage(p)

    def buyMessage(self, p):
        coloring = '\x1b[1;33;40m'
        ending = '\x1b[0m'

        price = p.current_price
        coin_name = p.pair[:3]

        buy_str = "Buying %s.  Wallet contains %1.6f %s (%5.2f USD)" % (coin_name, self.n_coin, coin_name, self.n_usd)
        summ_str = "Wallet is now worth %5.2f USD" % (self.n_coin * price + self.n_usd)
        price_str = "Price at buying: %5.2f USD" % price
        width = max(len(buy_str), len(summ_str), len(price_str))
        buy_str = buy_str.ljust(width, ' ')
        summ_str = summ_str.ljust(width, ' ')
        price_str = price_str.ljust(width, ' ')
        print(coloring + buy_str + ending + '\n' \
                + coloring + summ_str + ending + '\n' \
                + coloring + price_str + ending + '\n')

    def sellMessage(self, p):
        coloring = '\x1b[1;32;40m'
        ending = '\x1b[0m'

        price = p.current_price
        coin_name = p.pair[:3]

        sell_str = "Selling %s. Wallet contains %5.2f USD (%1.6f %s)" % (coin_name, self.n_usd, self.n_coin, coin_name)
        summ_str = "Wallet is now worth %5.2f USD" % (self.n_coin * price + self.n_usd)
        price_str = "Price at selling: %5.2f USD" % price
        width = max(len(sell_str), len(summ_str), len(price_str))
        sell_str = sell_str.ljust(width, ' ')
        summ_str = summ_str.ljust(width, ' ')
        price_str = price_str.ljust(width, ' ')
        print(coloring + sell_str + ending + '\n' \
                + coloring + summ_str + ending + '\n' \
                + coloring + price_str + ending + '\n')
