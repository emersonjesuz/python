try:
    a = int(input('numerador'))
    b = int(input('denominador '))
    r = a / b
except Exception as erro: # programa pra descobrir o erro e seu tipo e coloca uma frase quando o erro e encontado
    print(f'o erro encontrado foi {erro.__class__}')
except (ValueError, TypeError):
    print('ERRO ENCOTRADO!!!')
except ZeroDivisionError:# os tipo de erro começa maiusculo
    print('não é possivel dividir por zero')
except KeyboardInterrupt:
    print('o usuario não quis informa valor')
else:
    print(f'o resultado é {r:.1f}')
finally:
    print('volte sempre')