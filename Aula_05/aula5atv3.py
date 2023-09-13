frequencia_aluno = int(input("Digite a frequência do aluno:"))


if frequencia_aluno >= 2 and frequencia_aluno <= 20:
    print(f"VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO")

elif frequencia_aluno >= 21:
    print(f"UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ")

else:
    print(f"QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO.")