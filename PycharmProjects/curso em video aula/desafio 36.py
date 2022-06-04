casa = float(input('digite o valor da casa:'))
salario = float(input('digite seu salario'))
ano = float(input('em quantos anos vai pagar ?'))
t= casa /(ano *12)
d = salario*30/100     # salario-(salario*70/100)  outra forma de calcula a porcentagem de 30 % de um valor
if d <= t:
    print('desculpa, seu pedido de emprestimo foi \033[31m negado \033[m')
elif d > t:
    print('seu emprestimo foi \033[32maprovado \033[m') # ,end='' vai colocar o print de baixo na mesma linha
    print('sua mensalidade vai ser: \033[33m{:.2f}R$\033[m'.format(t),end= '')
print(' seu salario : \033[31m{:.2f}R$\033[m\n  valor da casa :\033[31m {:.2f}R$\033[m\n  anos proposto pra pagar : \033[31m{:.0f} anos\033[m'.format(salario,casa,ano))
