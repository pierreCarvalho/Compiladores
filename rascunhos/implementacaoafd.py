
arquivo = open('conf.afd', 'r')
texto = arquivo.readlines()
arquivo.close()

simbolos = texto[0].rstrip().split(',')
print("Simbolos: ",simbolos)

estados = texto[1].rstrip().split(',')
print("Estados: ",estados)

estadoIni = texto[2]
print("Estados inicias: ",estadoIni)

vetor_fim = []
estadosFim = texto[3].rstrip().split(',')
for i in range(len(estadosFim)):
    estadosFim = estadosFim[0].split('>')

print("Estados Finais: ",estadosFim)

transicoes = texto[4].rstrip().split(',')
vetor_transicoes = []
#meuDicionario = {}
for i in range(len(transicoes)):
    a = transicoes[i].split(":")
    vetor_transicoes.append([a[0],a[1],a[2]])
print("Regras de transição: ",vetor_transicoes)