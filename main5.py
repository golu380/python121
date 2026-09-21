l1 = []

for i in range(1,6):
    l1.append(i)

print(l1)


numbers = [i for i in range(1,6)]
print(numbers)

sqnums = [i * i for i in range(1,6)]
print(sqnums)

eveneven = [i for i in range(1,11) if i%2 == 0]
print(eveneven)
odds  = [i for i in range(1,11) if i%2 == 1]
print(odds)

squares = {}

for i in range(1,6):
    squares[i] = i * i 

print(squares)

sqnums1 = {i:i * i for i in range(1,6)}
print(sqnums1)

