import math
import cmath
print("Введите корни квадратного уравнения: ")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = b*b - 4*a*c
print(d)
if a == 0:
    print("Данное уравнение не является квадратным!")
else:
    if d < 0:
        x1 = (-b + cmath.sqrt(d))/(2*a)
        x2 = (-b - cmath.sqrt(d))/(2*a)
        print("Ответ:\nx1 =", x1, "\nx2 =", x2)
    else:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        if x1%1 == 0:
            x1 = int(x1)
        if x2%1 == 0:
            x2 = int(x2)
        if x1 == x2:
            print("Ответ:\nx =", x1)
        else:
            print("Ответ:\nx1 =", x1, "\nx2 =", x2)


