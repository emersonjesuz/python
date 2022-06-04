num=str(input('digite um numero:'))
print('esse é o seu numero:{}'.format(num))
print('unidade:{}'.format(num[3]))
print('dezena:{}'.format(num[2]))
print('centena:{}'.format(num[1]))
print('milhar:{}'.format(num[0]))

num1=int(input('digite um numero'))
n=str(num1)
print('unudade:{}'.format(n[3]))
print('dezena:{}'.format(n[2]))
print('centena:{}'.format(n[1]))
print('unidade:{}'.format(n[0]))

n1=int(input('digite um numero: '))
u= n1 //1 % 10
d=n1//10%10
c=n1//100%10
m=n1//1000%10
print('unidade:{}'.format(u))
print('dezena:{}'.format(d))
print('centena:{}'.format(c))
print('milhar:{}'.format(m))