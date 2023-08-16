# Variables Booleanas

print(4 < 5)  # ---> True

print(5 < 4)  # ---> False

print(5 == 5)  # ---> True

print(6 == 4)  # ---> False

x = True
y = False

print(type(x))
print(type(y))

print(x and x)  # ---> True

print(x and y)  # ---> False

print(x or x)  # ---> True

print(x or y)  # ---> True

print(y or y)  # ---> False

print((3 < 4) and (4 < 5))  # ---> True

print((3 < 4) and (6 < 5))  # ---> False

resultado = x and x  # ---> True

print(not resultado)  # ---> False
