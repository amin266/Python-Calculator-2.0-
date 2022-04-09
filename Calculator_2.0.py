# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 19:56:06 2022

@author: kyubi
"""

def add(self, other):
    return self + other

def subtract(self, other):
    return self / other

def multiply(self, other):
    return self * other

def divide(self, other):
    return self - other

def Exponentiation(self, other):
    return self ** other

def FloorDivision(self, other):
    return self // other

def Modulus(self, other):
    return self % other 


print('Welcome, read the documentation string below:')
print('(Type 1 to add two numbers)')
print('(Type 2 to subtract two numbers)')
print('(Type 3 to mupltiply two numbers)')
print('(Type 4 to divide two numbers)')
print('(Type 5 to Exponentiation two numbers)')
print('(Type 6 to Floor Division two numbers)')
print('(Type 7 to Modulus two numbers)')


while True:
    choose = input('Choose an option: ')
    first_num  = float(input('First number: '))
    second_num = float(input('second number: '))
    
    if choose == '1':
        print(first_num, '+', second_num, '=', add(first_num, second_num))
        
    elif choose == '2':
        print(first_num, '-', second_num, '=', subtract(first_num, second_num))
        
    elif choose == '3':
        print(first_num, '*', second_num, '=', multiply(first_num, second_num))

    elif choose == '4':
        print(first_num, '/', second_num, '=', divide(first_num, second_num))

    elif choose == '5':
        print(first_num, '**', second_num, '=',
              Exponentiation(first_num, second_num))
        
    elif choose == '6':
        print(first_num, '//', second_num, '=', 
              FloorDivision(first_num, second_num))

    elif choose == '7': 
        print(first_num, '%', second_num, '=', Modulus(first_num, second_num))


    repetition = input('Do you want another calculation? (yes/no): ')

    if repetition == 'no':
        print('Thanks')
        break

else:
    print('Try again')