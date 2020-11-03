conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)
print(conjunto_uniao)

conjunto_inter = conjunto.intersection(conjunto2)
print(conjunto_inter)

conjunto_diff = conjunto.difference(conjunto2)
print(conjunto_diff)

conjunto_diffsime = conjunto.symmetric_difference(conjunto2)
print(conjunto_diffsime)

conjuntoa = {1, 2, 3}
conjuntob = {1, 2, 3, 4, 5}
conjuntosubset = conjuntoa.issubset(conjuntob)
print(conjuntosubset)
conjuntosuper = conjuntob.issuperset(conjuntoa)
print(conjuntosuper)

#convertendo lista para conjunto
lista =['cachorro', 'cachorro', 'gato', 'gato' ]
conjunto_animal = set(lista)
print(conjunto_animal)

#convertendo de conjunto para lista
lista_animal = list(conjunto_animal)
print(lista_animal)


# conjunto = {1, 2, 3, 4, 5}
# conjunto.add(6)
# conjunto.discard(2)
#
# print(conjunto)

