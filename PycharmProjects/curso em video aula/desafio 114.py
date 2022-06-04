import urllib
import urllib.request

try:
    ssite = urllib.request.urlopen('http://www.pudim.com.br')
    site = urllib.request.urlopen('https://www.gov.br')   # programa pra pesquisar site .. mas so serve se for servidor oficial
except urllib.erro.URLError:
    print('o site NÃO esta acessivel ')
else:
    print('O SITE ESTA ACESSIVEL!!')
    print(ssite.read())   # busca o conteudo HTML do site
