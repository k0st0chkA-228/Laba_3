# Формируется матрица F следующим образом: если в С количество положительных элементов в четных столбцах в области 2
# больше, чем количество отрицательных  элементов в нечетных столбцах в области 4, то поменять в С симметрично
# области 1 и 3 местами, иначе С и Е поменять местами несимметрично. При этом матрица А не меняется. После чего
# вычисляется выражение: (F+A)*AT – K * F. Выводятся по мере формирования А, F и все матричные операции последовательно.

#                           1
#    E    B            4         2
#    D    C                 3

from random import randint
n = int(input('матрица размером NxN\nвведите n='))
while n < 5:
    print('вы ввели число, не подхлдящие по условие, введите число N, большее или равное 5')
    n = int(input())
k = int(input('коэффициент умножения на матрицу F\nвведите k='))
print()
print()
print('границы подматриц и областей не включаются')

arr = []
for i in range(n):
    arr.append([])
    for j in range(n):
        arr[i].append(randint(-10, 10))                           #заполнение матрицы А случайными числами от -10 до 10
print('_______________________________________________')
print('A')
for i in range(n):                                                #вывод матрицы А
    for j in range(n):
        print('{:4d}'.format(arr[i][j]), end='')
    print()

frr = []
for i in range(n):                                                #заполнение матрици F элементами матрицы А
    frr.append([])
    for j in range(n):
        frr[i].append(arr[i][j])

a = 0
b = 0
for i in range((n + 1) // 2, n):
    for j in range((n + 1) // 2, n):
        x = i - ((n + 1) // 2)
        y = j - ((n + 1) // 2)
        if (y % 2 != 0) and (x - y < 0) and (x + y > (n // 2) - 1) and frr[i][j] > 0:#условие для 2 области подматрицы С
            a += 1
        if (y % 2 == 0) and (x - y > 0) and (x + y < (n // 2) - 1) and frr[i][j] < 0:#условие для 4 области подматрицы С
            b += 1
print('количество положительных чисел A в области 2\nа = ', a, '\nколичество отрицательных чисел B в области 4\nb = ', b)
if a > b:
    print('a > b')
    print('первое условие: поменять в С симметрично области 1 и 3 местами')
    for i in range((n + 1) // 2, ((n + 1) // 2) + (n // 4)): #смена элементов области 1 и 3 подматрици С
        x = i - ((n + 1) // 2)
        for j in range(((n + 1) // 2) + x + 1, n - x - 1):
            y = j - ((n + 1) // 2)
            frr[((n // 2) - 1) - x + ((n + 1) // 2)][((n // 2) - 1) - y + ((n + 1) // 2)], frr[i][j] = \
                frr[i][j], frr[((n // 2) - 1) - x + ((n + 1) // 2)][((n // 2) - 1) - y + ((n + 1) // 2)]
else:
    print('a <= b')
    print('второе условие: С и Е поменять местами несимметрично')
    for i in range(n // 2):                                   #смена элементов подматриц С и Е
        for j in range(n//2):
            frr[i][j], frr[i + ((n + 1) // 2)][j + ((n + 1) // 2)] = \
                frr[i + ((n + 1) // 2)][j + ((n + 1) // 2)], frr[i][j]
print('______________________________________________________________________')
print('F')
for i in range(n):                                            #вывод матрици F
    for j in range(n):
        print('{:4d}'.format(frr[i][j]), end='')
    print()

print('_________________________________________')
print('F+A')
FA = []
for i in range(n):                                             #заготовка для суммы матриц А и F
    FA.append([])
    for j in range(n):
        FA[i].append(arr[i][j])

for i in range(n):                                             #складование элементов матриц А и F
    for j in range(n):
        FA[i][j] = arr[i][j] + frr[i][j]


for i in range(n):                                             #ввывод матрици равное сумме А и F = FA
    for j in range(n):
        print('{:4d}'.format(FA[i][j]), end='')
    print()

tran = []
for i in range(n):                                             #заготовка для транспонентной матрицы Аt
    tran.append([])
    for j in range(n):
        tran[i].append(arr[i][j])

for i in range(n):                                             #транспонирование матрицы А
    for j in range(n):
        tran[j][i] = arr[i][j]

print('___________________________________________')
print('At')                                                    #вывод транспонентной матрици Аt
for i in range(n):
    for j in range(n):
        print('{:4d}'.format(tran[i][j]), end='')
    print()

print('_________________________________________')

print('FA * At')

FAT = []                                                        #заготовка под матрицу равной произведению матриц FA и At = FAT
for i in range(n):
    FAT.append([])
    for j in range(n):
        FAT[i].append(frr[i][j])


for i in range(n):
    for j in range(n):
        for k in range(n):
            FAT[i][j] += FA[i][k] * tran[k][j]

for i in range(n):                                              #вывод матрицы FAT
    for j in range(n):
        print('{:4d}'.format(FAT[i][j]), end='')
    print()
print('______________________________________')
print('K*F')
FK = []                                                        #заготовка под матрицу F умноженную на k
for i in range(n):
    FK.append([])
    for j in range(n):
        FK[i].append(frr[i][j])

for i in range(n):                                              #умножение элементов матрицы F на коэффициент k
    for j in range(n):
        FK[i][j] = k * frr[i][j]

for i in range(n):                                              #вывод матрици равное F*k = FK
    for j in range(n):
        print('{:4d}'.format(FK[i][j]), end='')
    print()
print('_______________________________________________')
print('(F + A) * At - K * F')
fin = []                                                        #заготовка под матрицу равной FAT - FK
for i in range(n):
    fin.append([])
    for j in range(n):
        fin[i].append(frr[i][j])

for i in range(n):
    for j in range(n):
        fin[i][j] = FAT[i][j] - FK[i][j]

for i in range(n):                                              #вывод матрицы равной вырожению (F+A)*At - k * F =
    for j in range(n):
        print('{:4d}'.format(fin[i][j]), end='')
    print()
