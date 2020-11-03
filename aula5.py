lista = [12, 10, 5, 7]
animal = ['cachorro', 'gato', 'elefante', 'arara']

#lista é mutavel a tupla não é mutavel

tupla = (1, 10, 12, 14)
print(tupla[2])
print(len(tupla))

#convertendo  lista em tupla

tupla_animal = tuple(animal)
print(tupla_animal)

#convertendo tuplas em lista
lista_numerica = list(tupla)
print(lista_numerica)
print(type(lista_numerica))

# animal.sort()
# lista.sort()
# print(animal)
# print(lista)
#
# animal.reverse()
# print(animal)
#
# if 'lobo' in animal:
#     print('Ja existe gato')
# else:
#     print('não existe  na lista')
#     animal.append('lobo')
#     print(animal) # adiciona elemento na lista

#animal.pop(0) #retirar elemento passando indice.
#print(animal)

#animal.remove('elefante') #remove elemente conhecido

