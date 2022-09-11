a, b = input(), 0
for i in a:
    if not i.isdigit():
        continue
    else:
        b += int(i)
print(b)