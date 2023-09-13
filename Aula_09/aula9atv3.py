import pandas as pd

df = pd.read_csv("dados_ficticios.csv")

print(df[df['idade'] > 40])
print(df[df['renda'] > 5000])
print(df[df['renda'] > 15000])