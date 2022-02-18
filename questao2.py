def verifica_digito(senha):#funcao para verificar se a senha possui um digito
    for digito in senha:
        if digito.isnumeric():
            return 1
    return 0

def verifica_letra_maiuscula(senha):#funcao para verificar se a senha possui letra maiuscula
    for digito in senha:
        if digito.isupper():
            return 1
    return 0

def verifica_letra_minuscula(senha):#funcao para verificar se a senha possui letra minuscula
    for digito in senha:
        if digito.islower():
            return 1
    return 0
def verifica_caractere(senha):#funcao para verificar se a senha possui caractere
    lista_caracteres = ['!','@','#','$','%','^','&','*','(',')','-','+']
    for digito in senha:
        if digito in lista_caracteres:
            return 1
    return 0

senha = input()
forca=0#variavel para validar a senha
forca+=verifica_digito(senha)
forca+=verifica_letra_maiuscula(senha)
forca+=verifica_letra_minuscula(senha)
forca+=verifica_caractere(senha)

if(forca==4 and len(senha)>=6):
    print(0)
elif (4-forca<=6-len(senha)):
    print(6-len(senha))
else:
    print(4-forca)
