
def split_string_on_change(CipherString):
    length = len(CipherString)
    current = 0
    characterlist = list()
    if CipherString == "":
        return CipherString
    while current < length:
        nextcharacter = current + 1
        while True:
            if nextcharacter == length:
                break
            if CipherString[current] == CipherString[nextcharacter]:
                nextcharacter = + 1
            else:
                break
        characterlist.append(CipherString[current:nextcharacter])
        current = nextcharacter
    final = ' ,'.join(characterlist) + ' '
    return final
