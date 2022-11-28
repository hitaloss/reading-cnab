# CNAB - Interpretador

## Para rodar a aplicação, inicie o ambiente virtual "venv":

```
python -m venv venv
```

#

## Para entrar no ambiente virtual:

- Linux:

```
  source venv/bin/activate
```

- Windows:
  **(terminal bash)**

```
  source venv/Scripts/activate
```

- Windows:
  **(terminal powershell)**

```
  .\venv\scripts\activate
```

#

## A seguir, baixe todas as dependências rodando o comando:

```
pip freeze -r requirements.txt
```

#

## Execute as migrações para criar o db.sqlite e fazer persistência de dados:

- Linux:

```
  ./manage.py migrate
```

- Windows:
  **(terminal bash)**

```
  python manage.py migrate
```

- Windows:
  **(terminal powershell)**

```
  .\manage.py migrate
```

## Envio de Arquivo:

Com o servidor rodando é possivel acessar algumas rotas, seriam elas :

envio de aruivo CNAB.txt

```bash
  http://127.0.0.1:8000/api/cnab/

```
