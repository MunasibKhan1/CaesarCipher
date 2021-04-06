from io import StringIO

alphaUp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphaLo = alphaUp.lower()

def encrypt(key, message):
    encrypted = ''
    shiftUp = alphaUp[26-key:]+alphaUp[0:26-key]
    if(message == ""):
        return "NO MESSAGE TO ENCRYPT"
    if(key == 0):
        return "NO KEY TO ECRYPT THE MESSAGE"
    shiftLo = shiftUp.lower()
    for i in range(len(message)):
        char = message[i]
        if(char.isupper()):
            index = alphaUp.index(char)
            encrypted = encrypted + shiftUp[index]
        elif(char.islower()):
            index = alphaLo.index(char)
            encrypted = encrypted + shiftLo[index]
        else:
            encrypted = encrypted + char
    print(f"{encrypted}")
    return encrypted

