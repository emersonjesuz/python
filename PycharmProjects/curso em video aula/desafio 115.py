dados = {'Ana lucia': 44, 'Bianca moreira': 33, 'João araujo': 66, 'marcelo filho': 45}
final = False
while not final:
    print('-' * 40)
    print('            MENU PRINCIPAL')
    print('-' * 40)
    print('''\033[33m1-\033[m \033[34mVer pessoas cadastradas\033[m
\033[33m2-\033[m \033[34mCadastrar novas pessoas 
\033[33m3-\033[m \033[34mSair do sistema\033[m''')
    print('-' * 40)
    valida = False
    while not valida:
        try:
            opc = int(input('\033[33mSua opção:\033[m'))
            if opc > 3 or opc < 1:
                print('\033[31m ERRO""" USE APENAS AS OPÇÕES ACIMA!\033[m')
        except(TypeError, ValueError):
            print('\033[31m ERRO""" USE APENAS AS OPÇÕES ACIMA!\033[m')
        else:
            if opc == 1 or opc == 2 or opc == 3:
                if opc == 1:
                    print('-' * 40)
                    print('          PESSOAS CADASTRADAS ')
                    print('-' * 40)
                    for k, v in dados.items():
                        print(f'{k}', end='')
                        print(f'   \t{v} anos')
                    valida = True
                if opc == 2:
                    print('-' * 40)
                    print('          NOVO CADASTRO ')
                    print('-' * 40)
                    nome = str(input('Nome:'))
                    idadecert = False
                    while not idadecert:
                        try:
                            idade = int(input('Idade:'))
                        except(ValueError, TypeError):
                            print('\033[31m ERRO""" DIGITE UM NUMERO INTEIRO VALIDO!\033[m')
                        else:
                            dados[nome] = nome
                            dados[nome] = idade
                            print(f'Registro de {nome} adicionado.')
                            idadecert = True
                    valida = True
                else:
                    if opc == 3:
                        valida = True
                        final = True
print('-' * 40)
print('\033[32mPrograma finalisado\nvolte sempre !')
