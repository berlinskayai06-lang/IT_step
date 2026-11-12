#task_1
# Користувач вводить оцінку за іспит(від 1 до 5) поки не
# введе правильне число. Після цього виведіть цю оцінку
# текстом
# 1. Дуже погано
# 2. Погано
# 3. Задовільно
# 4. Добре
# 5. Чудово
#
# while True:
#     grade = int(input("Enter your grade (1-5): "))
#
#     if 1 <= grade <= 5:
#         break
#     else:
#         print("Invalid grade! Try again.")
#
# if grade == 1:
#     print("Very bad")
# elif grade == 2:
#     print("Bad")
# elif grade == 3:
#     print("Satisfactory")
# elif grade == 4:
#     print("Good")
# elif grade == 5:
#     print("Excellent")

# #task_2
# Проводиться опитування «Чи потрібно будувати більше
# дитячих садків у вашому місті?»
# Напишіть програму для підрахунку відповідей.
# Користувач вводить слова «так» або «ні» поки не введе
# слово «стоп», після чого треба показати кількості «так» та
# «ні» і також яких голосів більше.
# Якщо введено невідоме слово, то вивести повідомлення
# про помилку та продовжити підрахунок


# yes = 0
# no = 0
#
# while True:
#     answer = input("Enter your vote (yes/no/stop): ").lower()
#
#     if answer == "stop":
#         break
#     elif answer == "yes":
#         yes += 1
#     elif answer == "no":
#         no += 1
#     else:
#         print("Invalid answer! Try again.")
#
# print(f"Yes votes: {yes}")
# print(f"No votes: {no}")
#
# if yes > no:
#     print("More people voted YES")
# elif no > yes:
#     print("More people voted NO")
# else:
#     print("The votes are equal")

#task_3
# Нижче наведено код який зупиняється коли користувач
# вводить число 0, але він не працює.
# Виправіть помилку
# print("Введіть число (0 для виходу):")
# while True:
# num = input("Ваше число: ")
# if num == 0:
# print("Вихід з програми.")
# break
# print(f"Ви ввели: {num}")
#
# print("Enter a number (0 to exit):")
#
# while True:
#     num = int(input("Your number: "))
#
#     if num == 0:
#         print("Exiting the program.")
#         break
#
#     print(f"You entered: {num}")
