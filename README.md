

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
> usuarios = ((0, 'xpto@xyz.com'), (1, 'xkcd@phd.com'), (2, 'tester@teste.com')])
- Para acessar um valor na tupla
> usuarios[0][0]

## Principais diferenças entre Listas, Dicionários e Tuplas
Tanto em listas "[]" como nas tuplas "()" acessamos os dados por meio dos índices. 
Nos dicionários "{}" o acesso aos dados é feito por meio da chave associada a eles.
Para adicionar elementos em um dicionário é preciso adicionar uma nova chave ao objeto a qual irá receber o valor do objeto.
Já entre tuplas e listas, a diferença fica por conta da chave da tupla poder receber uma lista de valores.