#task_1
# Завдання 1
# Користувач вводить слово та індекс. Замініть символ під
# цим індексом на *. Скористайтесь зрізами
# Приклади:
# hello 1 – h*llo
# hello 2 – he*lo

#
# word = input("Enter a word: ")
# index = int(input("Enter index: "))
#
# print(f"{word[:index]}*{word[index + 1:]}")

#task_2
# Користувач вводить слово. Зробіть першу та останню
# літеру великою. Виправіть помилку в коді
# word = input("Введіть слово: ")
#
# result = word[0].isupper() + word + word[-1].isupper()   #should be .upper  and word[1:-1]
#
# print(result)

# word = input("Enter a word: ")
#
# result = word[0].upper() + word[1:-1] + word[-1].upper()
#
# print(result)


#task_3
# Користувач вводить слова, поки не введе END. Виведіть в
# кінці ті слова, які починаються і закінчуються на одну і ту
# саму літеру(регістр не важливий).
# Приклади: око, дід, Ротор, Ангора

# words = []
#
# while True:
#     word = input("Enter a word: ")
#
#     if word == "END":
#         break
#
#     if word and word[0].lower() == word[-1].lower():
#         words.append(word)
#
# print("Result:", words)