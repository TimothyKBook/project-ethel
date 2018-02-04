import smtplib

class Emailer:
    def __init__(self, address, password):
        self.address = address
        self.password = password

        # Set up connection
        self.conn = smtplib.SMTP("smtp.gmail.com", 587)
        self.conn.ehlo()
        self.conn.starttls()
        self.conn.login(address, password)

    def buyEmail(self, w, p):
        coin_name = p.pair[:3]

        subj_line = "Subject: Ethel just bought %s\n" % coin_name
        line1 = "%s price at purchase: $%5.2f\n" % (coin_name, p.current_price)
        line2 = "Wallet now contains %1.6f %s (worth $%5.2f)" \
                % (w.n_coin, coin_name, w.n_coin * p.current_price)
        body = subj_line + line1 + line2
        self.conn.sendmail(self.address, self.address, body)

    def sellEmail(self, w, p):
        coin_name = p.pair[:3]

        subj_line = "Subject: Ethel just sold %s\n" % coin_name
        line1 = "%s price at sell: $%5.2f\n" % (coin_name, p.current_price)
        line2 = "Wallet now contains $%5.2f (worth %1.6f %s)" \
                % (w.n_usd, w.n_usd / p.current_price, coin_name)
        body = subj_line + line1 + line2
        self.conn.sendmail(self.address, self.address, body)
