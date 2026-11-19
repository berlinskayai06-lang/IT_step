#task_1
# Завдання 1
# Користувач вводить рядок та символ. Порахуйте скільки
# разів цей символ зустрічається у рядку.
# Зробіть двома способами:
# ● з методом count
# ● з циклом for
# Приклад:
# В “it is amazing” символ “і” зустрічається 3 рази

# #method count()
# # enter sentence and character
# text = input("Enter the sentence: ")
# symbol = input("Enter the character: ")
#
# # Counting the number of occurrences of a character
# count_symbol = text.count(symbol)
#
# # Displaying the result
# print(f'In "{text}" sentence "{symbol}" is found {count_symbol} times')



# #cycle  for
#
# # enter sentence and character
# text = input("Enter the sentence: ")
# symbol = input("Enter the character: ")
#
# # counter
# count_symbol = 0
#
# # Checking every character in the sentence
# for char in text:
#
#     # check if character matching
#     if char == symbol:
#
#         # increment counter by 1
#         count_symbol += 1
#
# # Result
# print(f'In "{text}" character "{symbol}" is found {count_symbol} times')


#task_2
# Завдання 2
# Користувач вводить рядок. Виведіть наступну
# інформацію:
# ● кількість символів
# ● чи є там слово python
# ● кількість шиплячих літер – szh
#
#
# # User enter the text
# text = input("Enter your sentence: ")
#
# # Counting total quantity of characters
# total = len(text)
#
# # Check if "python" in the text by user
# has_python = "python" in text.lower()
#
# # counter sibilant letters
# count_szh = 0
#
# # check every character in the sentence
# for char in text.lower():
#     if char in "szh":
#         count_szh += 1
#
# # Results
# print(f"Quantity of characters: {total}")
#
# if has_python:
#     print('Word "python" is in the sentence')
# else:
#     print('There is no "python" in this sentence')
#
# print(f"Quantity of sibilant letters: {count_szh}")


# #task_3
# Завдання 3
# Користувач вводить тест. Потрібно замінити всі пробіли
# на дефіси. Виправіть помилку в коді
# text = input("Введіть текст: ")
#
# result = text.replace(" ", "-")
# print(f"Змінений текст: {text}") # here is mistake
#
# correct code
# text = input("Введіть текст: ")
#
#
# result = text.replace(" ", "-")
# print(f"Змінений текст: {result}")




#task_4
# Завдання 4
# Користувач вводить рядок та слово. Порахуйте скільки
# разів це слово зустрічається у рядку.

# # user enter text and a word to find
# user_text = input("Enter your sentence: ").lower()
# search_word = input("Enter the word: ").lower()
#
# # Split the text into words
# word_list = user_text.split()
#
# # Count how many times the word appears
# word_count = word_list.count(search_word)
#
# # Print the result
# print(f'The word "{search_word}" appears {word_count} times')


#task_5
# При оформлені посилки заборонено перевозити
# наступні речі:
# ● ножі
# ● гроші
# ● сильні отрути
# # Виправіть помилку в коді
#
# items = input("Введіть ваші речі: ")
# items = items.lower                                    #here is mistake
#
# if "ніж" or "гроші" or "отрута" in items:            #here also mistake
#     print("У вас є речі які заборонено перевозити")
# else:
#     print("Оформлено доставку")

#
# #user to enter parcel items
# user_items = input("Enter your items: ").lower()
#
# # Check for prohibited items
# if "knife" in user_items or "money" in user_items or "poison" in user_items:
#     print("You have items, that are prohibited")
# else:
#     print("Your shipment has been approved!")


#task_6
# Користувач вводить текст. Порахуйте скільки в ньому
# літер та цифр.

#
# # user to enter text
# text = input("Enter the text: ")
#
# # Set both counters to zero
# letter_count = 0
# digit_count = 0
#
# # Go through each character in the text
# for character in text:
#
#     # Check if the character is a letter
#     if character.isalpha():
#         letter_count += 1
#
#     # Check if the character is a digit
#     elif character.isdigit():
#         digit_count += 1
#
# # Print the results
# print(f"Quantity og letters: {letter_count}")
# print(f"Quantity of digits: {digit_count}")



#task_7
# Користувач вводить пароль поки не введе його
# правильно.
# Правильний пароль повинен:
# ● Бути довшим за 8 символів
# ● Містити хоча б одну цифру
# ● Містити хоча б одну літеру


# while True:
#     #user to enter a password
#     password = input("Enter your password: ")
#
#     #starting values
#     has_digit = False
#     has_letter = False
#
#     # Go through each character in the password
#     for character in password:
#
#         # Check if the character is a digit
#         if character.isdigit():
#             has_digit = True
#
#         # Check if the character is a letter
#         elif character.isalpha():
#             has_letter = True
#
#     # Check all password requirements
#     if len(password) > 8 and has_digit and has_letter:
#         print("Your password has been successfully created!")
#         break
#     else:
#         print("Invalid password. Please try again!")







