from faker import Faker
import pandas as pd

#inicializando biblioteca
faker = Faker('pt_BR')

#criando persona - parte um
data = {"Nome": faker.name(), "Cidade": faker.city()}

print(data)