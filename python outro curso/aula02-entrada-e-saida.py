'''
nome = 10.5
tipo = type(nome)

if tipo is str: isso é para comparar o tipo da variavel.
    print('Tipo String')
elif tipo is int:
    print("Tipo Inteiro")
elif tipo is float:
    print("Tipo FLOAT")

print(nome)
'''
nome = str(input("Digite seu nome: "))
cpf = int(input("Digite seu cpf: "))
endereco = str(input("Digite seu endereço: "))
altura = float(input("Digite sua altura: "))
telefone = int(input("Digite seu telefone: "))

print("Ola {} seu cpf é: {}\n seu endereço é: {}\n sua altura é: {}\n seu telefone é: {}".format(nome,cpf,endereco,altura,telefone))