'''
Para cirar uma lista basta colocar: nome_da_lista [itens_da_lista]
'''
frase = 'Oi, tudo bem?'
L = ['João', 'Maria', 'José', 'Guilherme']
L.append('Romulo')#Metodo append serve para adicionar mais um item a listaa
L.remove('José')#Metodo remove serve para remover um item da lista. insere no final
#L.clear() #Metodo clear serve para esvaziar a lista.
L.insert(1, 'Pedro')#Metodo insert serve para inserir um item na posição desejada.
L[0] = 'Rabesh' #Substituindo um item de determinada posição de acordo com o indice da lista.
count = L.count('Pedro')#Metodo lista.count serve  para retornar quantos itens do item desejado tem repetidos.
print(L.pop())#Metodo que se asemelha ao pop de uma pilha, só pega o item do topo e remove
print(L)#Imprimindo a lista invertida é assim.
print(len(L))#O metodo len retorna a quantidade de que há na string, lista, etc.

frase_separada = frase.split(',') #O metodo split serapara a frase onde vc quer. E transforma em uma lista;
print(frase_separada)