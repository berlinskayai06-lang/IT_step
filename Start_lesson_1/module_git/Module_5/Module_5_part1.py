# У файлі module_git/src/library.py реалізуйте програму
# роботи бібліотеки. Виконайте завдання в декілька кроків та
# збережіть відповідними комітами
# Коміт 1
# Виведення меню
# 1. Отримати книжку
# 2. Вихід
# Реалізуйте нескінченним циклом
# Якщо користувач хоче отримати книжку, попросіть
# ввести його своє ім’я та назву книжки
# Після чого виведіть фразу
# Книжку … видано читачеві …
# Коміт 2
# Додайте пункт меню
# 2. Повернути книжку
# пункт виходу зробіть номером 3
# Якщо користувач хоче повернути книжку то ви просите
# його ввести своє ім’я та назву книжки
# Після чого виведіть фразу
# Читач … повернув книжку …
# Коміт 3
# Коли користувач хоче взяти книжку додатково спитайте
# на скільки днів та оновіть повідомлення до
# Книжку … видано читачеві … на … днів
# Коміт 4
# Займіться рефакторингом
# Якщо у вас двічі написаний код який запитує
# користувача ім’я та нозву книжки то напишіть його 1 раз
# пере if
# Коміт 5
# Добавте перевірки значеннь:
# ● ім’я та назва книжки не можуть бути порожніми
# рядками
# ● кількість днів не може бути від’ємною
# ● книжку видають максимум на 30 днів
# Добавте усі зміни на віддалений репозиторій


while True:
    print("1. Get a book")
    print("2. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter your name: ")
        book = input("Enter name of book: ")

        print(f"The book {book} has been issued to {name}")

    elif choice == "2":
        break



while True:
    print("1. Get a book")
    print("2. Return a book")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter your name: ")
        book = input("Enter name of book: ")

        print(f"The book {book} has been issued to {name}")

    elif choice == "2":
        name = input("Enter your name: ")
        book = input("Enter name of book: ")

        print(f"The reader {name} returned the book {book}")

    elif choice == "3":
        break



while True:
    print("1. Get a book")
    print("2. Return a book")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter your name: ")
        book = input("Enter name of book: ")
        days = int(input("For how many days: "))

        print(f"The book {book} has been issued to {name} for {days} days")

    elif choice == "2":
        name = input("Enter your name: ")
        book = input("Enter name of book: ")

        print(f"The reader {name} returned the book {book}")

    elif choice == "3":
        break



while True:
    print("1. Get a book")
    print("2. Return a book")
    print("3. Exit")

    choice = input("Enter an option: ")

    if choice == "3":
        break

    if choice == "1" or choice == "2":
        name = input("Enter your name: ")
        book = input("Enter name of book: ")

        if choice == "1":
            days = int(input("For how many days: "))
            print(f"The book {book} has been issued to {name} for {days} days")

        elif choice == "2":
            print(f"The reader {name} returned the book {book}")