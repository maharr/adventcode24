import re
import collections

with open("1/input.txt", "r") as f:
    global data
    data = f.read().splitlines()

left = []
right = []

for line in data:
    numbers = re.findall(r'(\d+)', line)
    left.append(int(numbers[0]))
    right.append(int(numbers[1]))

left = sorted(left)
right = sorted(right)

total = 0

for i,j in enumerate(left):
    total += abs(left[i] - right[i])

print(total)

r = collections.Counter(right)

similar = 0

for i in left:
    similar += i * r[i]

print(similar)
