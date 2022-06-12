
ano_start = input("Digite o ANO INICIAL: ")

ano_stop = input("Digite o ANO FINAL: ")

def list_ano(ano_inicial, ano_fim):

    retorno = ''
    base = 0

    if ano_inicial > 1929:
        ano_ = 1930

        print(f'Valor Inicial informado: {ano_inicial}')

        while ano_ < 2023:

            ano_+=4

            if ano_ > ano_inicial:

                if ano_ < ano_fim:
                    base+=1
                    retorno += f'Teve copa em: {ano_}\n'  

        if base == 0:
            retorno += 'Não teve copa entre os anos informados\n'
            retorno += f'Valor Final informado: {ano_fim}\n'

        else:
            retorno +=f'Valor Final informado: {ano_fim}\n'  

    else:
        retorno +=f'Valor Inicial informado: {ano_inicial}\n'
        retorno +='Informe um valor maior que 1930\n'
        base+=1
        retorno +=f'Valor Final informado: {ano_fim}\n'
    return retorno

print(list_ano(int(ano_start), int(ano_stop)))
