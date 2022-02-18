def verifica_anagrama(lista_pares):
    '''
    funcao que recebe um par de caracteres e retorna se os mesmos são anagramas
    a funcao utiliza do comando ord que retorna o numero na tabela ASCII do caractere
    somando os valores da tabela ASCII e os comparando verificamos se os pares
    possuem os mesmos caracteres sendo assim anagramas
    '''
    anagramas=0
    for i in range(len(lista_pares)):
        ascii_par1 = 0
        ascii_par2 = 0
        for digito in lista_pares[i][0]:
            ascii_par1+=ord(digito)
        
        for digito in lista_pares[i][1]:
            ascii_par2+=ord(digito)
        if(ascii_par1 == ascii_par2):
            anagramas+=1
    return anagramas

def cria_palavra_base(palavra,letra_atual,tamanho_do_par):
    '''
    funcao para criar a palavra inicial de cada comparação baseado na letra atual por ex:
    i
    if
    ifa
    ifai
    ou
    f
    fa
    fal
    fail
    '''
    palavra_saida = ""
    for i in range(letra_atual,len(palavra)-1):
        palavra_saida+=palavra[i]
        if(len(palavra_saida)==tamanho_do_par):
            break
    return palavra_saida

def cria_pares(palavra,letra_atual,tamanho_do_par):
    '''
    funcao para criar os pares, baseado no tamanho de caracteres que estamos comparando
    ex:
    ['i','f']
    ['i','a']
    ['if','ai']
    '''
    lista_pares=[]#lista de saida com todos os pares formados
    par = []#lista auxiliar para guardar os pares em cada iteração
    palavra_base = cria_palavra_base(palavra,letra_atual,tamanho_do_par)
    for i in range(letra_atual,len(palavra)-1):
        palavra_nova = ""
        for j in range(i+1,len(palavra)):
                   palavra_nova += palavra[j]
                   if(len(palavra_nova)==tamanho_do_par):
                       par.append(palavra_base)
                       par.append(palavra_nova)
                       lista_pares.append(par)
                       break
        
        par=[]
    return lista_pares

        
palavra=input()
tamanho_do_par=1#varial para definir o tamanho dos pares que vamos comparar(1,2,3,...)
cont_anagramas=0#contador de anagramas que será mostrado na saida

for cont in range((len(palavra)//2)+1):#loop que vai de 0 até metade da palavra para criar os pares de anagramas
    for i in range(len(palavra)):#para cada letra na palavra
        pares = cria_pares(palavra,i,tamanho_do_par)#verificamos os pares formados por ela
        anagrama = verifica_anagrama(pares)#contamos quantos desses são anagramas
        cont_anagramas+=anagrama#somamos ao contador de saida
    tamanho_do_par+=1#aumentamos o tamanho do par em 1
print(cont_anagramas)













