valor_compra = float(input("Digite o valor da compra:"))
cupom_desconto = 10


if valor_compra >= 100:
    print(f"SUA SAÚDE É O QUE IMPORTA. APRESENTE ESSE CUPOM EM SUA PRÓXIMA COMPRA E GANHE R${cupom_desconto} REAIS DE DESCONTO.")

else:
    print(f"OBRIGADO POR ESCOLHER A MINHA FARMA. VOCÊ SABIA QUE COMPRAS ACIMA DE R$100 REAIS GERAM UM VOUCHER DE R${cupom_desconto} REAIS DE DESCONTO PARA A PRÓXIMA COMPRA?")