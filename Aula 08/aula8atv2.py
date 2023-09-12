"""
DESAFIO: Desenvolvam uma função para retornar se o número passado pelo usuario no console é par ou ímpar.

Caso o número de matrícula do(a) aluno(a) seja par imprima:
    VOCÊ ESTÁ NO TIME AZUL

Caso o número de matrícula do(a) aluno(a) seja impar imprima:
    VOCÊ ESTÁ NO TIME AMARELO
"""

#criando a função
def verificar_matricula(nro_matricula):
    if nro_matricula % 2 == 0:
        return "azul"
    else:
        return "amarelo"

#pedir para o usuário inserir o nro de matricula
nro_matricula = int(input("Digite o nro da matricula: "))

#verificando se é par ou impar
grupo = verificar_matricula(nro_matricula)

#Retorna o resultado no terminal
if grupo == "azul":
    print("VOCÊ ESTÁ NO TIME AZUL")
else:
    print("VOCÊ ESTÁ NO TIME AMARELO")