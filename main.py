string = input('Введите строку')    #ввод строки
word_list = string.split(' ')    #создание списка слов
for word in word_list:    #перебор по словам
    for k in range(len(word)):    #перебор по буквам
        print(word[-k-1], end='')    #переворот слова
    print(' ')
