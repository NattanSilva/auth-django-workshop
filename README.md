# Projeto DJango usando autenticação JWT

### Configurando .env

<p>Antes de executar o servidor crie um arquivo <code>.env</code> na raiz do projeto e preencha de acordo com o arquivo <code>.env.template</code>.</p>

```shell
  # Chave secreta do seu projeto
  SECRET_KEY=

  # Configs postgres
  
  # Nome da database que será usada do postgres
  PG_DATABASE=

  # Nome do seu usuário do postgres
  PG_USERNAME=

  # Senha do seu usuário do postgres
  PG_PASSWORD=

  # Endereço do postgres da sua máquina ou localhost
  PG_HOST=

  # Porta do postgres na sua máquina ou 5432
  PG_PORT=
```

### Configurações básicas do projeto

```shell
  # Criando venv
  python -m venv venv

  # Ativando a venv no windows
  .\venv\Scripts\activate

  # Ativando venv no Linux ou Mac
  source venv/bin/activate

  # Instalando as dependências do projeto
  pip install -r requirements.txt

  # Criando a migrations
  python manage.py makemigrations

  # Rodando as migrations
  python manage.py migrate

  # Ativando o servidor
  python manage.py runserver
```