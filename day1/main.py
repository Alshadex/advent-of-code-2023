

# open input.txt file and read it line by line and printint it to stdout then return.

ChartoDigit = {"one": "1",
                "two": "2",
                "three": "3",
                "four": "4",
                "five": "5",
                "six": "6",
                "seven": "7",
                "eight": "8",
                "nine": "9",
            }


def checkCharDigitStart(s : str) -> str:
    for d in ChartoDigit:
        if s.startswith(d):
            return ChartoDigit[d]
    return ""

def checkCharDigitEnd(s : str) -> str:
    for d in ChartoDigit:
        if s.endswith(d):
            return ChartoDigit[d]
    return ""


def getFirstDigit(s : str) -> str:
    for i in range(len(s)):
        if s[i].isdigit():
            return s[i]
        else:
            temp = checkCharDigitStart(s[i:])
            if temp != "":
                return temp
    return ""

def getLastDigit(s: str) -> str:
    for i in range(len(s) - 1, -1, -1):
        if s[i].isdigit():
            return s[i]
        else:
            temp = checkCharDigitEnd(s[:i+1])
            if temp != "":
                return temp
    return ""

sum = 0
with open('input.txt', 'r') as f:
    for line in f:
        fistDigit = getFirstDigit(line.rstrip('\n'))
        lastDigit = getLastDigit(line.rstrip('\n'))
        calib_value = int(fistDigit + lastDigit)
        print(calib_value, repr(line.rstrip('\n')))
        sum += calib_value
print(sum)


