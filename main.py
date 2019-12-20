"""
Created on Wed Dec 11 14:10:47 2019

@author: SERHIR Mohamed & ZARGA Ines
"""

import math
import numpy as np
from sympy import symbols, Eq, solve

# main python program
response = ['Welcome to smart calculator', 'Hello ', 'Thanks for enjoy with me',
            'Sorry ,this is beyond my ability', 
            'To play with this calculator, write what you want to do, for example add or subtract', 
            'If you want to know every command, tap help']


# fetching tokens from the text command
def extract_from_text(text):
    l = []
    for t in text.split(' '):
        if t.upper() == 'PI':
            t = math.pi
        elif t.upper() == "E":
            t = math.e
        elif t.upper() == "LAST":
            t = lastQuery
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


# Cosinus
def cos(a):
    return math.cos(a)


# Sinus
def sin(a):
    return math.sin(a)


# Tan
def tan(a):
    return math.tan(a)


# Acosus
def a_cos(a):
    return math.acos(a)


# Asinus
def a_sin(a):
    return math.asin(a)


# Atan
def a_tan(a):
    return math.atan(a)


# Puissance
def power(a, b):
    #print(a,b, "pow")
    return math.pow(a, b)


# Puissance 10
def power_ten(a):
    return math.pow(10, a)


# Log
def log_ten(a):
    return math.log10(a)


# Ln
def log_two(a):
    return math.log2(a)


# Exponentiel
def exp(a):
    return math.exp(a)


# X power 3
def x_pow_three(a):
    return math.pow(a, 3)


# Racine carree
def sqrt(a):
    return math.sqrt(a)


# Racine n-ieme
def n_sqrt(a, n):
    return power(a, 1.0 / n)


# Percent
def percent(a):
    return a / 100


# Pi
def pi():
    return math.pi


# Exponential
def e():
    return math.e


# Factorial
def fact(a):
    return math.factorial(a)


# To find delta
def find_delta(a, b, c):
    return b * b - 4 * a * c


# To find gcd
def gdc(a, b):
    return math.gcd(int(a),int(b))


# To convert to degree
def degree(a):
    return math.degrees(a)


# To convert to radian
def radian(a):
    return math.radians(a)


# To print the next var (usefull for pi for example)
def print_var(a):
    return a

# TVA HT
def tva_ttc_to_ht(a):
    tva_percent = input("Percent of the tva ?: ")
    return a / (1 + float(tva_percent) / 100)


# TVA TTC
def tva_ht_to_ttc(a):
    tva_percent = input("Percent of the tva ?: ")
    return a * (float(tva_percent) / 100) + a


# Equation du second degre
def sde(a, b, c):
    if a != 0 and b != 0 and c != 0:
        print("Your equation: ", a, "x²+", b,"x+",c)
        rep = input("yes or no ? (y / n)\n")
        if rep == "n" or rep == "no":
            return "Nothing"
        #calcul of delta 
        delta = find_delta(a, b, c)

        # coeff = [a,b,c]
        # print(np.roots(coeff)[0]) possible avec numpy mais affichage meilleur ci dessous:
        if delta > 0:
            result = "x1 = " + str((-b - math.sqrt(delta)) / (2 * a)) + " and x2 = " + str((-b + sqrt(delta)) / (2 * a))
        elif delta < 0:
            result = "x1 = " + str((-b) / (2 * a)) + " -" + str(round(math.sqrt(-delta) / (2 * a),2)) + "i and x2 = " \
                    + str((-b) / (2 * a)) + " +" + str(round(math.sqrt(-delta) / (2 * a),2)) + "i"
        else:
            result = [-b / (2 * a)]
    else:
        #Input the 3 variable of the equation
        print("Please enter your equation ax² + bx + c with a > 0")
        a = input("a= ")
        b = input("b= ")
        c = input("c= ")
        #verify if the equation is good
        print("Your equation: ", a, "x²+", b,"x+",c)
        rep = input("yes or no ? (y / n)\n")

        if rep == "n" or rep == "no":
            return "Nothing"
        #verify if the 3 variables are numbers
        try:
            a = float(a)
            b = float(b)
            c = float(c)
        except: #if not, re enter the 3 variables
            print("Please do it again (your vars are not correct...)")
            return ""

        delta = find_delta(a, b, c)
        if delta > 0:
            x1 = - 1 * b - math.sqrt(delta) / (2 * a)
            x2 = (-b + sqrt(delta)) / (2 * a)
            result = "x1 = " + str(x1) + " and x2 = " + str(x2)
        elif delta < 0:
            result = "x1 = " + str((-b) / (2 * a)) + " -" + str(round(math.sqrt(-delta) / (2 * a),2)) + "i and x2 = " \
                    + str((-b) / (2 * a)) + " +" + str(round(math.sqrt(-delta) / (2 * a),2)) + "i"
        else:
            result = [-b / (2 * a)]

        '''
        x = array([1, 3, 4, 6])
        y = array([2, 3, 5, 1])
        plot(x, y)

        show() 
        '''
        
    return result

# Equation 2 unknown
def equation(a,b,c,d,e,f):
    #if we enter "equation a b c d e" :
    if a != 0 and b != 0 and c != 0 and d != 0 and e != 0 and f != 0 :
        #display the 2 equations
        print("Your equations: ")
        print(a,"x +", b, "y = ", c)
        print(d,"x +", e, "y = ", f)
        rep = input("yes or no ? (y / n)\n")
        if rep == "n" or rep == "no":
            return "Nothing"
        #We use the import symbols, Eq, solve for solve the two equation
        x, y = symbols('x y')

        #define the two equations :
        eq1 = Eq(a*x +b*y + c)
        eq2 = Eq(d*x + e*y + f)
        #solve te equation eq1 eq2 with the variable x and y 
        sol_dict = solve((eq1,eq2), (x, y))

        if a * d - b*c == 0:
            print("The determinant is null, so the equations can't be resolve \n a * d - b*c = 0")

        #display the result which is in the dictionary sol_dict 
        result = f'x = {sol_dict[x]}' + "and" + f'y = {sol_dict[y]}'
    else:
        print("Please enter the 2 equations :")
        print("ax + by = c")
        print("dx + ey = f")
        #Input the 6 variable of the equation
        a = input("a= ")
        b = input("b= ")
        c = input("c= ")
        d = input("d= ")
        e = input("e= ")
        f = input("f= ")

        print("Your equations: ")
        print(a,"x +", b, "y = ", c)
        print(d,"x +", e, "y = ", f)

        rep = input("yes or no ? (y / n)\n")
        if rep == "n" or rep == "no":
            return "Nothing"
        #verify if the 6 variables are numbers
        try:
            a = float(a)
            b = float(b)
            c = float(c)
            d = float(d)
            e = float(e)
            f = float(f)
        except:
            print("Please do it again (your vars are not correct...)")
            return ""
        x, y = symbols('x y')

        eq1 = Eq(a*x +b*y + c)
        eq2 = Eq(d*x + e*y + f)
        #verify if the determinant is null or not 
        if a * d - b*c == 0:
            print("The determinant is null, so the equations can't be resolve \n a * d - b*c = 0")

        sol_dict = solve((eq1,eq2), (x, y))

        result = f'x = {round(sol_dict[x],2)}' + " and " + f'y = {sol_dict[y]}'
        
    return result


# Response to command
# printing - "Thanks for enjoy with me" on exit
def end():
    print(response[2])
    input('press enter key to exit')
    exit()


def my_name(name):
    print(name)

def sorry():
    print(response[3])

def version():
    print ("Version 1.0 by Serhir & Zarga !")

def help_():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("You can type what you need, this calculator can do the following queries: \
        \n- With 1 value: \n  Cos,  Sin, Tan, acos, asin, atan, Puissance, Log, Ln, Exp, Radian, Degree, ttc, ht, factorial, percent \
        \n     Example: Sin 5 \
        \n- With 2 values: \n  Add, Sub, LCM, HCF, Mutiplication, Division, Modulo, Racine_Nieme, gcd ( + and - working too) \
        \n     Example: Please add 7 and 7 \
        \n- With 3 values: \n  SDE (second-degree equation) \
        \n     Example: Sde 6 8 -5 \
        \n- With 6 values: \n  Equation (2 equation solution) \
        \n     For: ax + by = c and dx + ey = f: \
        \n     Example: Equation 6 8 -5 2 -7 6 \
        \nYou can use only sde keyword or equation and follow the instructions \
        \n If you need to do more operation you can use the functionnality last, for example you can add 1 and 1 and do last + 10, \
        \n  last is the last operation in memory and the result will be 12\
        \nYou can find delta by typing delta a b c, with abc your values\
        \nYou can print your last operation by typing print\
        \nYou can also quit by typing the keyword quit or exit, and you can know your name by typing name")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# Operations - performed on the basis of text tokens
operationsSimpleVar = {'COS': cos, 'COSINUS': cos, 'COSINE': cos,
                       'SIN': sin, 'SINUS': sin,
                       'TAN': tan, 'TANGENTE': tan, 'TANGENT': tan,
                       'ACOS': a_cos, 'ARCOSINUS': a_cos, 'ARC_COSINUS': a_cos, 'ARC_COSINE': a_cos,'COS_INVERSE': a_cos, 'COSINUS_INVERSE': a_cos, 'COSINE_INVERSE': a_cos,
                       'INVERSE_COS': a_cos, 'INVERSE_COSINUS': a_cos, 
                       'ASIN': a_sin, 'ARCSINUS': a_sin, 'ARC_SINUS': a_sin, 'SINUS_INVERSE': a_sin, 'SIN_INVERSE': a_sin, 'INVERSE_SIN': a_sin, 'INVERSE_SINUS': a_sin,
                       'ATAN': a_tan, 'ARCTAN': a_tan, 'ARC_TANGENTE': a_tan, 'TAN_INVERSE': a_tan, 'TANGENTE_INVERSE': a_tan,'TANGENT_INVERSE': a_tan, 'INVERSE_TANGENT': a_tan,
                       'PUISSANCE10': power_ten, 'PUISS10': power_ten, 'POW10': power_ten, 'PUISSANCE_10': power_ten, '^10': power_ten, 'POWER10': power_ten,
                       'LOG': log_ten, 'LOG10': log_ten, 'LOGARITHME10': log_ten, 'LOG DE 10': log_ten, 'LOGARITHM10': log_ten,
                       'LN': log_two, 'LOG2': log_two, 'LOGARITHME2': log_two, 'LOG DE 2': log_two, 'LOGARITHM2': log_two,
                       'EXP': exp, 'EXPONENTIELLE': exp, 'EXPONENTIEL': exp, 'EXPONENTIAL': exp,
                       'PUISSANCE_3': x_pow_three, 'PUISSANCE3': x_pow_three, 'PUISS3': x_pow_three, '^3': x_pow_three, 'POW3': x_pow_three,
                       'RACINECARREE': sqrt, 'RACINE_CARREE': sqrt, 'SQRT': sqrt, 'RACINECARRE': sqrt, 'SQUARE_ROOT': sqrt,
                       'POURCENTAGE': percent, 'PERCENT': percent,
                       'FACTORIEL': fact, 'FACT': fact, 'FACTORIELLE': fact, "FACTO": fact, 'FACTORIAL': fact,
                       'PRINT': print_var, 'AFFICHE': print_var,
                       'RADIAN': radian, 'RADIANS': radian,
                       'DEGREE': degree, 'DEGREES': degree,
                       'TTC': tva_ht_to_ttc,
                       'HT': tva_ttc_to_ht}

operationsDoubleVar = {'ADD': add, 'PLUS': add, 'SUM': add, 'ADDITION': add, 'AJOUTER': add, "AJOUTE": add, "+": add, "AND": add,
              'SUB': sub, 'SUBTRACT': sub, 'MINUS': sub, 'DIFFERENCE': sub, '-': sub, 'ENLEVE': sub, 'ENLEVER': sub,
              'LCM': lcm, 'PPCM': lcm,
              'HCF': hcf, 
              'PRODUCT': mul, 'MULTIPLY': mul, 'MULTIPLICATION': mul, '*': mul,
              'PUISSANCE': power, 'POWER': power, 'PUISS': power, 'POW': power, '^': power,
              'DIVISION': div, 'DIVIDE': div, 'DIVISE': div, '/': mul,
              'MOD': mod, 'REMANDER': mod, 'MODULAS': mod, 'MODULO': mod, '%': mod,
              'RACINE_NIEME': n_sqrt,
              'GCD': gdc, 'PGCD': gdc
              }

operationsThreeVar = {'SDE': sde, 'DELTA': find_delta}
operationsSixVar = {'EQUATION': equation}


# Commands
commands = {'NAME': my_name, 'EXIT': end, 'END': end, 'CLOSE': end, 'QUIT': end, 'HELP': help_, 'VERSION': version}

name = input("What is your name? ")
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('---- \t' + response[0] + '\t\t\t\t\t\t\t\t -----')
print('---- \t' + response[1]+ name + '\t\t\t\t\t\t\t\t\t\t -----') 
print('---- \t' + response[4] + '\t -----')
print('---- \t' + response[5] + '\t\t\t\t\t\t -----')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

lastQuery = 0
while True:
    print()
    text = input('Enter your queries: ')
    for word in text.split(' '):
        if word.upper() in operationsSimpleVar.keys():
            try:
                l = extract_from_text(text)
                r = operationsSimpleVar[word.upper()](l[0])
                lastQuery = r
                print(r)
            except:
                print('Something went wrong going please enter again !')
            finally:
                break
        elif word.upper() in operationsDoubleVar.keys():
            try:
                l = extract_from_text(text)
                r = operationsDoubleVar[word.upper()](l[0], l[1])
                lastQuery = r
                print(r)
            except:
                print('Something went wrong going please enter again !')
            finally:
                break
        elif word.upper() in operationsThreeVar.keys():
            try:
                l = extract_from_text(text)
                if len(l) == 3:
                    r = operationsThreeVar[word.upper()](l[0], l[1], l[2])
                else:
                    r = operationsThreeVar[word.upper()](0,0,0)
                lastQuery = r
                print(r)
            except:
                print('Something went wrong going please enter again !')
            finally:
                break
        elif word.upper() in operationsSixVar.keys():
            try:
                l = extract_from_text(text)
                if len(l) == 6:
                    r = operationsSixVar[word.upper()](l[0], l[1], l[2], l[3], l[4], l[5])
                else:
                    r = operationsSixVar[word.upper()](0,0,0,0,0,0)
                lastQuery = r
                print(r)
            except:
                print('Something went wrong going please enter again !')
            finally:
                break
        elif word.upper() in commands.keys():
            if commands[word.upper()] == my_name:
                my_name(name)
            else:
                commands[word.upper()]()
            break  
    else:
        sorry()