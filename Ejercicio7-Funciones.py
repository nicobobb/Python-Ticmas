def potenciacion(base, exponente):
    return base ** exponente


pot = potenciacion(2, 3)

pot_dec = potenciacion(exponente=3, base=2)

print(pot)
print(pot_dec)


def potenciacion_lambda(base, exponente): return base ** exponente


a = 1
b = 'Text'

try:
    print(a+b)
except:
    print('No se puede sumar. Ha ocurrido un error')
