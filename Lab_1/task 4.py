#Анаграммами называются слова, образованные путем взаимной
#перестановки букв. В английском языке, например, анаграммами
#являются слова «live» и «evil», а в русском – «выбор» и «обрыв».
#Напишите программу, которая будет запрашивать у пользователя два
#слова, определять, являются ли они анаграммами, и выводить на экран
#ответ

while True:
    word1 = input("Введите первое слово (0-exit): ")
    if word1 != "0":
        word2 = input("Введите второе слово: ")
        if sorted(word1) == sorted(word2):
            print("Являются анаграммами")
        else:
            print("не являются анаграммами")
    else:
        break
