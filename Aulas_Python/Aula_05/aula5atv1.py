"""
USANDO IF: Construa um script para verificar se o usuário tem uma idade maior que 18 anos,
se tiver, imprima na tela (Indivíduo possui idade mínima para dirigir)

USANDO ELSE: Complemente o script feito,
imprimindo na tela (Indivíduo NÃO possui idade mínima para dirigir)

USANDO ELIF: Complemente o script feito,
imprimindo na tela (Indivíduo tem entre 17 e 18 anos e ainda NÃO está apto para dirigir)
"""
idade = int(input("Digite sua idade:"))

if idade >=18:
    print("Individuo possuí idade minima para dirigir.")

elif idade >16 and idade <=18:
    print("Indivíduo tem entre 17 e 18 anos e ainda NÃO está apto para dirigir")

else:
    print("Ïndividuo não possuí idade minima para dirigir.")

