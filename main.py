def slovo():
    a = slovo.lower()[::-1]
    if slovo == a:
        return True
    else:
        return False

slovo = str(input("ВВедите слово: "))
