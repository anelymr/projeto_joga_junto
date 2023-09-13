nome = input('Digite o seu nome: ')
aula1 = int(input('Digite o sua 1 nota: '))
aula2 = int(input('Digite o sua 2 nota: '))
aula3 = int(input('Digite o sua 3 nota: '))
aula4 = int(input('Digite o sua 4 nota: '))
nota_geral = (aula1 + aula2 + aula3 + aula4)
nota_media = (nota_geral / 4)

print(f"Olá, {nome}! Sua média é: {nota_media}.")