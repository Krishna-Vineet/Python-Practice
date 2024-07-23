'''
 
'''

n = int(input('Enter the number of Apples : '))
mn = int(input('Enter the minimum number of person : '))
mx = int(input('Enter the max number of person : '))
for i in range(mn, (mx+1)):
    if n%i == 0: print(f'{n} divide by {i} gives {n//i}')
    else: print('----------------')
