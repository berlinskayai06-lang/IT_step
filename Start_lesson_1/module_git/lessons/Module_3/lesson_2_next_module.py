# task_1
# Користувач вводить свої ім’я та вік. Якщо введено
# від’ємне число то попросити ще раз ввести правильний вік
# поки не буде введено додатнє число.
# В кінці вивести привітання “Привіт Джон. Тобі 36
# років”
#
# name = input("Enter your name, please: ")
# age = int(input("Enter your age, please: "))
#
# while age <= 0:
#     age = int(input("Wrong age! Please, try again: "))
#
# print(f"Hello {name}. You are {age} years old.")


# task_2
# Користувач вводить суму грошей, яку він хоче
# відкласти. Далі кожного дня користувач вводить суму, яку
# він кладе в скарбничку.
# Програма зупиняється коли грошей достатньо.
# Виправте помилку в коді

# goal = float(input("Цільова сума? "))
# while True:
#  total = 0
#  daily_amount = float(input("Сьогоднішній вклад? "))
#  total += daily_amount
#
#  if total >= goal:
#      break
# print(f"Мету досягнуто! У скарбничці {total} грн.")

#
# goal = float(input("Цільова сума? "))

# total = 0
# while True:
#     daily_amount = float(input("Сьогоднішній вклад? "))
#     total += daily_amount
#
#     if total >= goal:
#         break

# print(f"Мету досягнуто! У скарбничці {total} грн.")


# task_3
# Користувач вводить довжину в метрах. Покажіть її у
# ● Ярдах(1 ярд = 0,9144 метра)
# ● Футах(1 фут = 0,3048 метра)
# В кінці спитайте користувача чи продовжувати роботу
# програми.

# while True:
#     meters = float(input("Enter the lenght in meters: "))
#
#     yards = meters / 0.9144
#     feet = meters / 0.3048
#
#     print(f"Yards: {yards:.2f}")
#     print(f"Foots: {feet:.2f}")
#
#     answer = input("Would you like to continue? (yes/no): ")
#
#     if answer.lower() != "yes":
#         print("Ok! Good luck")
#         break


# task_4
# У завданні 2 ще виведіть кількість днів за яку була
# зібрана потрібна сума.

# goal = float(input("Цільова сума? "))
#
# total = 0
# days = 0
# while True:
#     daily_amount = float(input("Сьогоднішній вклад? "))
#     total += daily_amount
#     days += 1
#
#     if total >= goal:
#         break
#
# print(f"Мету досягнуто! У скарбничці {total} грн.")
# print(f"Кількість днів: {days}")


# task_5
# Ваш колега написав програму для підрахунку кількість
# товарів, але програма не виводить фразу Підрахунок
# завершений , виправте помилку

# total_items = 0
# print("Додайте товари. Для завершення введіть 'stop'.")
#
# while True:
#     item = input("Введіть товар: ")
#
#     if item == "stop":
#        print("Підрахунок завершений")   #here i changed place of break and print("Підрахунок завершений")
#        break
#
#     total_items += 1   #here was mistake, i add "="
#
# print(f"Всього товарів додано: {total_items}")


# task_6
# Напишіть програму для введення пароля від банкомату.
# У користувача є лише три спроби
# В кінці виведіть чи вдалось правильно ввести пароль

# pin_code = "6996"
# attempts = 0

# while attempts < 3:
#     user_pin_code = input("Enter your pin: ")
#     attempts += 1
#
#     if user_pin_code == pin_code:
#         print("PIN code entered correctly!")
#         break
#     else:
#         print("Incorrect PIN code!")
#
# if user_pin_code == pin_code:
#     print("Access allowed!")
# else:
#     print("Access blocked! The attempts ended.")

# password = "1234"
#
# for i in range(3):
#     user_password = input("Enter your PIN: ")
#
#     if user_password != password:
#         print("Incorrect pin")
#
#     if user_password == password:
#             print("Correct PIN code!")
#             break
# else:
#     print("Access blocked! The attempts ended!")   #one more varian. but was realy difficult


# extra_task_1
# Користувач вводить з клавіатури ширину та висоту прямокутника. Потрібно відобразити на екран заповнений прямокутник
#із зазначеними висотою та шириною. Наприклад, якщо користувач ввів висоту 3, а ширину 5 на екрані буде виведено:
#
# *****
# *****
# *****


# width = int(input("Enter the width: "))
# height = int(input("Enter the height: "))
#
# row = 0
#
# while row < height:
#     print("*" * width)
#     row += 1
