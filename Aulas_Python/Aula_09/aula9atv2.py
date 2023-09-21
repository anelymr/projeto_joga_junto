"""
Crie um DataFrame com os seguintes dados:
    Nome, idade e cidade. Sendo 3 pessoas moradoras de Recife, 2 de Salvador, 1 de são paulo e 1 de Manaus
    Depois, filtre os dados para exibir na tela apenas os moradores do Recife. 
"""
import pandas as pd

data = {
    'Nome': ['Guilherme', "César", "Charly", "Cristina", "Joaquim", "Natália", "Maria"],
    'Idade': [23, 21, 32, 56, 3, 32, 90],
    'Cidade': ['Recife','São Paulo', 'Recife', 'Recife', 'Salvador', 'Manaus', 'Salvador' ]
}

df = pd.DataFrame(data)

print(df[df['Cidade'] == 'Recife'])

"""
#para salvar o código em um tipo de arquivo
df.to_csv("minhaprimeiratabela.csv")
"""