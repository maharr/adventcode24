import re
with open("2/test.txt", "r") as f:
    global data
    data = f.read().splitlines()

numbers = []

for line in data:
    numbers.append(list(map(int,re.findall(r'(\d+)', line))))
        
print(numbers)

for l,line in enumerate(numbers):
    if (line[0] - line[1]) < 0:
        dir = '+'
    else:
        dir = '-'
    for num in line:
        pass

