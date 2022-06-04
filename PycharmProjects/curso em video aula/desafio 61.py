print('Gerador de PA')
print('-='*10)
pa = int(input('qual o valor da pa? '))
ra = int(input('qual a razão ?'))
termo = pa
cont = 1
while cont <= 10:   # quando quiser que ele va ate um certo  ponto crie uma variavel contidade
    termo += ra       #  e coloque no while enquanto nao chegar ate essa contidade não pare
    cont += 1
    print('{} -=- '.format(termo), end='')
print('acabou ')
