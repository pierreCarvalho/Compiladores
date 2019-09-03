'''
exercicio 1 - Pré-processador de texto
Implemente um programa que elimine os comentários em um código-fonte em linguagem C.
Lembrando que em linguagem C existem dois tipos de comentários:
// - define o comentário a partir das barras até o final da LINHA
/* texto */ - define o comentário entre os delimitadores, podendo ser (o comentário) em várias linhas
'''

arquivo = open('arquivo.txt', 'r')


texto = arquivo.readlines()
arquivo.close()

#print(texto)
novoArquivo = open('novoArquivo.txt','w')

for i in range(len(texto)):
    
    comentario = texto[i].find('//')
    if(comentario != 0):
        #print("Tem comentário!")
        print(texto[i])
        novoArquivo.writelines(texto[i])
print("O arquivo foi compilado!")
novoArquivo.close()
