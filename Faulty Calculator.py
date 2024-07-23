
'''
It will don't show the current answer for: 
2*3 = 8
3+2 = 6
10-6 = 5
'''

print('\n\t P Y T H O N   C A L C U L A T O R \n\n Let\'s calcuclate.')
finish = False
while not finish:
    n1 = int(input('\nEnter first number : '))
    print('1 for *, 2 for /, 3 for +, 4 for -, 5 for //, 6 for ** & 7 for %')
    op = int(input('Enter the operation : '))
    n2 = int(input('Enter second number : '))
    if n1==2 and op==1 and n2==3:
        print(f'The result is : 8')
    elif n1==3 and op==3 and n2==2:
        print(f'The result is : 6')
    elif n1==10 and op==4 and n2==6:
        print(f'The result is : 5')
    else:
        if op==1:
            print(f'The result is : {n1*n2}')
        elif op==2:
            print(f'The result is : {n1/n2}')
        elif op==3:
            print(f'The result is : {n1+n2}')
        elif op==4:
            print(f'The result is : {n1-n2}')
        elif op==5:
            print(f'The result is : {n1//n2}')
        elif op==6:
            print(f'The result is : {n1**n2}')
        else:
            print('Your input is wrong. Please try again')
            pass
    again = input('\nDo you want to calculate more(Y for yes, N for no) : ')
    if again.upper() == 'Y':
        pass
    elif again.upper() == 'N':
        print('Thanks for using this calculator.')
        finish = True
    else:
        continue
