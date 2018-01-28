def shouldBuy(w, p, e):
    cond1 = p.ma_short > p.ma_long + e
    cond2 = w.phase != 'buy'
    cond3 = w.n_usd / p.current_price > w.prev_eth * w.thresh
    return cond1 & cond2 & cond3

def shouldSell(w, p, e):
    cond1 = p.ma_short > p.ma_long - e
    cond2 = w.phase != 'sell'
    cond3 = w.n_eth * p.current_price > w.prev_usd * w.thresh
    return cond1 & cond2 & cond3

def checkin(w, p):

    def enyellow(s):
        yellow = '\x1b[5;30;43m'
        ending = '\x1b[0m'
        return yellow + s + ending

    def engreen(s):
        green = '\x1b[6;30;42m'
        ending = '\x1b[0m'
        return green + s + ending

    current_value = w.n_eth * p.current_price + w.n_usd
    initial_value = (w.start_usd / p.initial_price + w.start_eth) * p.current_price

    print("CHECKIN %i.  WALLET CONTAINS:" % len(p.prices))
    print(enyellow("%1.6f ETH" % w.n_eth) + " and " + engreen("%5.2f USD" % w.n_usd))
    print("CURRENT PRICE:".ljust(21, ' ') + ("%5.2f USD" % p.current_price))
    print("CURRENT SHORT MA:".ljust(21, ' ') + ("%5.2f USD" % p.ma_short))
    print("CURRENT LONG MA:".ljust(21, ' ') + ("%5.2f USD" % p.ma_long))
    print("CURRENT WALLET VALUE:".ljust(21, ' ') + ("%5.2f USD" % current_value))
    print("IF YOU JUST BAH:".ljust(21, ' ') + ("%5.2f USD" % initial_value))
    print('')
