10.
n = int(input('Введите количество монет: '))
count_zero = 0
count_one = 0
for i in range(n):
    x = int(input())
    if x == 0:
        count_zero += 1
    else:
        count_one += 1
    if count_one > count_zero:
        print(count_zero)
    else:
        print(count_one)



12.
x = int(input('введите х: '))
y = int(input('введите y: '))
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)


14.
n = int(input('введите число'))
i = 0
while 2 ** i <= n:
    print(2 ** i)
    i += 1