
class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        try:
            self.lista_plano = ['basic', 'premium']
            if plano not in self.lista_plano:
                print('plano Invalido!!')
        except(AttributeError, TypeError):
            print('erro! tente novamente !!!')
        else:
            self.plano = plano

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_plano:
            self.plano = novo_plano
        else:
            print('PLANO INAVALIDO')

    def ver_fimes(self, filme='pesquisando'):
        print('-' * 30)
        print(f'{"PREMIUM":.^30}')
        print('-' * 30)
        print('''- Harry potter
- Madagasgar 
- 365''')
        print('-' * 30)
        print(f'{"BASIC":.^30}')
        print('-' * 30)
        print('''- Era do gelo
- 13 é de mas
- anaconda''')
        print()
        f = False
        while not f:
            filme = str(input('Qual opção desejada ?  '))
            filmegeral = dict()
            filmegeral['premiufilm'] = 'Harry potter', 'Madagasgar', '365'
            filmegeral['basicfilm'] = 'Era do gelo', '13 é de mas', 'anaconda'

            if self.plano == 'premium':
                if filme in filmegeral['premiufilm']:
                    print(f'{"CATEGORIA PREMIUM":.^30}')
                    print(f'ver o filme  {filme}')
                    f = True
                elif filme in filmegeral['basicfilm']:
                    print(f'{"CATEGORIA BASIC":.^30}')
                    print(f'ver o filme {filme}')
                    f = True
                else:
                    print('filme não encontrado no nosso catalago')
            elif self.plano in 'basic':
                if filme in filmegeral['basicfilm']:
                    print(f'{"CATEGORIA BASIC":.^30}')
                    print(f'ver o filme {filme} ')
                    f = True
                elif filme == filmegeral['premiufilm']:
                    print('faça um upgrade para premium para ver o filme !')
                else:
                    print('filme não encontrado no catalago ')
                    print('caso queira mas filmes assine o PREMIUM')
            else:
                print('plano invalido'
                      'por favor colocar o nome do filme carreto na pesquisa')
        print('obrigado !!')


pl = ''
print('-' * 30)
print(f'{"NETFLIX/ CADASTROS":^30}')
print('-' * 30)
nom = str(input('nome:')).upper()
emai = str(input('email:')).upper()
while True:
    print('-' * 30)
    print(f'''{"PLANOS":^25}
0 ] PARA PREMIUM
1 ] PARA BASIC''')
    print('-' * 30)
    try:
        plan = int(input('QUAL OPÇÂO:'))
        if 0 < plan > 1:
            pl = plan
            print('erro plano invalido!')
    except:
        print('erro tente novamente ')
        continue
    else:
        if plan == 0:
            plano1 = 'premium'
            break
        elif plan == 1:
            plano1 = 'basic'
            break
cliente = Cliente(nom, emai, plano1)
if cliente.plano in 'basic' or 'premium':
    print(f'Nome: {cliente.nome}')
    print(f'email: {cliente.email}')
    if cliente.plano in 'basic':
        print(f'plano- BASIC')
    else:

        print('Plano- PREMIUM')
opc = str(input('deseja mudar seu plano ? [S,N]:')).upper()
if opc == 'S':
    print(f'seu plano vai mudar de {cliente.plano} para ', end='')
    if cliente.plano in 'basic':
        cliente.mudar_plano('premium')
        print(f'PREMIUM')
    else:
        cliente.mudar_plano('basic')
        print('BASIC')
else:
    print('Obrigrado por se cadastrar!!')
print('-' * 30)
print(f'{"FILMES":^30}')
print('-' * 30)
cliente.ver_fimes()
