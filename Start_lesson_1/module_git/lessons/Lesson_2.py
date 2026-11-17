# # task_1
# num1 = int(input("enter current balance: "))
# num2 = int(input("price of purchase: "))
# total = num1 - num2
# print("resalt", total)
#
# #task_2
# price = float(input("price for one cup of coffe: "))
# qty = int(input("how many caps: "))
# total = price * qty
# print("Total price", total)
#
# #task_3
# width = float(input("enter the width: "))
# height = float(input("enter the height: "))
# area = width * height
# print("The area is equal to:", area)
#
# #task_4
# inv_amt = float(input("enter the amount: "))
# tips = float(input("percent: "))
# total_tips = inv_amt * tips / 100
# print("Tips:", total_tips)
# total_amount = total_tips + inv_amt
# print("Total: ", total_amount)
#
# #task_5
# distance = float(input("kilometers: "))
# consumption = float(input("liters per 100 km: "))
# price = float(input("price per liter: "))
# total_fuel = distance / 100 * consumption
# print("Total fuel used:", total_fuel)
# total_price = consumption * price
# # print("Total price for fuel:", total_price)
#
# #task_6
# num1 = int(input("first: "))
# num2 = int(input("second: "))
# result_1 = num1 + num2
# result_2 = num1 - num2
# result_3 = num1 * num2
# print("Answers:", result_1, result_2, result_3)
# #i found, that "result" used 3 times same variant for 3 different actions
#
# #task_7
# inv_amt = float(input("enter the amount: "))
# tips = float(input("percent: "))
# qnt = float(input("quantity of persons: "))
# total_tips = inv_amt * tips / 100
# print("Tips:", total_tips)
# total_amount = total_tips + inv_amt
# print("Total: ", total_amount)
# per_payment = total_amount / qnt
# print("Personal payment:", per_payment)

#task_8
sum = float(input("Введіть суму грошей покупця: "))
price = float(input("Введіть вартість товару: "))
change = sum - price
print("Здача:", change)
