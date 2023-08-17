lista = ['Hola', 'Chau', 'Nos vemos']
print(lista[1])

lista.append('Cachichen')
lista.insert(1, 'Estoy')

for value in lista:
    print(value)

numeros = [2, 1, 9, 5, 4, 3, 10]
numeros.sort()
print(numeros)


my_dic = {
    'nombre': 'Juan',
    # 'edad': 46
}

print(my_dic['nombre'])
print(my_dic.get('edad', 'No tiene edad'))

my_set = set([1, 2, 3])

my_set.add(2)  # No se agrega el 2 porque ya existe.
my_set.add(22)
my_set.remove(2)
print(my_set)

my_set2 = set([3, 4, 5])

union_de_sets = my_set.union(my_set2)

print(union_de_sets)
