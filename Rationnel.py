#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

import math
import numbers

global nombre 
global den
global periode


def split_str(s):
    
    """ Parameter :
        s : The string to split """

    return [ch for ch in s]

def reduit():
    
    '''
    Reduce the number entered as a global variable in an undivisble fractionned form
    '''

    tab = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    global den
    global nombre

    for i in tab:

        Fin = False

        while Fin == False:

            if nombre % i == 0 and den % i == 0:

                nombre = nombre / i
                den = den / i

            else:

                Fin = True

def recherchePeriode():

    '''
    Search for the decimal length
    '''

    global nombre
    global periode

    nombreStr = str(nombre)                 #On convertit le nombre rentré en String
    decimale = (nombreStr.split('.'))[1]    #On récupère la décimale
    tableauDecimale = split_str(decimale)   #On met chacun des caractères de la liste dans un tableau pour identifier les récurrences


    longueurPeriode = 0
    trouve = False
    

    if len(tableauDecimale) > 0:            #Si il y a une décimale, on regarde la période

        longueurPeriode = 1

        while trouve == False: #Tant que l'on a pas trouvé la période

            identique = True
            laPeriode = []

            for i in range(longueurPeriode):    #On définit la période à tester

                laPeriode.append(tableauDecimale[i])

            j = len(laPeriode)                  #Index à partir duquel on va tester les valeurs de la décimale
            iTest = len(laPeriode)              #Permet de pointer à la bonne valeur de la période de test

            while j < len(tableauDecimale) and identique == True:      #On compare la période de test avec le reste de la chaîne

                if tableauDecimale[j] != laPeriode[iTest - len(laPeriode)]:

                    identique = False

                j += 1
                iTest += 1

                if iTest - len(laPeriode) > len(laPeriode)-1:

                    iTest = len(laPeriode)

            
            if identique == True or longueurPeriode == len(tableauDecimale):     #Si les chiffres de la période était identique dans chaque groupe de la même longueur suivants, on s'arrête car la période est trouvée

                periode = ""
                trouve = True
                for i in laPeriode:

                    periode = periode + i

            longueurPeriode += 1

def miseEnFraction():

    '''
    Put the number in its fractionned form
    '''

    global nombre
    global periode
    global den

    longueurPeriode = len(periode)

    periode = int(periode)

    nombreMult = nombre * math.pow(10, longueurPeriode)

    checkEntier = nombreMult.is_integer()       #On regarde si le nombre multiplié est entier

    if not checkEntier:

        leNombre = nombreMult - nombre          #On enlève partie decimale
        nombre = int(leNombre)                  #On garde partie entière du nombre
        den = math.pow(10, longueurPeriode) - 1 #Dénominateur à 10^longueur période - 1

    else:

        nombre = nombreMult                     #Pas besoin d'enlever partie décimale par soustraction, le nombre est déjà entier
        den = math.pow(10, longueurPeriode)     #Dénominateur à 10^longueur periode



#===============================================================
#                           EXECUTION
#===============================================================


den = 1 #Dénominateur à 1 par défaut
nombre = float(input("Saisir le nombre à passer sous forme de fraction irréductible : "))

print("Le nombre à convertir :", nombre)

recherchePeriode()
miseEnFraction()
reduit()

print(nombre, "/", den)


