# Enigma Machine Python

This Python script simulates the operation of an Enigma machine, a type of encryption device used by the Germans during World War II. The script allows the user to input the settings for the rotors, reflector, and plugboard (appairages), and then it simulates the operation of the machine based on these settings.

## Usage
Run the script. You will be prompted to enter the settings for the rotors, reflector, and plugboard.

1. Input the rotors as 'Y-X' where Y is the rotor number and X is the value. You need to input three rotors. For example: `1-1 3-2 5-6`.

2. Input the plugboard settings (appairages) as 'A-C'. You can input up to 10 pairs. For example: `A-B C-D E-F G-H I-J K-L M-N O-P Q-R S-T`.

3. Input the reflector as a single letter: A, B, or C.

4. If the input is valid, the script will continue to the main function. If the input is invalid, the script will print "Invalid Input" and exit.

## Example
```
Input rotors comme ça 'Y-X' Avec Y le rotor et X la valeure (*3) et les appairages comme ça 'A-C' (*10) et le reflecteur : A ou B ou C
Espace = clear et Entrée = quitter
Rotors: 1-1 3-2 5-6
[1, 1, 3, 2, 5, 6]
appairage: A-B C-D E-F G-H I-J K-L M-N O-P Q-R S-T
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
Reflecteur: B
B
```


### Note
**This script is a simulation and does not provide real encryption. It is intended for educational purposes only.**