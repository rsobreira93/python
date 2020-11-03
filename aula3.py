
nota1 = float(input('Primeiro bimestre: '))
if nota1 > 10:
    nota1 =  float(input('Você digitou errado. Primeiro bimestre: '))
nota2 = float(input('Segundo bimestre: '))
if nota2 > 10:
    nota2 =  float(input('Você digitou errado. segundo bimestre: '))
nota3 = float(input('Terceiro bimestre: '))
if nota3 > 10:
    nota3 =  float(input('Você digitou errado. terceiro bimestre: '))
nota4 = float(input('Quarto bimestre: '))
if nota4 > 10:
    nota4 =  float(input('Você digitou errado. quarto bimestre: '))

media = (nota1 + nota2 + nota3 + nota4)/4
print(media)
# if nota1 <= 10 and nota2 <= 10 and nota3 <= 10 and nota4 <= 10:
#     print('media: {}'.format(media))
# else:
#     print('foi informado alguma nota errada!')

# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo valor: '))
#
# resto_a = a % 2
# resto_b = b % 2
# if(resto_a == 0 or not resto_b > 0):
#     print('foi digitado um numero par')
# else:
#     print('nenhum numero par foi digitado')


# a = float(input('Primeiro valor: '))
# b = float(input('Segundo valor: '))
# c = float(input('Terceiro valor: '))
# if(a > b and a > c):
#     print('O maior número é: {}'.format(a))
# elif(b > a and b >c):
#     print('O maior número é: {}'.format(b))
# else:
#     print('O maior número é: {}'.format(c))