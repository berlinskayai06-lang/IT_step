#task_1
# Завдання 1
# Створіть список чисел [1, 8, -5, 9]
# ● Виведіть на екран елементи цього списку
# ● Збільшіть кожне число в 3 рази та виведіть результат
# ● Замініть усі числа більші 10 на 0 та виведіть
# результат


# numbers = [1, 8, -5, 9]
# print(numbers)
#
# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 3
# print(numbers)
#
# for i in range(len(numbers)):
#     if numbers[i] > 10:
#         numbers[i] = 0
# print(numbers)

#task_2
# Користувач вводить числа, поки не введе -1.
# Збережіть усі ці числа в список. Виведіть їхню кількість,
# суму, мінімальне, максимальне та середнє.
# Скористайтесь функціями min, max, sum, len

# numbers = []
#
# while True:
#     number = int(input("Enter a number: "))
#
#     if number == -1:
#         break
#
#     numbers.append(number)
#
# if len(numbers) > 0:
#     print("Numbers:", numbers)
#     print("Count:", len(numbers))
#     print("Sum:", sum(numbers))
#     print("Minimum:", min(numbers))
#     print("Maximum:", max(numbers))
#     print("Average:", sum(numbers) / len(numbers))
# else:
#     print("The list is empty")


#task_3
# Користувач вводить числа, поки не введе 0. Створіть
# два нових списки: з додатніми та від’ємними числами.
# Виведіть елементи обох списків на екран.
# Виправіть помилку в коді
# while True:
#     number = int(input("Введіть число (0 для завершення): "))
#
#     positive = []     #shouldn`t be in cycle
#     negative = []     #shouldn`t be in cycle
#
#     if number < 0:               #this sign for negative numbers
#         positive.append(number)
#     else:
#         negative.append(number)
#
# print("Додатні числа:", positive)
# print("Від'ємні числа:", negative)
#also need something to finish cycle


# positive = []
# negative = []
#
# while True:
#     number = int(input("Enter a number (0 to stop): "))
#
#     if number == 0:
#         break
#
#     if number > 0:
#         positive.append(number)
#     else:
#         negative.append(number)
#
# print("Positive numbers:", positive)
# print("Negative numbers:", negative)


#task_4
# Користувач вводить зарплати співробітників, поки не
# введе -1. Після чого вводить відсоток на який треба
# збільшити усім зарплату.
# Виведіть нові зарплати
#
# salaries = []
#
# while True:
#     salary = float(input("Enter salary: "))
#     if salary == -1:
#         break
#     salaries.append(salary)
#
# percent = float(input("Enter percentage: "))
#
# for salary in salaries:
#     new_salary = salary + salary * percent / 100
#     print("New salary:", new_salary)


#task_5
# Користувач вводить кількість днів, після чого
# температуру повітря кожного дня.
# Збережіть температури у список
# Для кожного дня порахуйте різницю температур з
# попереднім днем.
# Виправіть помилку в коді

# days = int(input("Введіть кількість днів: "))
#
# for i in range(days):    #wrong index
#     temperatures = []    #move it from cycle
#     temperature = float(input(f"Введіть температуру за {i + 1}-й день: "))
#     temperatures.append(temperature)
#
# print("Температури:", temperatures)
#
# for i in range(days):
#     difference = temperatures[i] - temperatures[i - 1]
#     print(f"Різниця температур за {i + 1}-й день: {difference}")


# days = int(input("Enter the number of days: "))
#
# temperatures = []
#
# for i in range(days):
#     temperature = float(input(f"Enter temperature for day {i + 1}: "))
#     temperatures.append(temperature)
#
# print("Temperatures:", temperatures)
#
# for i in range(1, days):
#     difference = temperatures[i] - temperatures[i - 1]
#     print(f"Temperature difference for day {i + 1}: {difference}")



#task_6
# Створіть застосунок банк. Є список з рахунками
# клієнтів.
# Користувач вибирає одну з команд
# ● Додати клієнта
# ● Видалити клієнта
# ● Поповнити рахунок
# ● Зняти кошти
# ● Вихід
# При додаванні клієнта, добавте рахунок в 0грн в
# кінець списку.
# В інших випадках запросіть ID(індекс) клієнта і якщо
# він вірний, то проведіть операцію


# accounts = []
#
# while True:
#     print("1. Add client")
#     print("2. Delete client")
#     print("3. Deposit money")
#     print("4. Withdraw money")
#     print("5. Exit")
#
#     command = int(input("Choose a command: "))
#
#     if command == 1:
#         accounts.append(0)
#
#     elif command == 5:
#         break
#
#     elif command in (2, 3, 4):
#         client_id = int(input("Enter client ID: "))
#
#         if 0 <= client_id < len(accounts):
#
#             if command == 2:
#                 accounts.pop(client_id)
#
#             elif command == 3:
#                 amount = float(input("Enter amount: "))
#
#                 if amount > 0:
#                     accounts[client_id] += amount
#
#             elif command == 4:
#                 amount = float(input("Enter amount: "))
#
#                 if 0 < amount <= accounts[client_id]:
#                     accounts[client_id] -= amount
#                 else:
#                     print("Invalid amount or insufficient funds")
#
#         else:
#             print("Invalid client ID")
#
#     else:
#         print("Invalid command")
#
#     print("Accounts:", accounts)


#task_7
# Створіть за стосунок магазин. Є список з цінами
# товарів.
# Користувач обирає одну з дій
# ● Додати товар до кошика
# ● Видалити товар з кошика
# ● Очистити кошик
# ● Вивести загальну ціну
# ● Вихід
# Де потрібно, користувач вводить ID(індекс) товару та
# його кількість

# prices = [100, 250, 50, 300]
# cart = []
#
# while True:
#     print("1. Add product")
#     print("2. Remove product")
#     print("3. Clear cart")
#     print("4. Total price")
#     print("5. Exit")
#
#     command = int(input("Choose a command: "))
#
#     if command == 1:
#         product_id = int(input("Enter product ID: "))
#         quantity = int(input("Enter quantity: "))
#
#         if 0 <= product_id < len(prices) and quantity > 0:
#             for i in range(quantity):
#                 cart.append(prices[product_id])
#
#     elif command == 2:
#         product_id = int(input("Enter product ID: "))
#         quantity = int(input("Enter quantity: "))
#
#         if 0 <= product_id < len(prices) and quantity > 0:
#             for i in range(quantity):
#                 if prices[product_id] in cart:
#                     cart.remove(prices[product_id])
#
#     elif command == 3:
#         cart.clear()
#
#     elif command == 4:
#         print("Total price:", sum(cart))
#
#     elif command == 5:
#         break
#
#     else:
#         print("Invalid command")
#
#     print("Cart:", cart)