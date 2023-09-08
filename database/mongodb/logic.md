# Lógica da Base de Dados MongoDB

Este diretório contém os principais componentes para a interação com uma base de dados MongoDB no projeto MiniLinkWeb.

## `connector.py`

O arquivo `connector.py` é responsável por estabelecer a conexão com o banco de dados MongoDB. Ele utiliza a biblioteca PyMongo para configurar a conexão com o servidor MongoDB especificado.

- `Database` (Classe): Esta classe encapsula a funcionalidade de conexão com o MongoDB. Ao criar uma instância da classe `Database`, você estabelece uma conexão com o banco de dados `MiniLinkWebDatabase`. Os atributos `user` e `link` permitem a interação com as coleções de usuários e links na base de dados.

## `dbcollections.py`

O arquivo `dbcollections.py` define as coleções de dados que serão usadas no projeto MiniLinkWeb.

### `UserCollection` (Classe)

A classe `UserCollection` representa a coleção de usuários na base de dados. Ela inclui métodos para:

- `signin(data)`: Registra um novo usuário na coleção se o email fornecido não estiver em uso.
- `login(data)`: Verifica se um usuário com o email fornecido existe na coleção e retorna os detalhes do usuário.
- `create_link(data)`: Cria um novo link encurtado na base de dados e associa-o ao usuário.

### `LinkCollection` (Classe)

A classe `LinkCollection` representa a coleção de links encurtados na base de dados. Ela inclui métodos para:

- `verify(url)`: Verifica se um link encurtado já existe na coleção com base no URL original fornecido.
- `create(url, owner)`: Cria um novo link encurtado na coleção de links. O método verifica se o proprietário (usuário) está autenticado antes de criar o link.
- `update_clicks(link_id)`: Atualiza o número de cliques para um link específico com base no ID do link.

### `HashUtils` (Classe)

A classe `HashUtils` fornece métodos para criar e verificar hashes de senhas usando o algoritmo Bcrypt. Ela é usada para hashear e verificar senhas localmente.

## `objects.py`

O arquivo `objects.py` define as classes de objetos usadas para representar links encurtados e usuários no código.

- `LinkObject` (Classe): Esta classe representa um link encurtado. Ela inclui métodos para reduzir um link longo a uma forma mais curta e gerar um objeto de link para armazenar na base de dados.
- `UserObject` (Classe): Esta classe representa um usuário e inclui métodos para criar hashes de senha usando o `HashUtils`.

## Observações

O projeto foi atualizado com a adição da classe `HashUtils` para lidar com operações de hashing de senhas localmente. Além disso, foram feitas melhorias gerais na organização do código, incluindo a implementação de injeção de dependência, melhor formatação e uso adequado de classes e métodos. O projeto está seguindo as boas práticas de segurança, como o uso de Bcrypt para armazenar senhas com segurança.

Este é um resumo da lógica dos principais componentes relacionados ao MongoDB no projeto MiniLinkWeb.
