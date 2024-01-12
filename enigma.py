from msvcrt import getch
import sys
import os

rotors=[]
appairage=[]
alphabet =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rotor1=     "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
#######     "01234567890123456789012345"
rotor2=     "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor3=     "BDFHJLCPRTXVZNYEIWGAKMUSQO"
rotor4=     "ESOVPZJAYQUIRHXLNFTGKDCMWB"
#######     "01234567890123456789012345"
rotor5=     "VZBRGITYUPSDNHLXAWMJQOFECK"
reflexionA= "EJMZALYXVBWFCRQUONTSPIKHGD"
reflexionB= "YRUHQSLDPXNGOKMIEBFZCWVJAT"
#######     "01234567890123456789012345"
reflexionC= "FVPJIAOYEDRZXWGCTKUQSBNMHL"


def clear_screen():
    if sys.platform.startswith('win'):
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def passage_rotor(letter, rotors, i):
    rotor = globals()['rotor'+str(rotors[i])]
    index = (alphabet.index(letter)+rotors[i+1])%26
    return rotor[index]

def passage_rotor_r1(letter, rotors, i):
    rotor = globals()['rotor'+str(rotors[i])]
    index = (rotor.index(letter)-rotors[i+1])%26
    return alphabet[index]


def reflexion(letter,refelx):
    a=globals()['reflexion'+str(refelx)]
    index = alphabet.index(letter)
    return a[index]
    

def main():
    while True:
        input = getch()
        letter = input.decode().upper()
        if letter == ' ':
            clear_screen()
        elif letter == '\r':
            return(letter)
        elif alphabet.count(letter) == 1:
            print(enigma(letter, rotors, appairage), end="", flush=True)
            #print(str(enigma(letter, rotors, appairage)))

def enigma(letter, rotors, appairage):

    if appairage.count(letter) >= 1:
        if (appairage.index(letter))%2==0:
            letter = appairage[appairage.index(letter)+1]
        else:
            letter = appairage[appairage.index(letter)-1]
    letter = passage_rotor(letter,rotors,0)
    letter = passage_rotor(letter,rotors,2)
    letter = passage_rotor(letter,rotors,4)

    letter = reflexion(letter,reflex)

    letter = passage_rotor_r1(letter,rotors,4)
    letter = passage_rotor_r1(letter,rotors,2)
    letter = passage_rotor_r1(letter,rotors,0)

    if appairage.count(letter) >= 1:
        if (appairage.index(letter))%2==0:
            letter = appairage[appairage.index(letter)+1]
        else:
            letter = appairage[appairage.index(letter)-1]
    tour_rotor(rotors)
    return(letter)

def tour_rotor(rotors):
    for i in (0, 2):
        if rotors[i] == 1 and rotors[i+1] == 17:
            rotors[i+3] = ((rotors[i+3])%26)+1
            if i>0:
                rotors[i+1] = ((rotors[i+1])%26)+1    
        elif rotors[i] == 2 and rotors[i+1] == 5:
            rotors[i+3] = ((rotors[i+3])%26)+1
            if i>0:
                rotors[i+1] = ((rotors[i+1])%26)+1    
        elif rotors[i] == 3 and rotors[i+1] == 22:
            rotors[i+3] = ((rotors[i+3])%26)+1
            if i>0:
                rotors[i+1] = ((rotors[i+1])%26)+1            
        elif rotors[i] == 4 and rotors[i+1] == 10:
            rotors[i+3] = ((rotors[i+3])%26)+1
            if i>0:
                rotors[i+1] = ((rotors[i+1])%26)+1    
        elif rotors[i] == 5 and rotors[i+1] == 26:
            rotors[i+3] = ((rotors[i+3])%26)+1
            if i>0:
                rotors[i+1] = ((rotors[i+1])%26)+1    
    rotors[1] = ((rotors[1])%26)+1
    #print(f"rotors[{rotors[0]}] = {rotors[1]} - rotors[{rotors[2]}] = {rotors[3]} - rotors[{rotors[4]}] = {rotors[5]}")

def check(rotors, appairage, reflex):
    #CHECK DES ROTORS
    if len(rotors) != 6:
        print(f"Nombre de rotors invalide {len(rotors)}. Au lieu de 6.")
        return True
    if rotors[0] == rotors[2] or rotors[0] == rotors[4] or rotors[2] == rotors[4]:
        print("Rotor invalide. Chaque rotor est unique.")
        return True
    for i in range(0, 6, 2):
        if int(rotors[i])>=6 or int(rotors[i])<=0:
            print(f"Rotor invalide {i}. Doit être entre 1 et 5.")
            return True
    for i in range(1, 5, 2):
        if int(rotors[i])>=27 or int(rotors[i])<=0:
            print(f"Rotor invalide {i}. Doit être entre 1 et 26.")
            return True
        
    #CHECK DES appairageS
    if len(appairage) > 20 or len(appairage)%2 != 0:
        print(f"Nombre d'appairage invalide {len(appairage)}. (Max = 10)")
        return True
    for i in appairage:
        if alphabet.count(i) != 1:
            print(f"Appairage invalide : {i}. Doit être sous forme A-Z.")
            return True
    for i in appairage:
        if appairage.count(i) >= 2:
            print(f"Appairage invalide. Chaque lettres doit être utilisé maximum 1 fois.")
            return True
    
    #CHECK DU REFLECTEUR
    if alphabet.count(reflex) != 1:
        print(f"Reflecteur invalide : {reflex}. Doit être sous forme A B ou C.")
        return True
    if len(reflex) != 1:   
        print(f"Reflecteur invalide : {reflex}. Doit être sous forme A B ou C.")
        return True

    return False

#rotorss = "ROTOR1-VALEUR ROTOR2-VALEUR ROTOR3-VALEUR"
#rotorss = "1-1 3-2 5-6"
#reflex="B"
#appairages = "A-B C-D E-F G-H I-J K-L M-N O-P Q-R S-T".split('-')
#appairages = ""

if __name__ == "__main__":
    print("Input rotors comme ça 'Y-X' Avec Y le rotor et X la valeure (*3) et les appairages comme ça 'A-C' (*10) et le reflecteur : A ou B ou C\nEspace = clear et Entrée = quitter")
    rotorss = input("Rotors: ")
    rotors = [int(rotor) for rotor in rotorss.replace(' ', '-').split('-')]
    print(rotors)
    appairages = input("appairage: ").split('-')
    for i in appairages:
        appairage += i.upper().split(' ')
    print(appairage)
    reflex = input("Reflecteur: ").upper()
    print(reflex)
    if check(rotors, appairage, reflex):
        print("Invalid Input")
        exit()
    main()
