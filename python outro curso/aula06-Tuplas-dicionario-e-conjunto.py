minha_lista = ['Guilherme', 'Pedro'] #Lista (list)
minha_tupla = ('Guilherme', 'Pedro') #Tupla (tuple)
#A diferença entre ambas é que a tupla não é tão mutavel quanto a lista, ou seja, não tem metodo append, remove, etc...
meu_dicionario = {'nome': 'Romulo', 'Idade': 26} #Dicionario (dict) 
meu_conjunto = {'Romulo', 'João'} #conjunto (set)
#Adiferença entre conjunto e lista é que no conjunto não pode haver dois itens repetidos. E o conjunto não é ordenado, ou seja, não existe indice 0,1,2,3 etc.

#pesquisa em qualquer estrutura menos em dicionario
if 'Romulo' in meu_conjunto:
    print("OK")

#pesquisa no dicionario.
if 'Romulo' in meu_dicionario.values():
    print("OK!")
