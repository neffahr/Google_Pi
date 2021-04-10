'''
ACHANDO MAIOR VALOR
1º: CONVERTER OS NUM PARA UMA STR E SEPARA-LOS EM UMA LISTA COM BASE NOS NUMEROS PRIMOS,
SEPARANDO OS VALORES SEMPRE QUE HOUVER UM NÚMERO NÃO PRIMO.
2º: USAR O LEN() PARA DEFINIR A LARGURA DE CADA VALOR
3º: PEGAR O MAIOR VALOR E RETORNAR SUA INDEX PARA VOLTAR NA LISTA E PEGAR ESSA MESMA INDEX
'''
def group_primos():
    texto = open('Automatiza_Py\Atividade_Pi\Pi10000n.txt',"r")
    pi = texto.read()
    pi_valores = pi.split(".")
    pi_valores.remove('3')
    texto.close()
    pi_primos = list()
    index_finder = -1
    index_inicio = 0

    for x in pi_valores[0]:
        index_finder += 1
        join_numbers = pi_primos[index_inicio:index_finder]
        if (int(x) % 2 == 1) and not (int(x) == 1) or (int(x) == 2) or (int(x) != 9) or (int(x) != 6): # DEFININDO NUMEROS PRIMOS
            if (int(pi_valores[0][index_finder + 1]) % 2 == 0) or (int(pi_valores[0][index_finder + 1]) == 1) and not (int(pi_valores[0][index_finder + 1]) == 2):
                pi_primos.append(x + " ") # SE O PROXIMO VALOR NÃO FOR PRIMO
                pi_primos = "".join(join_numbers)
                pi_primos = pi_primos.split(" ")
                pi_primos.pop()
                index_inicio = index_finder + 1
            else:
                pi_primos.append(x) # SE O PROXIMO VALOR FOR PRIMO
                pi_primos = "".join(join_numbers)
                pi_primos = list(pi_primos)

        else: # NUMEROS NÃO PRIMOS
            print ('avaliando...')

    print (pi_primos)
    return pi_primos
    
group_primos()