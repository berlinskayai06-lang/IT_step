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