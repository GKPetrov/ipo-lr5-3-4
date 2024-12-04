string = input('')    #ввод строки
word_list = string.split(' ')    #создание списка слов
for i in range(len(word_list)):    #перебор по словам
    for k in range(len(word_list[i])):    #перебор по буквам
        print(word_list[i][-k-1], end='')    #переворот слова
    print(' ')
