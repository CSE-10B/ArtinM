vowels = ["a", "i", "e", "o", "u"] #list with vowels

letter = input("Type a letter: ").lower() #user inputs a letter to check

if len(letter) == 1: #makle sure it's a single letter, if so, continue within this loop, otherwise, not valid
    if letter in vowels: #if the inputted letter appears in the list of vowels
        print("Yes") #it is a vowel
    else:
        print("No") #otherwise, not a vowel
else: 
    print("Not a Single Letter")