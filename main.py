a=str(input(''))
b=a.split(' ')

for i in range(len(b)):
    for k in range(len(b[i])):
        print(b[i][-k-1])