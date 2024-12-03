a = (input('')    #ввод строки
b = a.split(' ')    #создание списка слов
for i in range(len(b)):    #перебор по словам
    for k in range(len(b[i])):    #перебор по буквам
        print(b[i][-k-1])    #переворот слова
