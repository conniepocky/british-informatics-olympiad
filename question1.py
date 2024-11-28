
def integer_strings(n, i):
    lenDigits = len(str(n))
    nextNum = n

    while lenDigits < i:
        nextNum = nextNum+1
        lenDigits += len(str(nextNum))

    indexOfDigit = i - (lenDigits - len(str(nextNum)))
    return str(nextNum)[indexOfDigit-1]


print(integer_strings(6, 12))

