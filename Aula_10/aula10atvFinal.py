import requests

#***************** AUTORES ******************
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
    if response.status_code == 200:
        print(f"O Autor: '{nome_autor}' foi cadastrado com sucesso")
    else:
        print(f"Erro ao cadastraro o autor. Motivo: {response.status_code} - {response.text}")
    return response.json()

# CADASTRA NOVO AUTOR
novo_autor_nome = input("Digite o nome do novo autor: ").lower()

#LISTA ATUAL DOS AUTORES
autores = authors_lista()

# VERIFICA SE O AUTOR JÁ EXISTE NA LISTA
autor_existente = next((autor for autor in autores if autor["name"].lower() == novo_autor_nome), None)

if autor_existente:
    print(f"Autor já existe. ID: {autor_existente['id']}, Nome: {autor_existente['name']}")
else:
    autor_existente = authors_cadastro(novo_autor_nome)
    if "id" in autor_existente and "name" in autor_existente:
        print(f"Autor cadastrado com sucesso. ID: {autor_existente['id']}, Nome: {autor_existente['name']}")
    else:
        print(f"Autor não encontrado.")

#***************** GÊNERO ******************
# FUNÇÃO PARA CONSULTAR O ID DE GÊNERO DOS LIVROS
def genders_lista():
    url = f"http://apilivro.jogajuntoinstituto.org/genders/"
    response = requests.get(url)
    return response.json()

# FUNÇÃO PARA CADASTRAR A LISTA DE GÊNEROS
def genders_cadastro(genero_desejado, nro_squad):
    url = f"http://apilivro.jogajuntoinstituto.org/genders/"
    data = {
        "name": genero_desejado,
        "squad": nro_squad
    }
    response = requests.post(url, json=data)
    if response.status_code == 201:
        print(f"O Gênero: '{genero_desejado}' foi cadastrado com sucesso")
    else:
        print(f"Erro ao cadastrar o gênero. Motivo: {response.status_code} - {response.text}")
    return response.json()

# INFORME QUAL GÊNERO VOCÊ DESEJA DESCOBRIR O ID
genero_desejado = input("Digite o nome do gênero que você deseja cadastrar: ").lower()
nro_squad = input("Digite o seu squad: ")

# LISTA ATUAL DOS GÊNEROS
generos = genders_lista()

# VERIFICA SE O GÊNERO JÁ EXISTE NA LISTA
genero_existente = next((genero for genero in generos if genero["name"].lower() == genero_desejado), None)

if genero_existente:
    print(f"Gênero já existe. ID: {genero_existente['id']}, Nome: {genero_existente['name']}")
else:
    genero_cadastrado = genders_cadastro(genero_desejado, nro_squad)
    if "id" in genero_cadastrado and "name" in genero_cadastrado:
        print(f"Gênero cadastrado com sucesso. ID: {genero_cadastrado['id']}, Nome: {genero_cadastrado['name']}")
    else:
        print(f"Gênero não encontrado.")

#***************** LIVROS ******************
# FUNÇÃO PARA CONSULTAR O ID DE GÊNERO DOS LIVROS
def books_lista():
    url = f"http://apilivro.jogajuntoinstituto.org/books/"
    response = requests.get(url)
    return response.json()

# FUNÇÃO PARA CADASTRAR A LISTA DE GÊNEROS
def books_cadastro(nome_livro, descricao,id_author, id_genero):
    url = f"http://apilivro.jogajuntoinstituto.org/books/"
    data = {
        "title": nome_livro,
        "description": descricao,
        "author": id_author,
        "gender": id_genero,
    }
    response = requests.post(url, json=data)
    if response.status_code == 201:
        print(f"O Livro: '{novo_livro_cadastro}' foi cadastrado com sucesso")
    else:
        print(f"Erro ao cadastrar o Livro. Motivo: {response.status_code} - {response.text}")
    return response.json()

# INFORME QUAL LIVRO VOCÊ DESEJA CADASTRAR
novo_livro_cadastro = input("Digite o nome do livro que você deseja cadastrar: ").lower()
novo_livro_descricao = input("Digite a descrição do livro: ").lower()
autor_livro = int(input("Digite o ID do autor: "))
genero_livro = int(input("Digite o ID do genero: "))

# LISTA ATUAL DOS LIVROS
livros = books_lista()

# VERIFICA SE O LIVRO JÁ EXISTE NA LISTA
livro_existente = next((livro for livro in livros if livro["title"].lower() == novo_livro_cadastro), None)

if livro_existente:
    print(f"Livro já existe. ID: {livro_existente['id']}, Nome: {livro_existente['title']}")
else:
    livro_cadastrado = books_cadastro(novo_livro_cadastro, novo_livro_descricao,autor_livro,genero_livro)
    if "id" in livro_cadastrado and "title" in livro_cadastrado:
        print(f"Livro cadastrado com sucesso. ID: {livro_cadastrado['id']}, Nome: {livro_cadastrado['title']}")
    else:
        print(f"Livro não encontrado.")