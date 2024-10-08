# API REST com Flask - the Games

## Criar o ambiente virtual
```bash
python -m venv venv
```

## Ativar o ambiente virtual

No Windows:

- Em alguns casos é necessário realizar esse comando no powershell para que seu usuá possa ativar no windows:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Ai sim rodar o comando para ativar o ambiente virtual

```bash
.\venv\Scripts\activate
```
No Linux/MacOS:
```bash
source venv/bin/activate
```

## Desativando o ambiente virtual

```bash
deactivate
```

## Exportando a lista de dependências
```bash
pip freeze > requirements.txt
```

## Instalando dependências do requirements
```bash
pip install -r requirements.txt
```

## Instalar Flask-Restful
```bash
pip install flask-restful
```

## Instalar Flask-PyMongo
```bash
pip install flask-pymongo
```

## Instalar Flask Marshmallow
```bash
pip install flask-marshmallow
```