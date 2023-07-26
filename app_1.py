# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты-3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн,
# вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

balance = 0
operations_count = 0


def print_balance(balance):
    """Function prints the balance"""
    print(f"Текущий баланс: {balance} у.е.")


while True:
    print("Введите действие: пополнить, снять, выйти")
    action = input("Введите действие: ").lower()

    if action == "выйти":
        print("До свидания!")
        break

    elif action == "пополнить":
        amount = int(input("Введите сумму для пополнения \
                           (сумма должна быть кратна 50): "))
        if amount % 50 == 0:
            balance += amount
            operations_count += 1
            print_balance(balance)
            if operations_count % 3 == 0:
                interest = balance * 0.03
                balance += interest
                print_balance(balance)
            if balance > 5000000:
                balance -= balance * 0.1
                print_balance(balance)
        else:
            print("Сумма должна быть кратна 50!")

    elif action == "снять":
        amount = int(input("Введите сумму для снятия \
                            (сумма должна быть кратна 50): "))
        if amount % 50 == 0:
            if amount <= balance:
                balance -= amount
                operations_count += 1
                print_balance(balance)
                if operations_count % 3 == 0:
                    interest = balance * 0.03
                    balance += interest
                    print_balance(balance)
                if balance > 5000000:
                    balance -= max(30, min(600, balance * 0.015))
                    print_balance(balance)
            else:
                print("Недостаточно средств на счете!")
        else:
            print("Сумма должна быть кратна 50!")

    else:
        print("Некорректное действие!")
