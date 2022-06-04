a = [2, 3, 5, 6]
b = a # assim ele nai fazer uma lista igual, apenas duas lista interligadas sendo que se se mexer em uma, ambas vao ser
b = a[:] # assim (b) vai receber os itens de (a)  e nao criando uma conexão entre elas podendo mexer em uma  e nao interfeiri na outras
b[2] = 8 # assim da pra modificar B sem modificar A
print(f'lista A{a}')
print(f'lista B{b}')