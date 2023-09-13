valor_compra = float(input("Digite o valor da compra:"))
desconto_min = 10
desconto_max = 30

if valor_compra >= 500.00:
    print(f"Parabéns! Você ganhou um super desconto de {desconto_max}%")

elif valor_compra >= 250.00 and valor_compra < 500.00:
    print(f"Parabéns! Você ganhou {desconto_min}% de desconto, mas pode ganhar {desconto_max}% se sua compra for acima de R$500,00")

else:
    print(f"Poxa, falta pouco para você ganhar {desconto_min}% de desconto em sua compra.")