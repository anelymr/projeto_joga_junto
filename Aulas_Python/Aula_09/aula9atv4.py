from faker import Faker
import pandas as pd

#inicializando biblioteca
faker = Faker('pt_BR')

#criando função
def persona():
    nome = faker.name()
    cidade = faker.city()
    return {'Nome': nome, 'Cidade': cidade}

#quantidade de pessoas
qtd_pessoas = 1

#criando lista
personas = []

#adiciona a pessoa a lista
for i in range(qtd_pessoas):
    personas.append(persona())

#criar dataframe
df = pd.DataFrame(personas)

#salvar em csv
df.to_csv("aula9atv4.csv")

print(personas)