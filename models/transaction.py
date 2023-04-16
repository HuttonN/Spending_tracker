class Transaction:
    def __init__(self, amount, merchant, tag, date, id=None):
        self.amount = amount
        self.merchant = merchant
        self.tag = tag
        self.date = date
        self.id = id