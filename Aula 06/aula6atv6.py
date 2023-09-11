palavra = input("Digite uma palavra: ")

#declarando as vogais
vogais = ['a','e','i', 'o', 'u']

#criando um contador
qtd_vogais = 0

#criando um loop
for letra in palavra:
    #if letra.lower() in 'a,e,i,o,u':
    if letra.lower() in vogais:
        qtd_vogais +=1

print(f"A quantidade de vogais na palavra {palavra} é: {qtd_vogais}")