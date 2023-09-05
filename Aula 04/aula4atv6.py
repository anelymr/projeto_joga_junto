#Tupla com 05 dados
bebidas = ('café', 'água', 'refrigerante', 'suco', 'vinho')
print(bebidas)

#Alterando a tupla para uma lista
bebidas_lista = list(bebidas)
print(bebidas_lista)
print('-'*30)

#Inserindo 02 dados extras na lista
bebidas_lista.append("cerveja")
bebidas_lista.append("frappucino")
print(f"A lista com duas bebidas adicionadas: {bebidas_lista}")
print('-'*30)

#Removendo o primeiro dado da lista
bebidas_lista.remove("café")
print(f"A lista sem o primeiro item: {bebidas_lista}")
print('-'*30)

#Removendo o último dado da lista
bebidas_lista.pop()
print(f"A lista sem o último item: {bebidas_lista}")
print('-'*30)

#Printando o primeiro dado da lista
print(f"A primeira cidade é: {bebidas_lista[0]}")
print('-'*30)

#Printando a quantidade de dados da lista
print(len(bebidas_lista))

#criando dicionario com nome, idade e profissão
pessoa = {
    "nome": "Mylena",
    "cidade": "Paulínia",
    "profissão": "Analista de teste"
          }
#Imprima somente o valor da chave >nome< do dicionário
print(pessoa["nome"])