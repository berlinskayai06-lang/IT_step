# #task_1
# Потрібно порахувати суму чисел в діапазоні, але
# програма виводить не те що треба(загальна сума має бути
# 15), виправіть помилку

# total = 0
# for number in range(1, 6):
#  total = number
#
#  print(f"Сума: {total}")


#
# total = 0
#
# for number in range(1, 6):
#     total += number
#
# print(f"Сума: {total}")

##task_2
# Користувач вводить два числа(початок та кінець
# діапазону). Пройдіться по всіх числах з цього діапазону та
# виведіть такий результат:
# ● якщо число ділиться на 3 – написати Fizz
# ● якщо число ділиться на 5 – написати Buzz
# ● якщо число ділиться на 3 i на 5 – написати FizzBuzz
# ● інакше вивести саме число
# Умови для перевірки чи число ділиться на 3 або 5
# num % 3 == 0
# num % 5 == 0
# приклад для діапазону 10 20
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# 16
# 17
# Fizz
# 19
# Buzz

#
# start = int(input("Enter the begin: "))
# end = int(input("Enter the end: "))
#
# for number in range(start, end + 1):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)


#task_3
# Напишіть програму яка протягом 5 робочих днів запитує
# в кур’єра кількість доставлених замовлень за кожен день.
# В кінці виведіть загальну кількість доставок за робочий
# тиждень та чи виконано тижневу норму в 50 доставок


# total = 0
#
# for day in range(1, 6):
#     deliveries = int(input(f"Enter deliveries for day {day}: "))
#     total += deliveries
#
# print(f"Total deliveries for the week: {total}")
#
# if total >= 50:
#     print("Weekly target achieved!")
# else:
#     print("Weekly target not achieved!")