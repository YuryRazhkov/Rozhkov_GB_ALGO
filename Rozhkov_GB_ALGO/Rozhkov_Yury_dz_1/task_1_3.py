#3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b,
# проходящей через эти точки.

print('enter coordinates of 2 points')
x1 = int(input('x1: '))
y1 = int(input('y1: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))

k = (y1 - y2) / (x1 - x2)
b = y1 - k * x1
if b > 0:
    print(f'y = {k} * x + {abs(b)}')
else:
    print(f'y = {k} * x - {abs(b)}')
