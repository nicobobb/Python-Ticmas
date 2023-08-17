class Persona:
    """
    Esta es una clase donde se agregan todos los datos
    respecto a una persona
    """

    # Definimos al constructor
    def __init__(self, nombre, edad):
        # Todo lo que definamos en __init__ se corre al crear la instancia de la clase
        self.nombre = nombre
        self.edad = edad

# El parámetro self se refiere al objeto instanciado de esa clase sobre el cual se está invocando dicho método.

# Creamos un objeto p1 que es una instancia de la clase Persona


p1 = Persona("Juan", 27)

print(p1.nombre)
print(p1.edad)
