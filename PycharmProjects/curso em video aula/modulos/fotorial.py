from uteis import fatorial
num = int(input('Digite um valor : '))
fat = fatorial.fatorial(num)
print(f'o fatorial de {num} é {fat}')
print(f'o dobro de {num} é {fatorial.dobro(num)}')
print(f'o triplo de {num} é {fatorial.triplo(num)}')
