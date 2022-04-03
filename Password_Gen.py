#!/usr/bin/env python3
# coding: utf-8
import random
import pyperclip
import time
from Manager import Access


#Déclaration des variables
Long = 0
Lettre = False
Nb_lettre = 0
MinMaj = False
Nombre = False
Nb_nombre = 0
Symbols = False
Nb_symbols = 0
mdp = []


#Début des fonctions
def preset():
    global Long
    global Lettre
    global Nb_lettre
    global Nombre
    global Nb_nombre
    global MinMaj
    global Symbols
    global Nb_symbols
    Long = 15
    Lettre = True
    Nb_lettre = 7
    Nombre = True
    Nb_nombre = 5
    MinMaj = True
    Symbols = True
    Nb_symbols = 3
    resume()


def Fsymbols():
    global Long
    global Lettre
    global Nb_lettre
    global Nombre
    global Nb_nombre
    global MinMaj
    global Symbols
    global Nb_symbols
    dem = str(input("Do you want symbols ? "))
    if dem.lower().strip() == "oui" or dem.lower().strip() == "yes" or dem.lower().strip() == "y":
        Symbols = True
        Nb_symbols = Long - (Nb_lettre + Nb_nombre)
        resume()
    else:
        resume()


def Fnombre():
    global Long
    global Nombre
    global Nb_lettre
    global Nb_nombre
    test = str(input("Do you want a numbers in your password ? "))
    if test.lower().strip() == "oui" or test.lower().strip() == "yes" or test.lower().strip() == "y":
        Nombre = True
        Nb_nombre = int(input("How many you want ? "))
        if Nb_nombre == (Long - Nb_lettre):
            valid2 = str(input("your password will be composed only of letters and numbers. Is that okay ? "))
            if valid2.lower().strip() == "oui" or valid2.lower().strip() == "yes" or valid2.lower().strip() == "y":
                resume()
            else:
                Fnombre()
        elif Nb_nombre > (Long - Nb_lettre):
            print("We have a problem, please try again. Sorry for the inconvenience")
            Fnombre()
        else:
            Fsymbols()
    else:
        Nombre = False
        Fsymbols()


def lettre():
    global Long
    global Lettre
    global Nb_lettre
    global MinMaj
    sur = str(input("Do you want to create your password with your preference ? "))
    if sur.lower().strip() == "oui" or sur.lower().strip() == "yes" or sur.lower().strip() == "y":
        Long = int(input("How many caracters you want in your password ? "))                              #DEMANDE LONGUEUR
        print("That's rigth, we continue")
        Lettre = str(input("Do you want a letters in your password ? "))                             #DEMANDE LETTRE
        if Lettre.lower().strip() == "oui" or Lettre.lower().strip() == "yes" or Lettre.lower().strip() == "y":
            Lettre = True
            Nb_lettre = int(input("How many you want ? "))                                               #NB LETTRE
            if Nb_lettre == Long:
                print("your password will be composed only of letters")
                valid = str(input("Is that okay ? "))
                if valid.lower().strip() == "oui" or valid.lower().strip() == "yes" or valid.lower().strip() == "y":
                    Minmaj = str(input("Do you want a mix of lowercases and uppercase ? "))
                    if Minmaj.lower().strip() == "oui" or Minmaj.lower().strip() == "yes" or Minmaj.lower().strip() == "y":
                        MinMaj = True
                    else:
                        pass
                    resume()
                else:
                    lettre()
            elif Nb_lettre < Long:
                Minmaj = str(input("Do you want a mix of lowercases and uppercase ? "))
                if Minmaj.lower().strip() == "oui" or Minmaj.lower().strip() == "yes" or Minmaj.lower().strip() == "y":
                    MinMaj = True
                else:
                    pass
                Fnombre()
            else:
                print('We have a problem, please try again. Sorry for the inconvenience')
                request()
        else:
            Lettre = False
            Fnombre()
    else:
        preset()


def request():
    print('Password Gen v.1.2')
    demande = str(input("Do you want to create a new password ? "))
    if demande.lower().strip() == "oui" or demande.lower().strip() == "y" or demande.lower().strip() == "yes":
        mode = str(input("Use the preset ? "))
        if mode.lower().strip() == "oui" or mode.lower().strip() == "y" or mode.lower().strip() == "yes":
            preset()
        else:
            lettre()
    else:
        print("See you soon")


def generation():
    global L
    global nombre
    global symbols
    print("We create your password, please wait...")
    L = []
    nombre = []
    symbols = []
    i = 0
    if Lettre == True:
        if MinMaj == True:
            Maj = random.randint(1, Nb_lettre)
            Min = Nb_lettre - Maj
            while i < Maj:
                L.append(chr(random.randint(65, 90)))
                i += 1
            i = 0
            while i < Min:
                L.append(chr(random.randint(97, 122)))
                i += 1
        else:
            i = 0
            while i < Nb_lettre:
                L.append(chr(random.randint(97, 122)))
                i += 1
    else:
        pass
    if Nombre == True:
        i = 0
        while i < Nb_nombre:
            nombre.append(chr(random.randint(48, 57)))
            i += 1
    else:
        pass
    if Symbols == True:
        i = 0
        while i < Nb_symbols:
            symbols.append(chr(random.randint(33, 47)))
            i += 1
        constru()
    else:
        constru()


def constru():
    global commande
    mdp = L + nombre + symbols
    random.shuffle(mdp)
    print("Your password has been created : " + "".join(mdp))
    pyperclip.copy("".join(mdp))
    print("Your password has been copied")
    reroll = str(input("Reroll ? "))
    if reroll.lower().strip() == "oui" or reroll.lower().strip() == "y" or reroll.lower().strip() == "yes":
        generation()
    else:
        go = input("Do you want to access to the manager ?")
        if go.lower().strip() == "oui" or go.lower().strip() == "y" or go.lower().strip() == "yes":
            commande = False
            Access()
        else:
            print("See you soon")
            commande = False
            time.sleep(2)


def resume():
    print("These are your preferences :")
    print("Length : {}\nLetters : {}\nNumber of letters : {}\nLowercase / uppercase : {}\nNumbers : {}\nNumbers of numbers : {}\nSymbols : {}\nNumbers of symbols : {}".format(Long, Lettre, Nb_lettre, MinMaj, Nombre, Nb_nombre, Symbols, Nb_symbols))
    generation()


#VERSION FRANCAISE -VF          VERSION FRANCAISE -VF           VERSION FRANCAISE -VF           VERSION FRANCAISE -VF           VERSION FRANCAISE -VF

def defaut():
    global Long
    global Lettre
    global Nb_lettre
    global Nombre
    global Nb_nombre
    global MinMaj
    global Symbols
    global Nb_symbols
    Long = 15
    Lettre = True
    Nb_lettre = 7
    Nombre = True
    Nb_nombre = 5
    MinMaj = True
    Symbols = True
    Nb_symbols = 3
    resumer()


def Fsymbol():
    global Long
    global Lettre
    global Nb_lettre
    global Nombre
    global Nb_nombre
    global MinMaj
    global Symbols
    global Nb_symbols
    dem = str(input("Voulez-vous des symboles dans votre mot de passe ? "))
    if dem.lower().strip() == "oui" or dem.lower().strip() == "yes" or dem.lower().strip() == "y":
        Symbols = True
        Nb_symbols = Long - (Nb_lettre + Nb_nombre)
        resumer()
    else:
        resumer()


def Fnombres():
    global Long
    global Nombre
    global Nb_lettre
    global Nb_nombre
    test = str(input("Voulez-vous des nombres dans votre mot de passe ? "))
    if test.lower().strip() == "oui" or test.lower().strip() == "yes" or test.lower().strip() == "y":
        Nombre = True
        Nb_nombre = int(input("Combien en souhaitez-vous ? "))
        if Nb_nombre == (Long - Nb_lettre):
            valid2 = input("Votre mot de passe sera uniquement composé de lettres et de nombres. Cela vous convient ? ")
            if valid2.lower().strip() == "oui" or valid2.lower().strip() == "yes" or valid2.lower().strip() == "y":
                resumer()
            else:
                Fnombres()
        elif Nb_nombre > (Long - Nb_lettre):
            print("Nous rencontrons un problème, merci de bien vouloir recommencer. Désolé pour la gêne occasionner.")
            Fnombres()
        else:
            Fsymbol()
    else:
        Nombre = False
        Fsymbol()


def lettres():
    global Long
    global Lettre
    global Nb_lettre
    global MinMaj
    sur = str(input("Voulez-vous créer un mot de passe avec vos préférences ? "))
    if sur.lower().strip() == "oui" or sur.lower().strip() == "yes" or sur.lower().strip() == "y":
        Long = int(input("Combien de caractères souhaitez-vous dans votre mot de passe ? "))                              #DEMANDE LONGUEUR
        print("Très bien, nous continuons")
        Lettre = str(input("Voulez-vous des lettres dans votre mot de passe ? "))                             #DEMANDE LETTRE
        if Lettre.lower().strip() == "oui" or Lettre.lower().strip() == "yes" or Lettre.lower().strip() == "y":
            Lettre = True
            Nb_lettre = int(input("Combien en souhaitez-vous ? "))                                               #NB LETTRE
            if Nb_lettre == Long:
                print("Votre mot de passe sera uniquement composé de lettres")
                valid = str(input("Cela vous convient ? "))
                if valid.lower().strip() == "oui" or valid.lower().strip() == "yes" or valid.lower().strip() == "y":
                    Minmaj = str(input("Voulez-vous un mélange de minuscule et de majuscule ? "))
                    if Minmaj.lower().strip() == "oui" or Minmaj.lower().strip() == "yes" or Minmaj.lower().strip() == "y":
                        MinMaj = True
                    else:
                        pass
                    resumer()
                else:
                    lettres()
            elif Nb_lettre < Long:
                Minmaj = str(input("Voulez-vous un mélange de minuscule et de majuscule ? "))
                if Minmaj.lower().strip() == "oui" or Minmaj.lower().strip() == "yes" or Minmaj.lower().strip() == "y":
                    MinMaj = True
                else:
                    pass
                Fnombres()
            else:
                print('Nous avons un problème, merci de bien vouloir recommencer. Desolé pour la gêne occasionner')
                choix()
        else:
            Lettre = False
            Fnombres()
    else:
        defaut()


def choix():
    print('Password Gen v.1.2')
    demande = str(input("Voulez-vous créer un mot de passe ? "))
    if demande.lower().strip() == "oui" or demande.lower().strip() == "y" or demande.lower().strip() == "yes":
        mode = str(input("Voulez-vous utiliser le mode par défaut ? "))
        if mode.lower().strip() == "oui" or mode.lower().strip() == "y" or mode.lower().strip() == "yes":
            defaut()
        else:
            lettres()
    elif demande.lower().strip() == "access":
        Access()
    elif demande.lower().strip() == "/en":
        request()
    else:
        print("A bientôt !")


def generatio():
    global L
    global nombre
    global symbols
    print("Nous créons votre mot de passe, merci de patienter")
    L = []
    nombre = []
    symbols = []
    i = 0
    if Lettre == True:
        if MinMaj == True:
            Maj = random.randint(1, Nb_lettre)
            Min = Nb_lettre - Maj
            while i < Maj:
                L.append(chr(random.randint(65, 90)))
                i += 1
            i = 0
            while i < Min:
                L.append(chr(random.randint(97, 122)))
                i += 1
        else:
            i = 0
            while i < Nb_lettre:
                L.append(chr(random.randint(97, 122)))
                i += 1
    else:
        pass
    if Nombre == True:
        i = 0
        while i < Nb_nombre:
            nombre.append(chr(random.randint(48, 57)))
            i += 1
    else:
        pass
    if Symbols == True:
        i = 0
        while i < Nb_symbols:
            symbols.append(chr(random.randint(33, 47)))
            i += 1
        construs()
    else:
        construs()


def construs():
    mdp = L + nombre + symbols
    random.shuffle(mdp)
    print("Votre mot de passe à bien été créé : " + "".join(mdp))
    pyperclip.copy("".join(mdp))
    print("Votre mot de passe à bien été copier")
    reroll = str(input("Reroll ? "))
    if reroll.lower().strip() == "oui" or reroll.lower().strip() == "y" or reroll.lower().strip() == "yes":
        generatio()
    else:
        go = input("Voulez-vous accéder au manager de mot de passe ?")
        if go.lower().strip() == "oui" or go.lower().strip() == "y" or go.lower().strip() == "yes":
            Access()
        else:
            print("A bientôt !")
            time.sleep(2)


def resumer():
    print("Voici vos préférences :")
    print("Longueur : {}\nLettres : {}\nNombre de lettres : {}\nMinuscule / Majuscule : {}\nNombre : {}\nNombre de nombre : {}\nSymboles : {}\nnombre de symboles : {}".format(Long, Lettre, Nb_lettre, MinMaj, Nombre, Nb_nombre, Symbols, Nb_symbols))
    generatio()


#Boucle de commande
commande = True
print("Welcome to Password_Master")
print("Note /help to access help")
print("press q to quitt")
while commande == True:

    print("Note a command")

    key = input()

    if key == "/password" or key == "/en":
        request()
    if key == "/fr":
        choix()
    if key == "/access":
        commande = False
        Access()
        break
    if key == "q":
        commande = False
        time.sleep(2)
    if key == "/help":
        print("*"*20)
        print("/password : Access to password generator")
        print("/fr & /en : switch language (French/English)")
        print("/access : access to password manager")
        print("q : quitt")
        print("If you have an error during the creation of the password try to answer just with y/n")
        print("*"*20)