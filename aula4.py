
nota1 = float(input('Primeiro bimestre: '))
while nota1 > 10:
    nota1 = float(input('Você digitou errado. Primeiro bimestre: '))
nota2 = float(input('Segundo bimestre: '))
while nota2 > 10:
    nota2 = float(input('Você digitou errado. segundo bimestre: '))
nota3 = float(input('Terceiro bimestre: '))
while nota3 > 10:
    nota3 = float(input('Você digitou errado. terceiro bimestre: '))
nota4 = float(input('Quarto bimestre: '))
while nota4 > 10:
    nota4 = float(input('Você digitou errado. quarto bimestre: '))

media = (nota1 + nota2 + nota3 + nota4)/4
print('A media é {}'.format(media))

# a = int(input('Entre com um valor: '))
# for i in range(a+1):
#     div = 0
#     for x in range(1, i+1):
#         resto = i % x
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print('Numero {} é primo'.format(i))


# a = int(input('Entre com um numero: '))
#
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     if resto == 0:
#        div += 1
#
# if div == 2:
#     print('Numero {} é primo'.format(a))
# else:
#     print('Numero {} nñao é primo'.format(a))