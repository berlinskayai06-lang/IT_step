# #task_1
# print("Hello!")
#
# minutes = int(input("Enter minutes: "))
# seconds = minutes * 60
#
# if minutes > 0:
#     print(f"Result is {seconds} in {minutes} minutes")
# else:
#     print("Sorry, the number can not be negative!")
#     print("Please, try again!")


# #task_2
# secret_password = "OpenSesame123"
#
# print("Hello!")

# password = input("Enter password, please: ")

# if password == secret_password:
#     print("Access allowed!")
# else:
#     print("Access blocked!")

#task_3
# meters = float(input("Enter meters: "))
# unit_of_meas = input("Enter transfer to (cm, km): ")

# if unit_of_meas == "cm":
#     centimeters = meters * 100
#     print(f"Distance in centimeters is: {centimeters}")
# elif unit_of_meas == "km":
#     kilometers = meters / 1000
#     print(f"Distance in kilometers is: {kilometers}")
# else:
#       print("Unknown unit of measurment!")
#

# #task_4
# answer = input("Відповідь на Велике Питання Життя, Всесвіту і Всього Іншого: ")
#
# if answer == "42":
#  print("Правильно")
#
# elif answer == "сорок два":
#  print("Правильно")
#
# elif answer == "сорок-два":
#  print("Правильно")
#
# else:
#  print("Не правильно")
#
# # #elif answer == "42":     #we already have this variant with "if", always will work firs suitable variant
# #  print("Правильно")


# #task_5
# grade = int(input("Введіть оцінку: "))
# if grade == 2:
#    print("Незадовільно")
# if grade == 3:
#    print("Задовільно")
# if grade == 4:
#    print("Добре")
# if grade == 5:
#    print("Відмінно")
# else:
# #    print("Оцінка має бути від 2 до 5")
# #


#
# grade = int(input("Введіть оцінку: "))

# if grade == 2:
#    print("Незадовільно")
# elif grade == 3:
#    print("Задовільно")
# elif grade == 4:
#    print("Добре")
# elif grade == 5:
#    print("Відмінно")
# else:
#    print("Оцінка має бути від 2 до 5")

# #i changed "if" to "elif"


#
# #task_6
# price = float(input("Price of one pizza: "))
# count = int(input("Quantity of pizza`s: "))
# budget = float(input("Budget: "))
#
# total = price * count
#
# if budget >= total:
#     print("The budget will be sufficient")
# else:
#     print("The budget will not be sufficient:", budget - total)


# #extra_task
# number = int(input("Enter a number: "))
#
# if number % 2 == 0:
#     print(number, "Even number")
# else:
#     print(number, "Odd number")

#
# #extra_task2
# number = int(input("Enter a number: "))
#
# if number % 7 == 0:
#     print(number, "Number is multiple 7")
# else:
#     print(number, "Number is not multiple 7")



# #extra_task3
# number_1 = int(input("Enter the first number: "))
# number_2 = int(input("Enter the second number: "))
#
# if number_1 > number_2:
#     print(number_1)
# else:
#     print(number_2)


# #extra_task4
# number_1 = int(input("Enter the first number: "))
# number_2 = int(input("Enter the second number: "))
#
# if number_1 < number_2:
#      print(number_1)
# else:
#      print(number_2)