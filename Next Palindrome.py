times = int(input('How many inputs you will give : '))
for i in range(times):
    num = int(input('Enter a number : '))
    n = 0
    while n > -1:
        if (num + n) == int(str((num + n))[::-1]):
            print(f'{n+num}')
            break
        else:
            n = n+1
