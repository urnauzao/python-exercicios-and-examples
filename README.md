

## Listas
- Para criar uma lista em python basta definir uma variavel como:
> usuarios = {}
> ##### //ou
> usuarios = {1,2,3}
> ##### //ou
> usuarios = {"alfa":"valores", "beta":"valores"}
- Para acessar um valor na lista podemos usar:
> usuarios[0] 
> ##### //ou
> usuarios.get(0)
- Para remover uma valoar na lista podemos usar:
> del(usuarios[0])
> ##### //ou
> usuarios.remove(0)
- Para adicionar um valor na lista podemos usar:
> usuarios.append(valor)

## Dicionários
 - Para setar um dicionário podemos usar:
> usuarios  = ["xpto@xyz.com", "xkcd@phd.com", "tester@teste.com"]
> ##### //ou, como é mais comum
> usuarios = []
> usuarios["luciano"] = "ativo"
> usuarios["frederico"] = "inativo"

## Tuplas
- Para acessar definir uma tupla:
> usuarios = ()
- Para setar valores em uma tupla:
> usuarios = ((0, 'xpto@xyz.com'), (1, 'xkcd@phd.com'), (2, 'tester@teste.com'))
- Para acessar um valor na tupla
> usuarios[0][0]

## Principais diferenças entre Listas, Dicionários e Tuplas
Tanto em listas "[]" como nas tuplas "()" acessamos os dados por meio dos índices. 
Nos dicionários "{}" o acesso aos dados é feito por meio da chave associada a eles.
Para adicionar elementos em um dicionário é preciso adicionar uma nova chave ao objeto a qual irá receber o valor do objeto.
Já entre tuplas e listas, a diferença fica por conta da chave da tupla poder receber uma lista de valores.

## Manipulando Arquivos
- Para manipular arquvios utilize:
> open("path/to/file.ext", modo)
- Os modos podem ser: 
  - 'r' - ler - open for reading (default)
  - 'w' - escrever - open for writing, truncating the file first
  - 'x' - Criar - open for exclusive creation, failing if the file already exists
  - 'a' - Adicionar - open for writing, appending to the end of the file if it exists
  - 'b' - return Binary - binary mode
  - 't' - return String -text mode (default)
  - '+' open for updating (reading and writing)
- Os modos podem ser combinados, como 'rw'
- utilize o comando abaixo para continuar no arquivo:
> with open("path/to/file.ext", "a") as arquivo:
- Caso não utilize o with, você será obrigado a fechar o arquivo com:
> arquivo = open("path/to/file.ext") <br>
> arquivo.write("meu texto") <br>
> arquivo.close
- Para ler uma linha
> arquivo.readline(0)
- Para ler todas as linhas
> arquivo.readlines()

## Manipulando String
- Formas de manipular uma string. texto[ posicao inicial : quantidade de informação a percorrer : passo ]
> texto = "Leia e Han Solo" <br>
> texto[0:4] #leia <br>
> texto[7:] #han solo <br>
> texto[-8:] #han solo <br>
> texto[::-1] #oloS naH e aieL <br>
> texto[::2] #Li  a oo

- Retonar uma lista 
> texto.split(" ")

- Encontrar uma string
> texto.find("o")

## Carregar JSON de um Arquivo
- utilize
> json.load(open("path/to/file.ext", "r"))

## Geocode
- Para utilizar a API do Google Maps é necessário:
  - Instalar o PyGeocoder
  - Acessar o Google Api Console(GAC)
  - Criar um projeto no GAC
  - Criar uma credencial para o projeto no GAC
  - Gerar o token de acesso ao Projeto no GAC
  - Passar o token nas requisições via PyGeocoder

## Informações do Sistema
- Para ter acesso a informações do sistema utilize a biblioteca "platform"
> exemplo: <br>
> import platform <br>
> platform.processor() # retorna o tipo de processador da maquina

## Informação de Usuário
- Para ter acesso a informações do usuário do sistema, utilize a biblioteca "getpass"
> exemplo: <br>
> import getpass <br>
> getpass.getuser() # retorna usuário logado

## Informações de Data e Hora
- Para ter acesso a informações de data e hora, utilize a biblioteca "datetime"
> exemplo: <br>
> from datetime import datetime
> datetime.now() # data atual completa

## Links Úteis
- [Google Api Console](https://console.cloud.google.com/apis/dashboard)

# Repositórios
- [Iris Data Set](https://archive.ics.uci.edu/ml/datasets/iris)
- [Breaking Bad Api](https://breakingbadapi.com/documentation)

# Dependências
- [PyGeocoder - Geolocalização](https://pypi.org/project/pygeocoder/)
- [Decouple - Environments Variables](https://pypi.org/project/python-decouple/)