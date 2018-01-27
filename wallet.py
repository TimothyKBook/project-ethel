class Wallet:
    def __init__(self, start_usd, start_eth, thresh):
        self.n_usd = self.prev_usd = start_usd
        self.n_eth = self.prev_eth = start_eth
        self.thresh = thresh
        self.phase = ''

    # TODO: Update this with the Poloniex API
    def buyCoin(self, price):
        self.phase = 'buy'
        self.prev_usd = self.n_usd
        self.n_eth += self.n_usd / price
        self.n_usd = 0
        self.buyMessage(price)

    # TODO: Update this with the Poloniex API
    def sellCoin(self, price):
        self.phase = 'sell'
        self.prev_eth = self.n_eth
        self.n_usd += self.n_eth * price
        self.n_eth = 0
        self.sellMessage(price)

    def buyMessage(self, price):
        # This is a yellow background with dark text
        coloring = '\x1b[5;30;43m'
        ending = '\x1b[0m'
        buy_str = "Buying ETH.  Wallet contains %1.6f ETH (%5.2f USD)" % (self.n_eth, self.n_usd)
        summ_str = "Wallet is now worth %5.2f USD" % (self.n_eth * price + self.n_usd)
        width = max(len(buy_str), len(summ_str))
        buy_str = buy_str.ljust(width, ' ')
        summ_str = summ_str.ljust(width, ' ')
        print(coloring + buy_str + ending + '\n' + coloring + summ_str + ending + '\n')

    def sellMessage(self, price):
        # This is a green background with dark text
        coloring = '\x1b[6;30;42m'
        ending = '\x1b[0m'
        sell_str = "Selling ETH. Wallet contains %5.2f USD (%1.6f ETH)" % (self.n_usd, self.n_eth)
        summ_str = "Wallet is now worth %5.2f USD" % (self.n_eth * price + self.n_usd)
        width = max(len(sell_str), len(summ_str))
        sell_str = sell_str.ljust(width, ' ')
        summ_str = summ_str.ljust(width, ' ')
        print(coloring + sell_str + ending + '\n' + coloring + summ_str + ending + '\n')

    # NOTE: This is currently unused in current implementation of code, since each transaction
    # dumps all currency into the other.
    def errorMessage(self, txtype):
        # This is a red background with dark text
        coloring = '\x1b[0;30;41m'
        ending = '\x1b[0m'
        error_str = "ERROR: You attempted to %s but had insufficient funds!" % txtype
        print(coloring + error_str + ending)

    def checkin(self, prices):

        def enyellow(s):
            yellow = '\x1b[5;30;43m'
            ending = '\x1b[0m'
            return yellow + s + ending

        def engreen(s):
            green = '\x1b[6;30;42m'
            ending = '\x1b[0m'
            return green + s + ending

        current_value = self.n_eth * prices.current_price + self.n_usd

        print("CHECKIN %i.  WALLET CONTAINS:" & len(prices.prices))
        print(enyellow("%1.6f ETH" % self.n_eth) + " and " + engreen("%5.2f USD" % self.n_usd))
        print("CURRENT PRICE:".ljust(21, ' ') + ("%5.2f USD" % prices.current_price))
        print("CURRENT SHORT MA:".ljust(21, ' ') + ("%5.2f USD" % prices.short_ma))
        print("CURRENT LONG MA:".ljust(21, ' ') + ("%5.2f USD" % prices.long_ma))
        print("CURRENT WALLET VALUE:".ljust(21, ' ') + ("%5.2f USD" % current_value))
        print('')

    def shouldBuy(self, prices, e):
        cond1 = prices.ma_short > prices.ma_long + e
        cond2 = self.phase != 'buy'
        cond3 = self.n_usd / prices.current_price > self.prev_eth * self.thresh
        return cond1 & cond2 & cond3

    def shouldSell(self, prices, e):
        cond1 = prices.ma_short > prices.ma_long - e
        cond2 = self.phase != 'sell'
        cond3 = self.n_eth * prices.current_price > self.prev_usd
        return cond1 & cond2 & cond3

