# #task_1
# Користувач вводить свій вік, якщо він працездатного
# віку(18-65) то виведіть фразу «Працездатний/на», інакше
# «Непрацездатний/на»
#
# age = float(input("Enter your age: "))
#
# if 18 <= age <=65:
#     print("Available to work!")
# else:
#     print("Not available to work!")

# #task_2
# До завдання 2 з попереднього заняття добавте додаткову
# перевірку: щоб отримати доступ користувач повинен ще й
# ввести правильний логін secret_login = "AliBaba"

# secret_login = "AliBaba"
# secret_password = "OpenSesame123"
#
# print("Hello!")

# login = input("Enter your user name, please: ")
# password = input("Enter password, please: ")
#
# if login == secret_login and password == secret_password:
#     print("Access allowed!")
# else:
#     print("Access blocked!")

# task_3
# Оформіть чек покупки. Користувач вводить ціну за
# одиницю товару, кількість товару та свій вік.
# Якщо користувач неповнолітній або старший за 65
# років, то застосуйте знижку 15%
#
# price = float(input("Enter price or purchase, please: "))
# quantity = float(input("Enter quantity, please: "))
# age = float(input("Enter your age, please: "))
#
# total = price * quantity
#
# discount = 0
#
# if 18 <= age <= 65:
#     discount = total * 0.15
#     print("Congratulation! You have rights for discount!")
#
# total_price = total - discount
#
# print("      RECIEPT      ")
# print("Purchase amount:", total)
# print("Discount:", discount)
# print("Due for payment:", total_price)


# #task_4
# Орендувати авто можна лише якщо
# ● у вас є ліцензія
# ● ви повнолітні
# ● ви не потрапляли в дтп
# Оцініть якість написаного коду, спробуйте його
# спростити використавши and\or
#
# age = 23
# has_license = "так"
# accidents = 0
#
# if age >= 18:
#   if has_license == "так":
#     if accidents == 0:
#       print("Оренда дозволена")
#     else:
#       print("Оренда заборонена")
#   else:
#     print("Оренда заборонена")
# else:
#     print("Оренда заборонена")


#
# age = 23
# has_license = "yes"
# accidents = 0
#
# if age >= 18 and has_license == "yes" and accidents == 0:
#     print("Renting is permitted!")
# else:
#     print("Renting is prohibited!")


# task_5
# В службі доставки діє акційна пропозиція, чи дорожча
# покупка тим більша знижка на доставку
# Ціна покупки Знижка на доставку
# < 500 грн повна ціна
# 500-1000 -5%
# 1000-2000 -20%
# >2000 доставка безкоштовно
# Напишіть програму яка запитує у користувача ціну
# покупки та виводить загальну вартість(покупки + доставка)
# Базова ціна доставки: 120 грн
# Знижка діє лише на доставку

# price = float(input("Enter price of purchase: "))
#
# delivery = 120
#
# if price < 500:
#     delivery = 120
# elif price < 1000:
#     delivery = 120 * 0.95
# elif price <= 2000:
#     delivery = 120 * 0.80
# else:
#     delivery = 0
#
# total = price + delivery
#
# print("Delivery price:", delivery)
# print("Total price:", total)


# task_6
# Користувач вводить суму кредиту та термін у роках.
# Виберіть відсоткову ставку за такими умовами:
# ● Для кредиту до 10 000$ на термін до 3 років – ставка
# 8%
# ● Для кредиту до 10 000$ на термін понад 3 роки –
# ставка 10%
# ● Для кредиту від 10 001$ до 50 000$ на термін до 3
# років – ставка 12%
# ● Для кредиту від 10 001$ до 50 000$ на термін понад 3
# роки – ставка 14%
# ● Для кредиту від 50 000$ на будь-який термін – ставка
# 20%
# Виведіть відсоткову ставку, загальну суму кредиту та
# щомісячний платіж
# Загальна сума кредиту вираховується так
#
# credit = float(input("Enter loan amount: "))
# year = int(input("Enter the loan term in years: "))
#
# if credit <= 10000:
#     if year <= 3:
#         percent = 8
#     else:
#         percent = 10
#
# elif credit <= 50000:
#     if year <= 3:
#         percent = 12
#     else:
#         percent =14
# else:
#     percent = 20
#
#
# total = credit * (1 + percent / 100) ** year
# monthly_payment = total / (year * 12)
#
# print("Interest rate:", percent, "%")
# print("Total loan amount:", total)
# print("Monthly payment:", monthly_payment)
