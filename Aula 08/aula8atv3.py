"""
Criem um scritp para:
    Ter um input de usuário para inserir os números de matrícula em uma lista. 
    Ter um validador nessa lista que permita a inserção de dados até ocupar 5 espaços index.
    Fazer um laço de repetição para passar todos os números da lista em uma função para verificar se o número é par ou ímpar.
"""

from aula8atv2 import verificar_matricula

#criando uma lista
nro_matricula = []

#solicitando ao usuario o numero
while len(nro_matricula) < 5:
    nro = int(input(f"Digite os numeros de matricula: "))
    nro_matricula.append(nro)

for nro in nro_matricula:
    grupo = verificar_matricula(nro)
    print(f"Sua matricula é: {nro} e você está no grupo: {grupo}")
