#task_1
# Завдання 1
# Щоб створити одну глиняну фігурку треба 130 грам
# глини.
# Користувач вводить масу глини в кілограмах. Виведіть
# скільки фігурок він зможе зробити.
# Наприклад, з 2 кг глини можна зробити 15 фігурок
# Розтавте команди нижче у правильному порядку та
# додайте підписи з описом що робить команда
#
# #data
# clay_per_figure = 130  #quantity for one figure
# # clay*= 1000  #i think this line shouldn`t be here, for this meaning we have line "15"
#
# clay = float(input("Введіть масу глини (кг): "))  #user have to enter total quantity
#
# #counting
# figures = clay // clay_per_figure  #counting how many figures could be done
#
# #result
# print(f"Можна зробити: {figures} фігурок")  #shows result of counting


#task_2
# Троє друзів пішли на рибалку. Програма отримує
# кількість риби яку зловив кожен рибалка.
# Виведіть на екран:
# ● скільки в середньому вийшло риб на людину
# ● розмір найбільшого улову

# first_fisher = int(input("First fisher: "))
# second_fisher = int(input("Second fisher: "))
# third_fisher = int(input("Third fisher: "))
#
# print("Average number of fish:", (first_fisher + second_fisher + third_fisher) / 3)
# print("The biggest catch:", max(first_fisher, second_fisher, third_fisher))



#task_3
# У кінотеатрі можна замовити квитки онлайн
# Місце Ціна
# Звичайне 150 грн
# VIP 250
# Користувач вводить бюджет. Виведіть скільки людей
# може піти в кіно якщо купляти лише звичайні місця або
# лише VIP

# budget = int(input("Enter your budget: "))
#
# ordinary = budget // 150
# vip = budget // 250
#
# print("Ordinary tickets:", ordinary)
# print("VIP tickets:", vip)

# #task_4
# Користувач вводить суму грошей.
# Програма розкладає суму на:
# ● купюри по 500;
# ● купюри по 200;
# ● купюри по 100;
# ● решту
#
# money = int(input("Enter your sum: "))
#
# banknotes_500 = money // 500
# money = money % 500
#
# banknotes_200 = money // 200
# money = money % 200
#
# banknotes_100 = money // 100
# money = money % 100
#
# print("Banknotes 500:", banknotes_500)
# print("Banknotes 200:", banknotes_200)
# print("Banknotes 100:", banknotes_100)
# print("Change:", money)

#task_7 from practice work
# Користувач вводить суму вкладу в банк та відсоток
# ставки.
# ● Обчисліть скільки користувач отримує через 5 років,
# якщо кожного року сума вкладу збільшується на даний
# відсоток
# # ● Виведіть суму вкладу кожного року окремо
#
# deposit = float(input("Enter your deposite: "))
# interest_rate = float(input("Enter interest rate: "))
#
# calculation = 1 + interest_rate / 100
#
# deposit_every_year = deposit * calculation
#
# deposit_year1 = deposit_every_year * calculation
# print("One year: ", deposit_year1)
#
# deposit_year2 = deposit_year1 * calculation
# print("Two years: ", deposit_year2)
#
# deposit_year3 = deposit_year2 * calculation
# print("Three years: ", deposit_year3)
#
# deposit_year4 = deposit_year3 * calculation
# print("Four years: ", deposit_year4)
#
# deposit_year5 = deposit_year4 * calculation
# print("Four years: ", deposit_year5)
#
# print(f"In 5 yaer your deposit will amount to: {deposit_year5: .2f}")


