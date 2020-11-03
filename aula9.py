import  shutil

def escrever(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar(nome, texto):
    arquivo = open(nome,'a')
    arquivo.write(texto)
    arquivo.close()

def ler(nome):
    arquivo = open(nome,'r')
    texto = arquivo.read()
    print(texto)

def media(nome):
    arquivo = open(nome,'r')
    nota = arquivo.read()
    aluno = nota.split('\n')
    lista_media = []
    for x in aluno:
        nota_aluno = x.split(',')
        aluno = nota_aluno[0]
        nota_aluno.pop(0)
        print(aluno)
        print(nota_aluno)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(nota_aluno))
        lista_media.append({aluno:media(nota_aluno)})
    return lista_media

def copia_arquivo(nome):
    shutil.copy(nome, '../')

def move(nome):
    shutil.move(nome, 'c:/')

if __name__ == '__main__':
    #print(media('notas.txt'))
    #escrever('Primeira linha.\n')
    #aluno = '\nEuder, 5, 8, 9, 10'
    #atualizar('notas.txt', aluno)
    #ler('teste.txt')
    copia_arquivo('notas.txt')