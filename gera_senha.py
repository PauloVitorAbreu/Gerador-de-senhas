#criador de senhas
#perguntas: comprimento_senha, caracter_esp, CAPS(true ou falso), (26)
import random as r
import string as s

def cria_senha (comprimento_senha, caracter_esp, caps):
    alfabeto = list(s.ascii_lowercase)
    ca_esp = '!@#$%^&*()-_=+[]{};:\",.<>?/|\\'
    lista_esp = list(ca_esp)
    contador = 0
    senha = ''


    while contador != comprimento_senha:
        escolhe_posicao = r.randint(0, 25)
        pega_letra = alfabeto[escolhe_posicao]
        
        if caps == True:
            sorteia = r.randint(1,2)
            if sorteia%2 != 0:
                pega_letra = pega_letra.upper()
                senha += pega_letra 
            else:
                senha += pega_letra 

        if caracter_esp == True:
            sorteia_2 = r.randint(1,2)
            if sorteia_2%2 == 0:
                pos_esp = r.randint(0,28)
                pega_esp = lista_esp[pos_esp]
                senha += pega_esp
            else:
                senha += pega_letra

        else:
            senha += pega_letra 

        contador += 1

    return senha

comprimento_senha = int(input('quantos caracteres sua senha precisa ter: '))

caracter_esp = input('Diga em "sim" ou "não" se deseja incluir caracter especiais: ')
if caracter_esp == 'sim':
    caracter_esp = True
else:
    caracter_esp = False

caps = input('Diga em "sim" ou "não" se deseja incluir caracter em CAPSLOCK: ')
if caps == 'sim':
    caps = True
else:
    caps = False

resultado = cria_senha(comprimento_senha, caracter_esp, caps)
print(resultado)
