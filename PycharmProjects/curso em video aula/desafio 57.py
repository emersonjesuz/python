
f = 'FEMININO'
m = 'MASCULINO'
o = str(input('qual o seu sexo [M/F]: ')).strip().lower()[0]
while o != 'f' and o != 'm':
    if o != f and o != m:
         o = str(input('dados invalidos, por favor  informe seu sexo')).strip().lower()[0]
if o == 'f':
    print('SEXO " {} " REGISTRADO COM  SUCESSO!'.format(f))
elif o == 'm':
    print('SEXO " {} " REGISTRADO COM SECESSO!'.format(m))


sexo = str(input('informe seu sexo [M/F]')).strip().upper()[0]
while sexo not in 'FMfm':
    sexo = str(input('dados invalidos, informe seu sexo ')).strip().upper()[0]
print('sexo {} registrado com sucesso'.format(sexo))