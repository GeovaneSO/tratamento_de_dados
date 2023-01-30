# tratamento_de_dados

## Available Scripts

Instalar as dependências do projeto

### `pip install -r requirements`

Iniciar o servidor

### `python manage.py runserver`

Criar e rodar o container

### `docker compose up` or `docker-compose up`

## Fluxo da aplicação

Ao adicionar e submeter o arquivo CNAB.txt, que se encontra no diretório assets, o tratamento dos dados é realizado.

Com base nas informações contidas no arquivo um Process é criado.

## Features

O usuário cria sua conta na rota `account/register` e é direcionado para a rota de login `account/login`.

Com o login feito, o usuário vai para a página home de url `upload`. Nessa página é possível selecionar o arquivo CNAB.txt.

Os dados do arquivo são tratados e o saldo por loja é mostrado.

Esse fluxo não está em funcionamento por consequência de alguns bugs.
