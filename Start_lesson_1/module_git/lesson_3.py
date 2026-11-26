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

