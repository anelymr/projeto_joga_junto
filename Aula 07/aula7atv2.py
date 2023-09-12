"""
O desafio é o seguinte:
você vai criar uma lista de dados e, usando a biblioteca OS, interagir com o seu sistema operacional.
Além disso, também criará uma nova pasta para salvar o arquivo de texto txt.
"""
dados = ['dado 1', 'dado 2', 'dado 3']

import os

pasta_nome = 'dados_atividade'

if not os.path.exists(pasta_nome):
    os.makedirs(pasta_nome)

caminho_arquivo = os.path.join(pasta_nome, 'dados.txt')

with open(caminho_arquivo, 'w') as arquivo:
    for dado in dados:
        arquivo.write(f'{dados}\n')

if os.path.exists(pasta_nome):
    print(f"a pasta {pasta_nome} foi criada")
if os.path.exists(caminho_arquivo):
    print(f"o arquivo {caminho_arquivo} foi criado")