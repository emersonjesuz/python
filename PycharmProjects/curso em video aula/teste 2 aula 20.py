def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'a soma entre A + B = {s}')


soma(b=2, a=3)  # tem como escolher no programa principal qual valor fica com A e com B
soma(7, 2)   # se eu n deixar explicito o primeiro valor é A e o segundo é B

def contador(* num):  # usando * ele vai dobra minha tupla pra receber varios valores msm que não saiba quantos
    tam = len(num)
    print(f'eu recebi {num} e são ao todo {tam} valores')


contador(5, 6, 3, 1, 9)
contador(2, 5, 1, 6, 8)


