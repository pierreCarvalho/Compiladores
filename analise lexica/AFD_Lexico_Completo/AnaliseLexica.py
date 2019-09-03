arquivo = open('arquivo.txt', 'r')
texto = arquivo.readlines()
arquivo.close()

def mandarTabela(token,tipo,identificador,linha,coluna):
        #gerar tokens
        arquivo_tabela = open('tabela.txt','r')
        conteudo = arquivo_tabela.readlines()
        if token == 'VG':
                token = ','
        conteudo.append('{},{},{},{},{}\n'.format(identificador,token,tipo,linha,coluna))
        
        arquivo_tabela = open('tabela.txt','w')
        arquivo_tabela.writelines(conteudo)
        arquivo_tabela.close()

def procurar(letraCorrente,estadoCorrente):
    for i in range(len(vetor_transicoes)):
        if vetor_transicoes[i][0] == estadoCorrente and vetor_transicoes[i][1] == letraCorrente:
            return vetor_transicoes[i][2]

    return 'não existe'

simbolos = texto[0].rstrip().split(',')
print("Simbolos: ",simbolos)

estados = texto[1].rstrip().split(',')
print("Estados: ",estados)

estadoIni = texto[2].rsplit()
print("Estados inicias: ",estadoIni)

estadosFim = {}
vetor_fim = []
vetor_fim = texto[3].rstrip().split(',')
for i in range(len(vetor_fim)):
    a = vetor_fim[i].split('>')
    estadosFim[a[0]] = a[1]
print("Estados Finais: ",estadosFim)

vetor_transicoes = []
for i in range(4,len(texto)):
    transicoes = texto[i].rstrip().split(',')
    for j in range(len(transicoes)):
        a = transicoes[j].split(":")
        vetor_transicoes.append([a[0],a[1],a[2]])
print("Regras de transição: ",vetor_transicoes)

arquivoC = open('arquivoC.txt','r')
texto_codigo = arquivoC.readlines()

arquivo_tabela = open('tabela.txt','w')
arquivo_tabela.write('ID,Token,Token_tipo,Linha,Coluna,Ref \n')
arquivo_tabela.close()

letraCorrente = ''
estadoInicial = ''
estadoCorrente = ''
destino = ''
finalTmp = ''
token = ''
tipo = ''
identificador = 0
linha = 0

#for para achar o estado inicial
for i in range(len(estados)):
    if estados[i] == estadoIni[0]:
        estadoInicial= estadoIni[0]

#ler o arquivo para ver se é aceito
for i in range(len(texto_codigo)):
        token = ''
        mensagem = texto_codigo[i].rstrip()
        print(mensagem)
        estadoCorrente = estadoInicial
        indexador = 0
        linha = linha + 1
        coluna = 0
        while (indexador < len(mensagem)):                  
                letraCorrente = mensagem[indexador]
                print('letra a ser lida ',letraCorrente)
                print('estado atual ',estadoCorrente)
                #procura na lista transicao
                if letraCorrente == ',':
                        letraCorrente = 'VG'
                destino = procurar(letraCorrente,estadoCorrente)
                if destino == 'não existe':
                        if estadoCorrente in estadosFim.keys():
                                print("resetando o automato")
                                identificador = identificador + 1
                                print(token)
                                coluna = coluna +1
                                mandarTabela(token,estadosFim[tipo],identificador,linha,coluna)
                                estadoCorrente = estadoInicial
                                token = ''
                                indexador = indexador - 1
                        else:
                                print("Não existe transição para esse cara")
                else:
                        tipo = destino
                        token += letraCorrente
                        print("O Conjunto ({},{}) chegou em {}".format(estadoCorrente,letraCorrente,destino))
                        estadoCorrente = destino
                indexador = indexador +1

        if token != "":
                identificador = identificador + 1
                coluna = coluna +1
                mandarTabela(token,estadosFim[tipo],identificador,linha,coluna)

def line_count(fname):
    return sum(1 for line in open(fname))

nlinha = line_count('arquivoC.txt')
print(nlinha)