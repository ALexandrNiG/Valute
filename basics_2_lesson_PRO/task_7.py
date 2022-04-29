a = str(254314)

h = 1
i = 0
while i < 6:
    b = int(a[i])
    h *= b
    i += 1
print("Произведение цифр числа - ", h, end='(')
print(a[0], a[1], a[2], a[3], a[4], a[5], sep="*", end=')')