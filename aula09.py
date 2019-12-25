#manipulando text
frase = 'Curso em video'
print(frase)
#acessa um indice especifico
print(frase[2])
#acessa um range de caracteres
print(frase[3:7])
#acessa um range de caracteres (indice zero ate o limite)
print(frase[:2])
#acessa um range de caracteres (inicio definido ate o fim)
print(frase[1:])
#pula caracter
print(frase[::2])
#precura e conta quantidade de caracter
print(frase.count('C'))
print(frase.count('c'))
print(frase.upper().count('O'))
#conta a quantidade de caracteres
print(len(frase))
#remove os espaço em branco
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())
#realiza uma substituicao
print(frase.replace('video', 'audio'))
#quebra a string
dividido = frase.split()
print(dividido[2])
print(dividido[2][2])
#busca no texto
print('video' in frase) #True or False
print(frase.find('em')) #retorna a posicao
print(frase.find('ou')) #-1 nao encontrou
