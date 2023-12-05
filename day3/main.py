import re

digits = re.compile(r'\d+')

def getAllIntegers(data: str) -> list[str]:
    return re.findall(digits, data)
        

with open('input.txt', 'r') as file:
    data = file.read().split('\n')

for i in data:
    print(getAllIntegers(i))