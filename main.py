"""
Created on Wed Dec 11 14:10:47 2019

@author: SERHIR Mohamed
"""
import math

# main python program


response = ['Welcome to smart calculator', 'Hello user !', 'Thanks for enjoy with me',
            'Sorry ,this is beyond my ability']


# fetching tokens from the text command
def extract_from_text(text):
    l = []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l


# calculating LCM
def lcm(a, b):
    L = a if a > b else b
    while L <= a * b:
        if L % a == 0 and L % b == 0:
            return L
        L += 1


# calculating HCF
def hcf(a, b):
    H = a if a < b else b
    while H >= 1:
        if a % H == 0 and b % H == 0:
            return H
        H -= 1


# Addition
def add(a, b):
    return a + b


# Subtraction
def sub(a, b):
    return a - b


# Multiplication
def mul(a, b):
    return a * b


# Division
def div(a, b):
    return a / b


# Remainder
def mod(a, b):
    return a % b


def cos(a):
    return math.cos(a)

def sin(a):
    return math.sin(a)

# Response to command
# printing - "Thanks for enjoy with me" on exit
def end():
    print(response[2])
    input('press enter key to exit')
    exit()


def my_name():
    print(response[1])


def sorry():
    print(response[3])


# Operations - performed on the basis of text tokens
operations = {'ADD': add, 'PLUS': add, 'SUM': add, 'ADDITION': add, 'AJOUTER': add, "AJOUTE": add,
              'SUB': sub, 'SUBTRACT': sub, 'MINUS': sub, 'DIFFERENCE': sub,
              'LCM': lcm, 'PPCM': lcm,
              'HCF': hcf, 'PGCD': hcf,
              'PRODUCT': mul, 'MULTIPLY': mul, 'MULTIPLICATION': mul,
              'DIVISION': div, 'DIVIDE': div, 'DIVISE': div,
              'MOD': mod, 'REMANDER': mod, 'MODULAS': mod,}

operationsSimpleVar = {'COS': cos, 'COSINUS': cos,
                       'SIN': sin, 'SINUS': sin,
                       'TAN': tan, 'TANGENTE': tan,
                       'ACOS': acos, 'ARCOSINUS': acos, 'ARC COSINUS': acos, 'COSINUS INVERSE': acos, 'COS INVERSE': acos,
                       'ASIN': acos, 'ARCSINUS': acos, 'ARC SINUS': acos, 'SINUS INVERSE': acos,'SIN INVERSE': acos, 
                       'ATAN': acos, 'ARCTAN': acos, 'ARC TANGENTE': acos, 'TAN INVERSE': acos, 'TANGENTE INVERSE': acos,
                       'PUISSANCE': power, 'POWER': power, 'PUISS': power, 'POW': power,
                       'PUISSANCE10': power_10, 'PUISS10': power_10, 'POW10': power_10, 'PUISSANCE 10': power_10,
                       'LOG': log_10, 'LOG10': log_10, 'LOGARITHME10': log_10, 'LOG DE 10': log_10,
                       'LN': log_2, 'LOG2': log_2, 'LOGARITHME2': log_2, 'LOG DE 2': log_2,
                       'EXP': exp, 'EXPONENTIELLE': exp, 'EXPONENTIEL': exp,
                       'PUISSANCE 3': x_pow_three, 'PUISSANCE3': x_pow_three, 'PUISS3': x_pow_three, 'POW3': x_pow_three,
                       'RACINECARREE': sqrt, 'RACINE CARREE': sqrt, 'SQRT': sqrt
                       'POURCENTAGE': percent, 'PERCENT': percent}

# commands
commands = {'NAME': my_name, 'EXIT': end, 'END': end, 'CLOSE': end}

print('----' + response[0] + '-----')
print('----' + response[1] + '-----')
while True:
    print()
    text = input('enter your queries: ')
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l = extract_from_text(text)
                r = operations[word.upper()](l[0], l[1])
                print(r)
            except:
                print('something went wrong going plz enter again !!')
            finally:
                break
        elif word.upper() in operationsSimpleVar.keys():
            try:
                l = extract_from_text(text)
                r = operationsSimpleVar[word.upper()](l[0])
                print(r)
            except:
                print('something went wrong going plz enter again !!')
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break
        else:
            sorry()
