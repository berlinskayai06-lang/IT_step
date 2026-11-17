# task_1
# Каса кінотеатру розраховує вартість квитка в залежності
# від віку користувача:
# Вік Ціна квитка
# <12 80 грн
# 12-65 200 грн
# 65+ 120 грн
# Користувач вводить свій вік, виведіть вартість квитка.
# Також програма в кінці повинна побажати гарного дня.

# age = int(input("Enter your age, please: "))
#
# if age < 12:
#     price = 80
# elif age < 65:
#     price = 200
# else:
#     price = 120
#
# print("Ticket price is:", price, "uah")
# print("Have a nice day!")

# task_2
# Інший розробник намагався написати програму яка
# автоматично визначає категорію товару за її вагою, але
# програма завжди видає “Дрібна посилка”
# Виправіть проблему
#
# weight = float(input("Введіть вагу товару в кг: "))
# if weight < 1:
#  print("Дрібна посилка")
# elif weight < 5:
#  print("Середня посилка")
# elif weight < 10:
#  print("Велика посилка")
# else:
#  print("Надважка посилка") #as we disscused here is no error

# task_3
# Користувач вводить назву місяця та число. Потрібно
# вивести яке сьогодні свято.
# Якщо сьогодні звичайний день то так і сказати
# користувачу.
# див наступну сторінку
# Дата Свято
# 1 січня Новий рік
# 14 лютого день св Валентина
# 25 грудня Різдво
# 1 квітня день сміху

# month = input("Enter the month, please: ").lower() # i found this command can recognize capital and small letters
# day = int(input("Enter the date, please: "))
#
# if month == "january" and day == 1:
#     print("New year")
# elif month == "february" and day == 14:
#     print("Valentine`s Day")
# elif month == "december" and day == 25:
#     print("Christmas")
# elif month == "April" and day == 1:
#     print("April Fool`s Day")
# else:
#     print("Today is usual day!")

# task_4
# У завданні 1 треба купити білети трьом людям.
# Змініть код таким чином щоб можна було ввести три
# числа(вік трьох людей) та вивести скільки коштує білет
# для кожної людини окремо.
# Також вивести загальну суму.
#
# age_1 = int(input("Enter age of first person: "))
# age_2 = int(input("Enter age of second person: "))
# age_3 = int(input("Enter age of third person: "))
#
# if age_1 < 12:
#     price_1 = 80
# elif age_1 < 65:
#     price_1 = 200
# else:
#     price_1 = 120
#
# if age_2 < 12:
#     price_2 = 80
# elif age_2 < 65:
#     price_2 = 200
# else:
#     price_2 = 120
#
# if age_3 < 12:
#     price_3 = 80
# elif age_3 < 65:
#     price_3 = 200
# else:
#     price_3 = 120
#
# total = price_1 + price_2 + price_3
#
# print("Ticket for first person:", price_1, "uah")
# print("Ticket for second person:", price_2, "uah")
# print("Ticket for third person:", price_3, "uah")
#
# print("Total price:", total, "uah")
# print("Have a nice day!")

# task_5
# Користувач вводить назву товару, програма повинна
# перевірити чи можна продати цей товар
# Якщо хочуть купити алкоголь або тютюн то спитайте
# вік. Продаж дозволено з 18 років
# Якщо це ліки то попросіть рецепт від лікаря.(див
# далі)
# Всі інші товари дозволені без будь-яких умов
# Розставте код нижче у правильному порядку та з
# правильними відступами. Деякі блоки можна
# використати 2 рази. Додайте коментарі
#
# # collecting first data
# product = input("Enter the product name: ").lower()
#
# # first checking
# if product == "alcohol" or product == "tabaco":
#     age = int(input("Enter your age: "))
#
#     # age checking
#     if age >= 18:
#         print("Approved for sale")
#     else:
#         print("Sale prohibited ")
#
# # second checking
# elif product == "medicine":
#     prescription = input("Do you have a prescription? ")
#
#     # prescription checking
#     if prescription == "yes":
#         print("Approved for sale")
#     else:
#         print("Sale prohibited")
#
# # all other staffs
# else:
#     print("Approved for sale")
#

# task_6
# Для того щоб оформити замовлення в онлайн
# магазині потрібно зайти на сайт, добавити товар в кошик
# та оплатити замовлення.
# Нижче наведено код цієї програми
# is_logged_in = input("Ви увійшли в систему? (так/ні): ")
# cart_is_empty = input("Ваш кошик порожній? (так/ні): ")
# balance = float(input("Введіть баланс: "))
# total_price = float(input("Введіть вартість замовлення: "))
# if is_logged_in == "так":
# if cart_is_empty == "ні":
# if balance >= total_price:
# print("Замовлення успішно оформлено!")
# else:
# print("Недостатньо коштів на рахунку")
# else:
# print("Ваш кошик порожній")
# else:
# print("Будь ласка, увійдіть в систему")
# Спробуйте позбутись вкладених умов. Для цього
# перевіряйте спочатку що не так(наприклад не зайшли на
# сайт) і лише в кінці після всіх перевірок підтвердіть
# замовлення.
# Можете скористатись Student Helper

# is_logged_in = input("Ви увійшли в систему? (так/ні): ")
#
# if is_logged_in == "так":
#     cart_is_empty = input("Ваш кошик порожній? (так/ні): ")
#
#     if cart_is_empty == "ні":
#         balance = float(input("Введіть баланс: "))
#         total_price = float(input("Введіть вартість замовлення: "))
#
#         if balance >= total_price:
#             print("Замовлення успішно оформлено!")
#         else:
#             print("Недостатньо коштів на рахунку")
#     else:
#         print("Ваш кошик порожній")
# else:
#     print("Будь ласка, увійдіть в систему")

# task_7
# Користувач вводить швидкість.
# Якщо швидкість більша за 90км\год – спитати де саме
# він
# їде: місто чи траса. Якщо в місті то повідомити про
# штраф, якщо траса то попередження
# Якщо швидкість менша за 20км/год – спитати скільки
# років машині. Якщо їй більше 15 років – запропонувати
# купити нову, інакше запропонувати поїхати на СТО
# Інша швидкість – побажати гарної подорожі.
#
# speed = float(input("Enter your currently speed: "))
#
# if speed > 90:
#     place = input("Where are you driving? (city/highway): "). lower()
#
#     if place == "city":
#         print("You have to pay a bill!")
#     else:
#         print("Warning! Reduce speed!")
#
# elif speed < 20:
#     age = int(input("How old are your car? "))
#
#     if age > 15:
#         print("Recommendation to buy a new car!")
#     else:
#         print("Recommendation go to a service station!")
