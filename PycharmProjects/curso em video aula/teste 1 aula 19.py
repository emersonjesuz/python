pessoas = {'nome': 'Josiemerson', 'sexo': 'M', 'idade': 23}
print(f'o {pessoas["nome"]} tem {pessoas["idade"]} anos ')
print(pessoas.keys())  # serve pra mostra apenas o titulo do dicionario ! exp: nome, sexo, idade!
print(pessoas.values())  # serve pra mostra o conteudo do dicionario exp: josiemerson, sexo, idade!
print(pessoas.items())  # vai me mostra o titulo do dicionario e seu conteudo ou seja vai mostra tudo !
pessoas['nome'] = 'allan' # assim eu modifico meu dicionario
pessoas['peso'] = 90.5   # pra adicionar uma nova categoria eu coloco o titulo e seu conteudo e altomaticamente ele adiciona uma nova
del pessoas['sexo']  # del vai apagar a categoria(titulo) que eu fiz assim ele apaga tudo que tem na categoria idade
for k in pessoas.keys(): # usando o laço "for" com keys vai me mostra os titulos mas bonitos !
    print(k)
for l in pessoas.values(): # assim ele mostra apenas o conteudo !
    print(l)
for d, v in pessoas.items(): # assim ele vai mostra todos titulos e seu conteudos ! mas tenho que botar d = titulo v = o conteudo
    print(f'{d} = {v}')

