import Card
import Amountexception


class Atm:
    serial_number = 0
    OPERATING_COMISSION =  0.015  # 1.5%
    MINIMUM_COMISSION = 30
    MAXIMUM_COMISSION = 600
    INTEREST_RATE = 0.03
    INCOME_TAX_RATE = 0.13


    def withdrow_money(self, card, amount):
        
            if card.get_balance() >= amount + 30:
                if amount > 0 & amount % 50 == 0:
                    if amount * self.OPERATING_COMISSION < 30:
                        card.set_balance(card.get_balance() - amount  - 30)
                    elif amount * self.OPERATING_COMISSION > 600:
                        card.set_balance(card.get_balance() - amount  - 600)
                    else:
                        card.set_balance(card.get_balance() - amount * (1 + self.OPERATING_COMISSION))
                else:
                    raise Amountexception.Amountexception("Вы ввели некорректную сумму, необходимо ввести сумму, кратную 50")
            else:
                raise Amountexception.Amountexception("На вашем счете недостаточно денег, чтобы осуществить операцию")
        

    def put_money(self, card, amount):
        
            if amount > 0 and amount % 50 == 0: 
                if amount * self.OPERATING_COMISSION < 30:
                    card.set_balance(card.get_balance() + amount  - 30)
                elif amount * self.OPERATING_COMISSION > 600:
                    card.set_balance(card.get_balance() + amount  - 600)
                else:
                    card.set_balance(card.get_balance() + amount * (1 - self.OPERATING_COMISSION))
            else:
                raise Amountexception.Amountexception("Вы ввели некорректную сумму, необходимо ввести сумму, кратную 50")
        
            

    def charge_interest(self, card):
        card.set_balance(card.get_balance() * (1 + self.INTEREST_RATE))

    def pay_tax(self, card):
        card.set_balance(card.get_balance() * (1 - self.INCOME_TAX_RATE))

    def stop_atm(self):
        answer = input("Хотите остановить? Д/н").lower()
        if answer in ["да", "д", "yes", "y"]:
            return True
        elif answer in ["нет", "н", "n", "no"]:
            return False
        else:
            raise AnswerError.AnswerError("Я Вас не понял,, повторите, пожалуйста")

