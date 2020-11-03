

arquivo = open('teste.txt', 'r')
lista = [1, 10]
try:
    divisao = 10 / 0
    numero = lista[3]
    texto = arquivo.read()
    x = a
except ZeroDivisionError:
    print('Não é possivel dividir por 0')
except IndexError:
    print('Erro por acessar indice invalido na lista')
except BaseException as ex:
    print(ex)
else:
    print('Executa quando não ouver execção.')
finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()