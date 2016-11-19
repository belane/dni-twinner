#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# DNI Twinner - Finds similar ID numbers
# belane 2016

## Globals
NIF = 'TRWAGMYFPDXBNJZSQVHLCKE'
SAME_START = 3
SAME_END = 2

## Functions
def dniLetter(dni):
    ''' calculate control letter '''
    return NIF[int(dni) % 23]

def checkTwin(dni):
    ''' check valid twins '''
    if (
        dniLetter(dni) == original_letter and
        len(str(dni)) == len(str(original_dni)) and
        str(dni) != str(original_dni) and
        str(dni)[0:SAME_START] == str(original_dni)[0:SAME_START] and
        str(dni)[-SAME_END:len(str(dni))] == str(original_dni)[-SAME_END:len(str(dni))]
    ):
        return True

def alternateNumbers(dni, alternates):
    ''' switch numbers positions => 0 '''
    result = []
    for position in range(len(str(dni)) - alternates):
        new_dni = list(str(dni))
        i = new_dni[position]
        new_dni[position] = new_dni[position + alternates]
        new_dni[position + alternates] = i
        dni_final = ''.join(new_dni)
        if (checkTwin(dni_final)):
            #print(dni_final, dniLetter(dni_final), sep='-')
            result.append(dni_final)
    return result

def replaceXNumbers(dni, x):
    ''' replace X consecutive numbers '''
    result = []
    for position in range(len(str(dni)) - (x-1)):
        new_dni = list(str(dni))
        del new_dni[position + 1:position + x]
        for num in range((10**x)-1):
            new_dni[position] = str(num).zfill(x)
            dni_final = ''.join(new_dni)
            if (checkTwin(dni_final)):
                #print(dni_final, dniLetter(dni_final), sep='-')
                result.append(dni_final)
    return result

def bruteForce(dni):
    ''' try all combinations '''
    result = []
    i = len(str(dni)) - SAME_START - SAME_END
    for num in range((10**i)-1):
        dni_final = str(dni)[0:SAME_START]  + str(num).zfill(i) + str(dni)[-SAME_END:len(str(dni))]
        if (checkTwin(dni_final)):
            #print(dni_final, dniLetter(dni_final), sep='-')
            result.append(dni_final)
    return result


## Banner
print('\033[1m' + """
   _     _    _         _
 _| |___|_|  | |_ _ _ _|_|___ ___ ___ ___
| . |   | |  |  _| | | | |   |   | -_|  _|
|___|_|_|_|  |_| |_____|_|_|_|_|_|___|_|
    """ + '\033[0m')

## Main
original_dni = input("DNI nubmer without letter: ") or exit()
SAME_START = int(input(" keep the first digits [" + str(SAME_START) + "]: ") or SAME_START)
SAME_END = int(input(" keep the lasts digits [" + str(SAME_END) + "]: ") or SAME_END)
if (
    len(original_dni) != 8 or
    SAME_START > 4 or SAME_START < 1 or
    SAME_END > 4 or SAME_END < 1
    ): exit()
original_letter = dniLetter(original_dni)
print(" Base ID ", original_dni, "-", original_letter, sep="")
print("__________________________________________\n")

variations = []
variations += alternateNumbers(original_dni, 2) # 0
variations += replaceXNumbers(original_dni, 1) # 0
variations += replaceXNumbers(original_dni, 2)
variations += replaceXNumbers(original_dni, 3)
variations += bruteForce(original_dni)

variations = list(set(variations))
for variation in variations:
    print(variation,original_letter,sep="-")

print("done!")
