# finding and playing with power law and game theory
# multiplication with 1.1 and 0.9 alternatively other than simple 1 = ?

import numbers

#b = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
b = [2, 3, 4]

result = 1
for x in b:
    result = x*x
print(result)

result = 1
for i, x in enumerate(b):
    if i % x == 0:
        result *= x * 0.9
    else:
        result *= x * 1.1

print(result)
