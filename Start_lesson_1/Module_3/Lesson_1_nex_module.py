#task_1
# Завдання 1
# Користувач зберігає печиво у спеціальному кошику.
# Потрібно написати програму яка покаже вміст цього
# кошика.
# Приклад
# Введіть кількість печива: 7
# Вміст кошика:
# 🍪🍪🍪🍪🍪🍪🍪
# Щоб емодзі печива виводились в одному рядку
# використовуйте
# print(..., end="")
# Розставте боки коду нижче у правильному порядку та
# додайте підписи що робить команда
# #
# print("Вміст кошика:")
# #
# print("🍪", end="")
# #
# for cookie in range(cookies):
# #
# cookies = int(input("Введіть кількість печива: "))


# # Вводимо кількість печива
# cookies = int(input("Введіть кількість печива: "))
#
# # Виводимо заголовок
# print("Вміст кошика:")
#
# # Повторюємо дію стільки разів, скільки є печива
# for cookie in range(cookies):
#     # Виводимо печиво в одному рядку
#     print("🍪", end="")




#task_2
# Бухгалтерія має згенерувати номери рахунків для
# клієнтів у форматі INV-1001, INV-1002 тощо
# Програма отримує кількість клієнтів
#
# # user enter quantity ogf customers
# clients = int(input("Enter quantity of clients: "))
#
# # Enter name of function
# print("Accounts:")
#
# # Counting
# for i in range(1, clients + 1):
#     print("INV-", 1000 + i, sep="")





#task_3
# Ви розробляєте застосунок для планування тренувань.
# Користувач вводить раз на скільки днів він готовий
# виконувати вправи. Вам потрібно вивести всі дні протягом
# місяця(30 днів) коли треба займатись спортом.
# Приклад
# Раз на скільки днів тренуватися: 5
# День тренування: 1
# День тренування: 6
# День тренування: 11
# День тренування: 16
# День тренування: 21
# День тренування: 26

# days = int(input("Раз на скільки днів тренуватися: "))
#
# for i in range(1, 31, days):
#     print("День тренування:", i) #sorry left names on ukrainian, don`t know how to translate correctly




#task_4
# Завдання 4
# У завданні 1 зробіть так щоб користувач сам вирішував
# що він кладе в кошик, бо не всі люблять печиво.
# З можливих варіантів 🍪 🧁 🍩 🍬 🍫 🍭 🥨 🥠 🍰 🍎
# 🍏 🍐 🍊 🍌 🍉 🍇 🍓 🫐 🍒 🍑 🥭 �

# Вибираємо, що покласти в кошик
# food = input("Що покласти в кошик? 🍪 🧁 🍩 🍬 🍫 🍭 🥨 🥠 🍰 🍎 🍏 🍐 🍊 🍌 🍉 🍇 🍓 🫐 🍒 🍑 🥭: ")
#
# # Вводимо кількість
# cookies = int(input("Введіть кількість: "))
#
# # Виводимо вміст кошика
# print("Вміст кошика:")
#
# # Повторюємо вибраний емодзі
# for cookie in range(cookies):
#     print(food, end="")




#task_5
# Завдання 5
# Напишіть програму яка виконує зворотній відлік перед
# запуском ракети.
#
# print("Start of the countdown!")
# for number in range(10, 0,-1):
#     print(number)
#
# print("Start!")




#task_6
# Потрібно вивести на екран таблицю множення для
# певного числа. Наприклад для числа 5
# 1*5 = 5
# 2*5 =10
# …
# 10*5=50
# Виправте помилку в коді
# num = int(input("Введіть число: "))
# for num in range(1, 11):
#  result = num * num      #here is mistake, have to be two different numbers
#  print(f"{num} * {num} = {result}")   # here the same mistake

# num = int(input("Введіть число: "))
#
# for myltiplayer in range(1, 11):
#     result = myltiplayer * num
#     print(f"{myltiplayer} * {num} = {result}")



# #task_7
# Перепишіть завдання 7(про вклад в банк) з теми Модуль
# 2 Змінні та типи даних. Частина 2 (файл Практична 2.2)
# використовуючи цикл
#task_7 from practice work
# Користувач вводить суму вкладу в банк та відсоток
# ставки.
# ● Обчисліть скільки користувач отримує через 5 років,
# якщо кожного року сума вкладу збільшується на даний
# відсоток
# # ● Виведіть суму вкладу кожного року окремо
#
# deposit = float(input("Enter your deposite: "))
# interest_rate = float(input("Enter interest rate: "))
#
# calculation = 1 + interest_rate / 100
#
# deposit_every_year = deposit * calculation
#
# deposit_year1 = deposit_every_year * calculation
# print("One year: ", deposit_year1)
#
# deposit_year2 = deposit_year1 * calculation
# print("Two years: ", deposit_year2)
#
# deposit_year3 = deposit_year2 * calculation
# print("Three years: ", deposit_year3)
#
# deposit_year4 = deposit_year3 * calculation
# print("Four years: ", deposit_year4)
#
# deposit_year5 = deposit_year4 * calculation
# print("Four years: ", deposit_year5)
#
# print(f"In 5 year your deposit will amount to: {deposit_year5: .2f}")




# deposit = float(input("Enter your deposit: "))
# interest_rate = float(input("Enter interest rate: "))
#
# calculation = 1 + interest_rate / 100
#
# for year in range(1, 6):
#     deposit = deposit * calculation
#     print(f"Year {year}: {deposit:.2f}")
#
# print(f"In 5 years your deposit will amount to: {deposit:.2f}")