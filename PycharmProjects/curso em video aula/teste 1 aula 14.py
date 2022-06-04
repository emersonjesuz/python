#r = 'S'
#while r == 'S':
 #   m = int(input('digite um valor '))
  #  r = str(input('ainda quer continua [N /S] ')).upper()
#print('fim')


par = impar = 0
num = ''
while num != 0:
    num = int(input('digite um valor '))
    if num != 0:
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
print('você digitou {} pares e {} numeros impares'.format(par, impar))
