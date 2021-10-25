# Primeiros Passos com Python

# Objetivo
- Apresentar exemplos de projetos e atividades utilizando conceitos introdutórios ao python e conhecer sua utilização.

## Variaveis
- Definir uma variavel em python é bem simples, basta em uma linha vazia, definir nossa variavel e setar um valor.
> minha_variavel = 'hoje' <br>
> minhaSegundaVariavel = 'amanhã' <br>
> qualquercoisa = 'ontem' <br>
> primeiro =  1
> segundo = 2
> eh_hoje = true

- Observe o padrão empregado para definir uma variavel, note que sempre haverá o nome da variavel um simbolo de igual e o seu valor.
- Veja nos exemplos abaixo formas incorretas de se definir uma variavel.
> // <strong style="color:red">os exemplos abaixo são casos incorretos de definição de variavel </strong><br>
> minha variavel  = 'hoje' // ira resultar em um erro por haver um espaço no nome da variavel <br>
> MinhaSegundaVariavel = 'amanhã' // pelos padrões de definição de varaiveis essa definição está errada <br> 
> éhoje = true // é errado esse tipo de definição, pois não devemos utilizar um acento ou caractere especial no nome da variavel<br>
> primerio == 1 // é errado, só se usa 2 iguais juntos (==) quando se está querendo comparar os valores para saber se é verdadeiro ou falso

## Decisões
- Iremos destacar 3 tipos de decisões e explanar cada caso.
- IF | utilizado para inciar toda condição de comparação. Em pt-br é o mesmo de 'SE'.
> total = 10 <br>
> if(total == 10): // podemos ler esse caso como: Se Total for igual a 10 então será feito o que está dentro da decisão 
- ELIF | utilizado após a primeira condição de IF, para então tentar uma segunda condição. Em pt-br é o mesmo que 'SENÃO, ENTÃO É'
> total = 11 <br>
> if(total == 10): <br>
>   ...<br>
> elif(total == 11): // podemos ler esse caso como: Se Total for igual a 11 então será feito o que está dentro da decisão<br>
- ELSE | Diferente dos outros casos, é uma condição onde pode ser qualquer coisa menos as validadas anteriormente, é o resto que não foi validado. Em pt-br é o mesmo de 'SENÃO'
> total = 110032 <br>
> if(total == 10): <br>
>   ...<br>
> elif(total == 11):<br> 
>   ...<br>
> > elif(total == 12):<br> 
>   ...<br>
> else: // não necessita de comparação, é o resto do que não foi decidido durante os if e elif

## Loop
- Para loop temos o While e o For
- O while é executado enquanto for verdade a situação definida nele
> doenca_infectocontagiosa != "SIM" and doenca_infectocontagiosa != "NAO":
- O for será executado enquanto houver valores em uma lista que foi definida em sua criação
> for valor in range(1,11,1):
> 
## Funções
- Toda função é defina pelo termo 'def' e pode receber quantos parametros for necessário. 
- Uma função pode ou não ter retorno.
- Uma função pode ser chamada a qualquer momento.
- Em caso a função esteja em outro script é fundamental que ela seja importada no script.
> def excluirTodos(lista): <br>
> ... <br>
> return "Itens excluídos." <br>


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

## Socket 
- Permitindo a comunicação via protocolos UDP ou TCP foi possivel abrir um canal de comunicação entre 2 servidores distintos.
- Todas as comunicações são realizadas através do import:
> from socket import *

## Portas Serial
- Permite lista as portas de comunicação no computador através do import:
> from serial.tools import list_ports

## Links Úteis
- [Google Api Console](https://console.cloud.google.com/apis/dashboard)

# Repositórios
- [Iris Data Set](https://archive.ics.uci.edu/ml/datasets/iris)
- [Breaking Bad Api](https://breakingbadapi.com/documentation)

# Dependências
- [PyGeocoder - Geolocalização](https://pypi.org/project/pygeocoder/)
- [Decouple - Environments Variables](https://pypi.org/project/python-decouple/)