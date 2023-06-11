import Card
import Amountexception
import Atm
MESSAGE = "Операция прошла успешно"
TAXABLEAMOUNT = 5_000_000
card_1 = Card.Card()
card_1.create_new_card(1234567,"Stanley")
atm = Atm.Atm()
stop_flag = False
transaction_count = 0

# atm.put_money(card_1, 100)
# print(f"Ваш баланс: {card_1.get_balance()}")

while not stop_flag:
    transaction = input("Что вы хотите сделать: снять (оплатить) или внести? ")
    match transaction.split():
        case ["снять"] | ["оплатить"]:
            
            while True:
                try:
                    amount = int(input("Сколько вы хотите снять (оплатить)?\n"))
                    atm.withdrow_money(card_1, amount)
                    transaction_count += 1
                    print(MESSAGE)
                    break
                except Exception as exc:
                    print(exc)
                    continue

        case ["внести"] | ["пополнить"]:
            
            while True:
                try:
                    amount = int(input("Сколько вы хотите внести?\n"))
                    atm.put_money(card_1, amount)
                    transaction_count += 1
                    print(MESSAGE)
                    break
                except Exception as exc:
                    print(exc)
                    continue
        case _:
            print("Не понял Вас, повторите Ваш запрос, пожауйста\n")
            continue
            
    if transaction_count % 3 == 0:
        atm.charge_interest(card_1)
    if card_1.get_balance() >= TAXABLEAMOUNT:
        atm.pay_tax(card_1)
    print(f"Ваш баланс: {card_1.get_balance()}")
    while True:
        try:
            stop_flag = atm.stop_atm()
            break
        except Exception as exc:
            print(exc)
            continue









