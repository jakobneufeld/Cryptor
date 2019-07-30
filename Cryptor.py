import random

class Cryptor :
    def decryptWithGeneratedCode(text,codelist):
        decrypto = []
        for j in range(len(text)):
            letter = text[j]
            letternum = ord(letter) - 97
            deshift = int(codelist[j])
            newletter = (letternum - deshift)
            if newletter < 0:
                newletter +=  26
            decrypto.append("abcdefghijklmnopqrstuvwxyz"[newletter])
        return decrypto
    def encryptWithGeneratedCode(message, messageLeng, key,self):
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
