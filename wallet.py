class Wallet:
    def __init__(self, start_usd, start_eth, thresh):
        self.start_usd = start_usd
        self.start_eth = start_eth
        self.n_usd = self.prev_usd = start_usd
        self.n_eth = self.prev_eth = start_eth
        self.thresh = thresh
        self.phase = 'sell'

    def buyCoin(self, p):
        self.phase = 'buy'
        self.prev_usd = self.n_usd

        buy_amt = (self.n_usd / p.current_price) * 0.95
        p.conn.createMarketBuyOrder(p.pair, buy_amt)
        self.n_eth = p.conn.fetchBalance()['free'][p.pair[:3]]
        self.n_usd = p.conn.fetchBalance()['free'][p.pair[-3:]]
        self.buyMessage(p.current_price)

    def sellCoin(self, p):
        self.phase = 'sell'
        self.prev_eth = self.n_eth

        sell_amt = self.n_eth * 0.95
        p.conn.createMarketSellOrder(p.pair, sell_amt)
        self.n_eth = p.conn.fetchBalance()['free'][p.pair[:3]]
        self.n_usd = p.conn.fetchBalance()['free'][p.pair[-3:]]
        self.sellMessage(p.current_price)

    def buyMessage(self, price):
        # This is a yellow background with dark text
        coloring = '\x1b[5;30;43m'
        ending = '\x1b[0m'
        buy_str = "Buying ETH.  Wallet contains %1.6f ETH (%5.2f USD)" % (self.n_eth, self.n_usd)
        summ_str = "Wallet is now worth %5.2f USD" % (self.n_eth * price + self.n_usd)
        price_str = "Price at buying: %5.2f USD" % price
        width = max(len(buy_str), len(summ_str), len(price_str))
        buy_str = buy_str.ljust(width, ' ')
        summ_str = summ_str.ljust(width, ' ')
        price_str = price_str.ljust(width, ' ')
        print(coloring + buy_str + ending + '\n' \
                + coloring + summ_str + ending + '\n' \
                + coloring + price_str + ending + '\n')

    def sellMessage(self, price):
        # This is a green background with dark text
        coloring = '\x1b[6;30;42m'
        ending = '\x1b[0m'
        sell_str = "Selling ETH. Wallet contains %5.2f USD (%1.6f ETH)" % (self.n_usd, self.n_eth)
        summ_str = "Wallet is now worth %5.2f USD" % (self.n_eth * price + self.n_usd)
        price_str = "Price at selling: %5.2f USD" % price
        width = max(len(sell_str), len(summ_str), len(price_str))
        sell_str = sell_str.ljust(width, ' ')
        summ_str = summ_str.ljust(width, ' ')
        price_str = price_str.ljust(width, ' ')
        print(coloring + sell_str + ending + '\n' \
                + coloring + summ_str + ending + '\n' \
                + coloring + price_str + ending + '\n')

    # NOTE: This is currently unused in current implementation of code, since each transaction
    # dumps all currency into the other.
    def errorMessage(self, txtype):
        # This is a red background with dark text
        coloring = '\x1b[0;30;41m'
        ending = '\x1b[0m'
        error_str = "ERROR: You attempted to %s but had insufficient funds!" % txtype
        print(coloring + error_str + ending)
