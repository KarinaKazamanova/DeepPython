class Card:
    number = 0
    balance = 0.0
    owner = ""

    def create_new_card(self, number, owner):
        self.number = number
        self.balance = 0
        self.owner = owner

    def set_balance(self, amount):
        self.balance = amount

        # card.set_balnce(amount)

    def get_balance(self):
        return self.balance
    
    def get_owner(self):
        return self.owner
    
    def get_card_number(self):
        return self.number
    
