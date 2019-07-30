import random


def encryptWithGeneratedCode(message, messageLeng, key):
    abc = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13,
           "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25,
           "z": 26}
    textlist = []
    i = 0
    for x in range(messageLeng):
        textlist.append(message[i])
        i += 1
    encrypt = []

    for j in range(messageLeng):
        letter = textlist[j]
        letternum = ord(letter) - 96
        shift = key[j]
        shift -= 1
        newletter = (letternum + shift) % 26
        encrypt.append("abcdefghijklmnopqrstuvwxyz"[newletter])
    return encrypt


print ("""  /$$$$$$                                  /$$                     /$$$$$$$            /$$                   /$$    
 /$$__  $$                                | $$                    | $$__  $$          | $$                  | $$    
| $$  \__/  /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$    /$$$$$$       | $$  \ $$  /$$$$$$ | $$$$$$$   /$$$$$$  /$$$$$$  
| $$       /$$__  $$| $$  | $$ /$$__  $$|_  $$_/   /$$__  $$      | $$$$$$$/ /$$__  $$| $$__  $$ /$$__  $$|_  $$_/  
| $$      | $$  \__/| $$  | $$| $$  \ $$  | $$    | $$  \ $$      | $$__  $$| $$  \ $$| $$  \ $$| $$  \ $$  | $$    
| $$    $$| $$      | $$  | $$| $$  | $$  | $$ /$$| $$  | $$      | $$  \ $$| $$  | $$| $$  | $$| $$  | $$  | $$ /$$
|  $$$$$$/| $$      |  $$$$$$$| $$$$$$$/  |  $$$$/|  $$$$$$/      | $$  | $$|  $$$$$$/| $$$$$$$/|  $$$$$$/  |  $$$$/
 \______/ |__/       \____  $$| $$____/    \___/   \______/       |__/  |__/ \______/ |_______/  \______/    \___/  
                     /$$  | $$| $$                                                                                  
                    |  $$$$$$/| $$                                                                                  
                     \______/ |__/                                                                                  """)
print("                       ")
text = input("Enter your cipher text no spaces allowed: ")
text = text.lower()
textLeng = len(text)

keyGenerate = input("Do you want to chooose the key (type yes) or do you want that I generate the key (type no): ")
keyGenerate = keyGenerate.lower()
code = ''
codeGenerate = []
if keyGenerate == "yes":
    while len(code) != textLeng:
        code = input("Please enter your key, it has to be as long as your text that you want to encrypt: ")
elif keyGenerate == "no":
    for i in range(textLeng):
        codeGenerate.append(random.randint(1, 26))
    print("This is your code: ", codeGenerate)

if keyGenerate == 'no':
    print("Here is your text")
    print(encryptWithGeneratedCode(text, textLeng, codeGenerate))
else:
    codelist = []
    for l in range(len(code)):
        codelist.append(int(code[l]))
    print(encryptWithGeneratedCode(text, textLeng, codelist))
