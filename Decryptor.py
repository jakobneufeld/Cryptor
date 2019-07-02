print("welcome to decrypto robot")
print("""      $$\                                                    $$\           $$$$$$$\            $$\
      $$ |                                                   $$ |          $$  __$$\           $$ |
 $$$$$$$ | $$$$$$\   $$$$$$$\  $$$$$$\  $$\   $$\  $$$$$$\ $$$$$$\         $$ |  $$ | $$$$$$\  $$$$$$$\   $$$$$$\
$$  __$$ |$$  __$$\ $$  _____|$$  __$$\ $$ |  $$ |$$  __$$\\_$$  _|        $$$$$$$  |$$  __$$\ $$  __$$\ $$  __$$\
$$ /  $$ |$$$$$$$$ |$$ /      $$ |  \__|$$ |  $$ |$$ /  $$ | $$ |          $$  __$$< $$ /  $$ |$$ |  $$ |$$ /  $$ |
$$ |  $$ |$$   ____|$$ |      $$ |      $$ |  $$ |$$ |  $$ | $$ |$$\       $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |
\$$$$$$$ |\$$$$$$$\ \$$$$$$$\ $$ |      \$$$$$$$ |$$$$$$$  | \$$$$  |      $$ |  $$ |\$$$$$$  |$$$$$$$  |\$$$$$$  |
 \_______| \_______| \_______|\__|       \____$$ |$$  ____/   \____/       \__|  \__| \______/ \_______/  \______/
                                        $$\   $$ |$$ |
                                        \$$$$$$  |$$ |
                                         \______/ \__|        """)
text = input("Enter your encrypted text: ")
codelist = input("Enter your code, seperate each number by a ',': ").split(",")
decrypto = []

for j in range(len(text)):
    letter = text[j]
    letternum = ord(letter) - 97
    deshift = int(codelist[j])
    newletter = (letternum - deshift)
    if newletter < 0:
        newletter +=  26
    decrypto.append("abcdefghijklmnopqrstuvwxyz"[newletter])
print(decrypto)
