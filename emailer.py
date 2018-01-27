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
        subj_line = "Subject: Ethel just bought ETH\n"
        line1 = "ETH price at purchase: $%5.2f" % p.current_price
        line2 = "Wallet now contains %1.6f ETH (worth $%5.2f)" \
                % (w.n_eth, w.n_eth * p.current_price)
        body = subj_line + line1 + line2
        self.conn.sendmail(self.address, self.address, body)

    def sellEmail(self, w, p):
        subj_line = "Subject: Ethel just sold ETH\n"
        line1 = "ETH price at sell: $%5.2f" % p.current_price
        line2 = "Wallet now contains $%5.2f (worth %1.6f ETH)" \
                % (w.n_usd, w.n_usd / p.current_price)
        body = subj_line + line1 + line2
        self.conn.sendmail(self.address, self.address, body)
