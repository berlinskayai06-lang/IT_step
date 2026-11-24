# task_1
# Завдання 1
# Користувач вводить рядок та індекс. Виведіть символ
# під цим індексом. Якщо індекс завеликий, виведіть
# інформацію про помилку.
#
#
# text = input("Enter a line: ")
# idx = int(input("Enter an index: "))
#
# if 0 <= idx < len(text):
#     print(text[idx])
# else:
#     print("Error: Index out of range")



# #task_2
# Завдання 2
# Користувач вводить рядок та два індекси. Виведіть
# зріз рядка. Виправіть помилку в коді
#
# text = input("Введіть рядок: ")
#
# start = float(input("Введіть початковий індекс: "))   #can not be float
# end = float(input("Введіть кінцевий індекс: "))
#
# segment = text[start, end]    #have to be symbol :
#
# print(segment)

#
# text = input("Enter a string: ")
#
# start = int(input("Enter the start index: "))
# end = int(input("Enter the end index: "))
#
# segment = text[start:end]
#
# print(segment)


# #task_3
# Завдання 3
# Користувач вводить рядок та число n. Виведіть перші
# n символів. Також виведіть останні n символів.
#
# text = input("Enter a line: ")
# idx_num = int(input("Enter a number: "))
#
# print("First characters:", text[:idx_num])
#
# if idx_num > 0:
#     print("Last characters:", text[-idx_num:])
# else:
#     print("Last characters:", "")

#task_4
# Завдання 4
# Користувач вводить рядок. Перевірте чи це
# речення(закінчується на .!?)
#
# text = input("Enter a sentence: ")
#
# if text and text[-1] in ".!?":
#     print("It is a sentence")
# else:
#     print("It is not a sentence")

#task_5
# Завдання 5
# Користувач вводить рядок. Перевірте чи перший
# символ – це велика літера. Виправіть помилку в коді

# text = input("Введіть рядок: ").lower()  # lower make all symbols small
#
# if text[0].upper():                #change upper(make symbol capital)  to isupper (check if symbol is capital)
#     print("Перший символ — велика літера")
# else:
#     print("Перший символ — не велика літера")
#
# text = input("Введіть рядок: ")
#
# if text[0].isupper():
#     print("Перший символ — велика літера")
# else:
#     print("Перший символ — не велика літера")

# #task_6
# Завдання 6
# Користувач вводить рядок. Перевірте чи це
# паліндром(читається задом наперед так само).
# Приклади: Кіт утік, око, потоп
#
# text = input("Enter a line: ")
#
# text = text.lower()
# text = text.replace(" ", "")
#
# if text == text[::-1]:
#     print("It is a palindrome")
# else:
#     print("It is not a palindrome")

#task_7
# Завдання 7
# Користувач вводить рядок та символ. Виведіть індекс
# цього символу.
#
# text = input("Enter a line: ")
# character = input("Enter a character: ")
#
# print(text.index(character))


# #task_8
# Завдання 8
# Користувач вводить рядок та символ. Виведіть усі
# індекси цього символу, якщо він зустрічається декілька
# разів.
#
# text = input("Enter a line: ")
# character = input("Enter a character: ")
#
# for i in range(len(text)):
#     if text[i] == character:
#         print(i)

#task_9
# Завдання 9
# Користувач вводить слова поки не введе слово END.
# Збережіть це слово до одного з 4-ох рядків:
# ● герундій – закінчується на ing
# ● дієслово past tense – закінчується на ed
# ● починаються на голосну – aeuio
# ● решта
# Слова можуть вводитися як великими так і малими
# літерами


# gerund = ""
# past = ""
# vowels = ""
# other = ""
#
# while True:
#     word = input("Enter a word: ").lower()
#
#     if word == "END":
#         break
#     elif word[-3:] == "ing":
#         gerund += word + " "
#     elif word[-2:] == "ed":
#         past += word + " "
#     elif word[0] in "aeuio":
#         vowels += word + " "
#     else:
#         other += word + " "
#
# print("Gerund:", gerund)
# print("Past tense:", past)
# print("Vowels:", vowels)
# print("Other:", other)


#task_10
# Користувач вводить математичний вираз, наприклад
# 23+45. Виведіть результат
# Обробіть такі математичні операції – +*/-
# Реалізуйте як консольну програму(закінчити якщо
# введено EXIT)
# Приклад роботи програми

#
# while True:
#     text = input("Enter an expression: ").upper()
#
#     if text == "EXIT":
#         break
#
#     for i in range(len(text)):
#         if text[i] in "+-*/":
#             a = float(text[:i])
#             b = float(text[i+1:])
#
#             if text[i] == "+":
#                 print("Result:", a + b)
#             elif text[i] == "-":
#                 print("Result:", a - b)
#             elif text[i] == "*":
#                 print("Result:", a * b)
#             elif text[i] == "/":
#                 print("Result:", a / b)
#             break

#task_11
# Користувач вводить текст та число. Зробіть циклічний
# зсув, тобто індекси всіх символів збільшуються на певне
# число, а символи з кінця опиняються спереду.
# Приклади
# abcde 1 – eabcd
# abcde 3 – cdeab
# abcde -1 – bcdea

# text = input("Enter a line: ")
# number = int(input("Enter a number: "))
#
# number = number % len(text)
#
# result = text[-number:] + text[:-number]
#
# print(result)

#made it with chatGPT, difficult, but understand how % is working

# #task_12
# Реалізуйте римське шифрування – кожен символ
# замінюється на інший, який знаходиться на певній
# відстані в алфавіті.
# Користувач вводить текст, число та пропонує
# зашифрувати або розшифрувати текст.
# Щоб отримати позицію в алфавіті – ord(letter)
# Щоб отримати символ за позицією – chr(num)
#
text = input("Enter a text: ").lower()
quantity_of_positions = int(input("Enter a shift: "))
mode = input("Encrypt or decrypt? ").lower()

if mode == "decrypt":
    quantity_of_positions = -quantity_of_positions

result = ""

for letter in text:
    if letter in "abcdefghijklmnopqrstuvwxyz":
        num = ord(letter) - ord("a")
        num = (num + quantity_of_positions) % 26
        result += chr(num + ord("a"))
    else:
        result += letter

print("Result:", result)

#also made it with chat, make him explain everything. Understand everything, can explain if you ask