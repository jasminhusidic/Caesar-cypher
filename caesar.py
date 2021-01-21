"""
Author: Jasmin Husidic
Name: caeser.py
Description: A program that can encode a message using a caesar cypher.
"""
encodeOutput = ""
decodeOutput = ""
flag = True
while flag == True:
    option = input("e for encode, d for decode, q for quit: ")
    option = option.lower()
    while option != "e" and option != "q" and option != "d":
        print("I don't recognize that option. Try again")
        option = input("e for encode, d for decode, q for quit: ")
        option = option.lower()
        
    if option == "q":
        print("Thanks for playing")
        flag = False
        
    if option == "d":
        decode = input("String to decode: ")
        value = int(input("Rotation value: "))
        while value > 25 or value < 1:
            print("Please use a rotation value in the range 1-25")
            value = int(input("Rotation value: "))
            
        alphabet = str("abcdefghijklmnopqrstuvwxyz")

        rotatedAlphabet = alphabet[value:26]+alphabet[0:value]
        for char in decode:
            if char in alphabet:
                original = rotatedAlphabet.find(char)
                letter = alphabet[original]
                decodeOutput = decodeOutput + letter
            else:
                decodeOutput = decodeOutput + char
        print("The decoded string is: ",decodeOutput)
        decodeOutput = ""
            

    if option == "e":
        encode = input("String to encode: ")
        value = int(input("Rotation value: "))
        while value > 25 or value < 1:
            print("Please use a rotation value in the range 1-25")
            value = int(input("Rotation value: "))
    

        alphabet = str("abcdefghijklmnopqrstuvwxyz")

        rotatedAlphabet = alphabet[value:26]+alphabet[0:value]
        for char in encode:
            if char in alphabet:
                original = alphabet.find(char)
                letter = rotatedAlphabet[original]
                encodeOutput = encodeOutput + letter
            else:
                encodeOutput = encodeOutput + char
        print("The encoded string is: ",encodeOutput)
        encodeOutput = ""
   
