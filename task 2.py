"""
Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
"""

def Numbers(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значения {xyz[i]}: "))
    return a

def checkExp(x):
    left = not (x[0] or x[1] or x[2])
    rigth = not x[0] and not x[1] and not x[2]
    res = left == rigth
    return res

expression = Numbers(3)

if checkExp(expression) == True:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")
