def squares(n):
    start = 1
    while start <= n:
        yield start * start #start**2
        start += 1

for el in squares(5):
    print(el)

print(list(squares(5)))