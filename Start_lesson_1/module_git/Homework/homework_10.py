#task_1
# Завдання 1
# Напишіть програму для роботи онлайн магазину.
# Товари:
# ● подушка – 650 грн
# ● ковдра – 1700 грн
# ● лампа – 500 грн
# ● брелок – 60 грн
# Меню дій:
# ● додати товар
# ● видалити товар
# ● очистити кошик
# ● показати вміст кошики та суму покупки
# ● вихід
# Користувачу показується меню один раз на початку
# програми
# Користувач вибирає номер дії після чого за потреби
# вводить назву товару то його кількість
# У випадку неправильно введених даних повідомити про
# це та повернутись до вибору номера дії
# Створіть для кожного товару змінну з кількістю цього
# товару у кошику для подальшої роботи

#
# pillow = 0
# blanket = 0
# lamp = 0
# keychain = 0
#
# print("ONLINE STORE")
# print("Products:")
# print("pillow - 650 UAH")
# print("blanket - 1700 UAH")
# print("lamp - 500 UAH")
# print("keychain - 60 UAH")
#
# print("\nMENU:")
# print("1 - Add product")
# print("2 - Remove product")
# print("3 - Clear cart")
# print("4 - Show cart and total")
# print("5 - Exit")
#
# while True:
#     choice = input("\nChoose an action (1-5): ")
#
#     if choice == "1" or choice == "2":
#         product = input("Enter product name: ").lower()
#
#         if product not in ["pillow", "blanket", "lamp", "keychain"]:
#             print("Invalid product!")
#             continue
#
#         quantity = input("Enter quantity: ")
#
#         if not quantity.isdigit() or int(quantity) == 0:
#             print("Invalid quantity!")
#             continue
#
#         quantity = int(quantity)
#
#         if choice == "1":
#             if product == "pillow":
#                 pillow += quantity
#             elif product == "blanket":
#                 blanket += quantity
#             elif product == "lamp":
#                 lamp += quantity
#             elif product == "keychain":
#                 keychain += quantity
#
#             print("Product added!")
#
#         elif choice == "2":
#             if product == "pillow" and pillow >= quantity:
#                 pillow -= quantity
#             elif product == "blanket" and blanket >= quantity:
#                 blanket -= quantity
#             elif product == "lamp" and lamp >= quantity:
#                 lamp -= quantity
#             elif product == "keychain" and keychain >= quantity:
#                 keychain -= quantity
#             else:
#                 print("Not enough products in cart!")
#                 continue
#
#             print("Product removed!")
#
#     elif choice == "3":
#         pillow = 0
#         blanket = 0
#         lamp = 0
#         keychain = 0
#         print("Cart cleared!")
#
#     elif choice == "4":
#         total = (pillow * 650 + blanket * 1700 +
#                  lamp * 500 + keychain * 60)
#
#         print("\nYOUR CART:")
#         print("Pillow:", pillow)
#         print("Blanket:", blanket)
#         print("Lamp:", lamp)
#         print("Keychain:", keychain)
#         print("Total:", total, "UAH")
#
#     elif choice == "5":
#         print("Thank you for shopping!")
#         break
#
#     else:
#         print("Invalid action! Choose 1-5.")
