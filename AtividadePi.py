def group_primos(): # AGRUPA TODAS AS SEQUÊNCIAS DE NUMEROS PRIMOS 
    texto = open('Automatiza_Py\Atividade_Pi\Pi10000n.txt',"r")
    pi = texto.read()
    pi_valores = pi.split(".")
    pi_valores.remove('3')
    texto.close()
    pi_primos = list()

    for index_finder, x in enumerate(pi_valores[0]):

        if int(x) not in [0,1,4,6,8,9]: # DEFININDO NUMEROS PRIMOS

            if int(pi_valores[0][index_finder + 1]) in [0,1,4,6,8,9]:
                pi_primos.append(x + " ") # SE O PROXIMO VALOR NÃO FOR PRIMO
            else:
                pi_primos.append(x) # SE O PROXIMO VALOR FOR PRIMO
        
        else: # NUMEROS NÃO PRIMOS
            print ('avaliando...')

    # APÓS PASSAR POR TODOS OS NÚMEROS, IRÁ SEPARÁ-LOS EM GRUPOS
    pi_primos = "".join(pi_primos)
    pi_primos = pi_primos.split(" ")
    pi_primos.pop()
    return pi_primos

def max_seq(primos, num_casas): # COM BASE EM UM NÚMERO DE CASAS, PEGA A MAIOR SEQUÊNCIA MAIS PERTO DO PONTO DECIMAL E RETORNA A SEQUÊNCIA
    index_len = dict()

    for num_primo in primos:
        if len(num_primo) > num_casas :
            primos.remove(num_primo)

    for primo_index, num_primo in enumerate(primos):
        index_len[primo_index] = len(num_primo)

    seq_values = list(index_len.values())
    max_index = seq_values.index(num_casas)
    max_num = primos[max_index]
    print (max_num)

# INTERFACE
gp = group_primos()

while True:
    try:
        casas = int(input('Com base em quantas casas decimais você quer avaliar as sequências de numeros primos no Pi? --> '))
        if casas != 0:
            max_seq(gp, casas)
            continuar = input('Quer avaliar denovo? S/N --> ')
            if continuar == "S" or continuar == "s":
                continue
            if continuar == "N" or continuar == "n":
                break
        else:
            print ('O número de casas avaliadas nas sequências deve ser maior que 0!')
            continue
    except:
        print ('Número de casas a ser avaliadas é grande demais!')
        continue