n, factorial, count = int(input()), 1, []

for i in range(2, n + 2):
    count.append(factorial)
    factorial *= i

print(*count)