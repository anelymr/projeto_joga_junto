import requests

#FUNÇÃO PARA LISTAR OS AUTORES
def authors_lista():
    url = f"http://apilivro.jogajuntoinstituto.org/authors/"
    response = requests.get(url)
    return response.json()

#FUNÇÃO PARA CADASTRAR A LISTA DE AUTORES
def authors_cadastro(nome_autor):
    url = f"http://apilivro.jogajuntoinstituto.org/authors/"
    data = {
        "name": nome_autor
    }
    response = requests.post(url, json=data)
    if response.status_code == 201:
        print(f"O Autor: '{nome_autor}' foi cadastrado com sucesso")
    else:
        print(f"Erro ao cadastraro o autor. Motivo: {response.status_code} - {response.text}")
    return response.json()

# CADASTRA NOVO AUTOR
novo_autor_nome = input("Digite o nome do novo autor: ")

#LISTA ATUAL DOS AUTORES
autores = authors_lista()

# VERIFICA SE O AUTOR JÁ EXISTE NA LISTA
autor_existente = next((autor for autor in autores if autor["name"] == novo_autor_nome), None)

if autor_existente:
    print(f"Autor já existe. ID: {autor_existente['id']}, Nome: {autor_existente['name']}")
else:
    autor_cadastrado = authors_cadastro(novo_autor_nome)
    if "id" in autor_cadastrado and "name" in autor_cadastrado:
        print(f"Autor cadastrado com sucesso. ID: {autor_cadastrado['id']}, Nome: {autor_cadastrado['name']}")
    else:
        print(f"Autor não encontrado.")
