def solution(userPassword):
    characterlist = ['@', '-', '_', '+', '!', '?', '%', '$', '#']
    digitcount = 0
    specialcount = 0
    capitalcount = 0
    lettersequence = 0
    charactercount = dict()
    if len(userPassword) < 12 or len(userPassword) > 25:  # Rule 1
        return False
    if 'password' in userPassword.lower():  # Rule 2
        return False
    for character in userPassword:
        charactercount[character] = charactercount.get(character, 0) + 1
        if character.isalpha() is False and lettersequence < 5:
            lettersequence = 0
        if character.isdigit() is True:
            digitcount += 1
        elif character.isupper() is True:
            capitalcount += 1
            lettersequence += 1
        elif character in characterlist:
            specialcount += 1
        elif character.isalpha():
            lettersequence += 1
        else:
            return False
    if digitcount == 0 or digitcount >= 2:
        return False
    if capitalcount == 0:
        return False
    if specialcount == 0 or specialcount >= 2:
        return False
    if userPassword[len(userPassword) - 1].isdigit() or userPassword[len(userPassword) - 1] in characterlist:
        return False
    if lettersequence < 5 and userPassword <= 20:
        return False
    for value in charactercount.values():
        if value >= 4:
            return False
    return True
