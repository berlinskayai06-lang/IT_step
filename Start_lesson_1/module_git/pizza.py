# Завдання 4
# Створіть нову гілку practice/pizza
# Перейдіть на неї та реалізуйте програму замовлення
# піци в декілька комітів
# Коміт1
# Вивід Меню
# 1. Вибрати піцу
# 2. Вихід
# Далі реалізуйте нескінченний цикл
# Якщо користувач обирає 1, то запитати назву піци та
# кількість і вивести повідомлення
# Замовлено [назва піци], [кількість] шт
# Коміт2
# Додайте меню з цінами піц
# Маргарита – 150 грн
# Пепероні – 180 грн
# Чотири сири – 200 грн
# Якщо користувач ввів неправильно назву піци то
# повідомити про це
# Коміт3
# Додайте третю опцію – показати все замовлення
# Треба вивести які піци були замовлені, їхня вартість та
# загальна вартість
# Приклад:
# ========== ВАШЕ ЗАМОВЛЕННЯ ==========
# Піца Кількість Вартість
# --------------------------------------
# Маргарита 2 300 грн
# Чотири сири 1 200 грн
# --------------------------------------
# Загальна вартість: 500 грн
# ======================================
# Дякуємо за замовлення!
# Коміт4
# Займіться рефакторингом
# Перевірте щоб кількості піц не були від’ємними
# Також загальна кількість піц в замовлені не може бути
# більше 15
# Створіть пул реквест(див завдання 4) та очікуйте
# підтвердження від викладача




while True:
    print("\n===== PIZZA MENU =====")
    print("1. Order pizza")
    print("2. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        pizza_name = input("Enter pizza name: ")
        quantity = int(input("Enter quantity: "))

        print(f"Ordered {pizza_name}, {quantity} pcs")

    elif choice == "2":
        print("Thank you for your order!")
        break

    else:
        print("Invalid option! Please try again.")




pizzas = {
    "Margherita": 150,
    "Pepperoni": 180,
    "Four Cheese": 200,
}

while True:
    print("\n===== PIZZA MENU =====")
    print("1. Order pizza")
    print("2. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("\nAvailable pizzas:")

        for name, price in pizzas.items():
            print(f"{name} - {price} UAH")

        pizza_name = input("Enter pizza name: ").strip()

        if pizza_name not in pizzas:
            print("Pizza not found! Please choose from the menu.")
            continue

        quantity = int(input("Enter quantity: "))

        print(f"Ordered {pizza_name}, {quantity} pcs")

    elif choice == "2":
        print("Thank you for your order!")
        break

    else:
        print("Invalid option! Please try again.")





pizzas = {
    "Margherita": 150,
    "Pepperoni": 180,
    "Four Cheese": 200,
}

orders = {}

while True:
    print("\n===== PIZZA MENU =====")
    print("1. Order pizza")
    print("2. Exit")
    print("3. Show complete order")

    choice = input("Choose an option: ")

    if choice == "1":
        print("\nAvailable pizzas:")

        for name, price in pizzas.items():
            print(f"{name} - {price} UAH")

        pizza_name = input("Enter pizza name: ").strip()

        if pizza_name not in pizzas:
            print("Pizza not found! Please choose from the menu.")
            continue

        quantity = int(input("Enter quantity: "))

        orders[pizza_name] = orders.get(pizza_name, 0) + quantity

        print(f"Ordered {pizza_name}, {quantity} pcs")

    elif choice == "2":
        print("Thank you for your order!")
        break

    elif choice == "3":
        print("\n========== YOUR ORDER ==========")
        print(f"{'Pizza':<16} {'Quantity':<10} Cost")
        print("--------------------------------")

        total_price = 0

        for pizza_name, quantity in orders.items():
            cost = pizzas[pizza_name] * quantity
            total_price += cost

            print(f"{pizza_name:<16} {quantity:<10} {cost} UAH")

        print("--------------------------------")
        print(f"Total price: {total_price} UAH")
        print("================================")

    else:
        print("Invalid option! Please try again.")




PIZZAS = {
    "Margherita": 150,
    "Pepperoni": 180,
    "Four Cheese": 200,
}

MAX_PIZZAS = 15


def show_menu():
    print("\n===== PIZZA MENU =====")
    print("1. Order pizza")
    print("2. Exit")
    print("3. Show complete order")


def show_pizzas():
    print("\nAvailable pizzas:")

    for name, price in PIZZAS.items():
        print(f"{name} - {price} UAH")


def add_pizza(orders):
    show_pizzas()

    pizza_name = input("Enter pizza name: ").strip()

    if pizza_name not in PIZZAS:
        print("Pizza not found! Please choose from the menu.")
        return

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid quantity! Please enter a whole number.")
        return

    if quantity <= 0:
        print("Quantity must be greater than zero!")
        return

    total_quantity = sum(orders.values())

    if total_quantity + quantity > MAX_PIZZAS:
        print("Error! Maximum 15 pizzas per order.")
        print(f"You can order {MAX_PIZZAS - total_quantity} more pizzas.")
        return

    orders[pizza_name] = orders.get(pizza_name, 0) + quantity

    print(f"Ordered {pizza_name}, {quantity} pcs")


def show_order(orders):
    print("\n========== YOUR ORDER ==========")
    print(f"{'Pizza':<16} {'Quantity':<10} Cost")
    print("--------------------------------")

    total_price = 0

    for pizza_name, quantity in orders.items():
        cost = PIZZAS[pizza_name] * quantity
        total_price += cost

        print(f"{pizza_name:<16} {quantity:<10} {cost} UAH")

    print("--------------------------------")
    print(f"Total price: {total_price} UAH")
    print("================================")


def main():
    orders = {}

    while True:
        show_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            add_pizza(orders)

        elif choice == "2":
            print("Thank you for your order!")
            break

        elif choice == "3":
            show_order(orders)

        else:
            print("Invalid option! Please try again.")


if __name__ == "__main__":
    main()
