def shouldBuy(w, p, e):
    cond1 = p.ma_short > p.ma_long + e
    cond2 = w.phase != 'buy'
    cond3 = w.n_usd / p.current_price > w.prev_coin * w.thresh
    return cond1 & cond2 #& cond3

def shouldSell(w, p, e):
    cond1 = p.ma_short < p.ma_long - e
    cond2 = w.phase != 'sell'
    cond3 = (w.n_coin * p.current_price + w.n_usd) > (w.prev_usd + w.prev_coin * p.prev_price) * w.thresh
    return cond1 & cond2 #& cond3

def checkin(w, p):

    def enyellow(s):
        yellow = '\x1b[1;33;40m'
        ending = '\x1b[0m'
        return yellow + s + ending

    def engreen(s):
        green = '\x1b[1;32;40m'
        ending = '\x1b[0m'
        return green + s + ending

    current_value = w.n_coin * p.current_price + w.n_usd
    initial_value = (w.start_usd / p.initial_price + w.start_coin) * p.current_price

    coin_name = p.pair[:3]

    print("CHECKIN %i.  WALLET CONTAINS:" % len(p.prices))
    print(enyellow("%1.6f %s" % w.n_coin, coin_name) + " and " + engreen("%5.2f USD" % w.n_usd))
    print("CURRENT PRICE:".ljust(22, ' ') + ("%5.2f USD" % p.current_price))
    print(("CURRENT MA(%i):" % p.short_len).ljust(22, ' ') + ("%5.2f USD" % p.ma_short))
    print(("CURRENT MA(%i):" % p.long_len).ljust(22, ' ') + ("%5.2f USD" % p.ma_long))
    print("CURRENT WALLET VALUE:".ljust(22, ' ') + engreen("%5.2f USD" % current_value))
    print("IF YOU JUST BAH:".ljust(22, ' ') + ("%5.2f USD" % initial_value))
    print('')
