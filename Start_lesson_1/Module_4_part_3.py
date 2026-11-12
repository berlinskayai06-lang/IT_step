#task_1
# Користувач вводить число від 1 до 9. Потрібно вивести
# для цього числа таблицю множення.
# Наприклад для 5 це буде:
# 1х5=5
# 2х5=10
# …
# 9х5=45
# 10х5=50
# Якщо користувач ввів неправильне число то
# продовжувати запитувати поки не введе правильне.

# while True:
#     number = int(input("Enter a number from 1 to 9: "))
#
#     if 1 <= number <= 9:
#         break
#     else:
#         print("Invalid number! Try again.")
#
# for multiplier in range(1, 11):
#     print(f"{multiplier} x {number} = {multiplier * number}")

#task_2
# Користувач вводить свої оцінки поки не введе 0. Після
# чого програма виводить середню оцінку.
# Виправіть помилку в коді
# total = 0
# count = 0
# while True:
# grade = input("Введіть оцінку: ")
# if grade == 0:
# break
# total += grade
# average_grade = total / count
# print(f"середня оцінка:
# {average_grade}")

#
# total = 0
# count = 0
#
# while True:
#     grade = int(input("Введіть оцінку: "))
#
#     if grade == 0:
#         break
#
#     total += grade
#     count +=1  #here is mistake
#
# if count > 0:  #and here also have to be some command
#     average_grade = total / count
#     print(f"середня оцінка: {average_grade}")

#task_3
# Напишіть простий калькулятор
# Користувач вводить два числа після чого обирає яку дію
# виконати:
# 1. сума
# 2. різниця
# 3. добуток
# 4. частка
# 5. вихід
# Якщо користувач обрав частку, то переконайтесь що не
# буде ділення на 0. У випадку проблеми виведіть відповідне
# повідомлення.
#
# while True:
#     number1 = float(input("Enter first number: "))
#     number2 = float(input("Enter second number: "))
#
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Exit")
#
#     option = int(input("Choose an operation (1-5): "))
#
#     if option == 1:
#         print(f"Result: {number1 + number2}")
#
#     elif option == 2:
#         print(f"Result: {number1 - number2}")
#
#     elif option == 3:
#         print(f"Result: {number1 * number2}")
#
#     elif option == 4:
#         if number2 != 0:
#             print(f"Result: {number1 / number2}")
#         else:
#             print("Error! Cannot divide by zero.")
#
#     elif option == 5:
#         print("Exiting calculator.")
#         break
#
#     else:
#         print("Invalid choice! Try again.")

#task_4
# Програма повинна зареєструвати рівно 3 учасників. Для
# цього користувач вводить їхні імена, але ім’я admin уже
# зайняте.
# Виправіть помилку в коді
# for i in range(3):
#  name = input("Введіть ім'я: ")
#  if name == "admin":
#  print("Це ім'я недоступне")
#  print(f"Учасник №{i}: {name}")
# Приклад роботи програми
# Введіть ім'я: Mary
# Учасник №1: Mary
# Введіть ім'я: admin
# Це ім'я недоступне
# Введіть ім'я: admin
# Це ім'я недоступне
# Введіть ім'я: John
# Учасник №2: John
# Введіть ім'я: Anna
# Учасник №3: Anna

#
# count = 0
#
# while count < 3:
#     name = input("Enter your name: ")
#
#     if name == "admin":
#         print("This name is unavailable")
#         continue
#
#     count += 1
#     print(f"Participant #{count}: {name}")


# #task_5
# Напишіть гру «Камінь, ножиці, папір»
# Спочатку користувач пропонується вибір:
# 1. Нова гра
# 2. Вихід
# Якщо вибрана нова гра, то користувач вводить кількість
# раундів.
# На кожному раунді користувач вводить одне зі слів:
# «камінь», «ножиці» або «папір». Якщо користувач вводить
# щось інше, зарахуйте це як програш в раунді.
# Коли всі раунди закінчились потрібно вивести кількість
# перемог, програшів та нічиї.
# Щоб згенерувати вибір комп’ютера використайте такий
# код
# computer_choice = random.choice("камінь", "ножиці",
# "папір"])


# import random
#
# while True:
#     print("1. New game")
#     print("2. Exit")
#
#     choice = input("Choose an option: ") 
#
#     if choice == "2":
#         print("Goodbye!")
#         break
#
#     if choice != "1":
#         print("Invalid choice!")
#         continue
#
#     rounds = int(input("How many rounds? "))
#
#     wins = 0
#     losses = 0
#     draws = 0
#
#     for round_number in range(1, rounds + 1):
#         print(f"Round {round_number}")
#
#         user = input("Rock, scissors or paper: ").lower()
#         computer = random.choice(["rock", "scissors", "paper"])
#
#         print(f"Computer: {computer}")
#
#         if user not in ["rock", "scissors", "paper"]:
#             print("You lose!")
#             losses += 1
#
#         elif user == computer:
#             print("Draw!")
#             draws += 1
#
#         elif user == "rock" and computer == "scissors":
#             print("You win!")
#             wins += 1
#
#         elif user == "scissors" and computer == "paper":
#             print("You win!")
#             wins += 1
#
#         elif user == "paper" and computer == "rock":
#             print("You win!")
#             wins += 1
#
#         else:
#             print("You lose!")
#             losses += 1
#
#     print("Game over!")
#     print(f"Wins: {wins}")
#     print(f"Losses: {losses}")
#     print(f"Draws: {draws}")


#task_6
# Змініть завдання 5 так, щоб на можна було грати
# декілька ігор.
# Для цього програма пропонує вибір:
# 1. Нова гра
# 2. Вихід


