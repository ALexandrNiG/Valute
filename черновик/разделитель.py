s0 = "lamp, bag, mirror"
s = s0.split(", ") # s is a list: ["lamp", "bag", "mirror"]
print(s)

print('Hello!')
print('Hello!', 'Student!', 123)
print('Hello!', 'Student!', 123, sep = 'xxx')
print('Hello!', 'Student!', 123, end = 'yyy')
print()
print("Alexandr \"Hi\" Nikolaevich")

c = [c +'_3' for c in 'dfgh']
print(c)

sp  = []
a = int(input('Введите количество элементов: '))
for i in range(a):
    n = int(input('Введите '  + str(i+1)+ ' элемент: '))
    sp.append(n)
print('Вы ввели список: ', sp)
sp.sort()
print("Отсортированный список" ,sp)