import shutil

def escrever_arquivo(texto):

    # Se não passar o caminho cria onde o python está
    # sendo executado
    diretorio = 'D:/Projetos/python-dio/teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto + '\n')
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):

    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto + '\n')
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_notas = arquivo.read().split()
    #print(aluno_notas)
    lista_media = []
    for x in aluno_notas:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})

    return lista_media

def copiar_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'D:/projetos/notas_alunos.txt')

def mover_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'D:/projetos/')



if __name__ == '__main__':

    #lista_media = media_notas('notas.txt')
    #print(lista_media)
    #escrever_arquivo('Escrendo primeira linha do método')
    #ler_arquivo('teste.txt')
    #aluno = 'Daniel,5,10,2,4'
    #atualizar_arquivo('notas.txt', aluno)
    #copiar_arquivo('aula9_notas.txt')
    mover_arquivo('aula9_notas.txt')



