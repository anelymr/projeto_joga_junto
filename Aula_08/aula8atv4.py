import requests

def define_frete(cep):
    url = (f'https://viacep.com.br/ws/{cep}/json/')
    response = requests.get(url)
    data = response.json()

    for uf in data.items():
        estado = data['uf']
        if estado in ('AM', 'RR', 'AP', 'PA', 'TO', 'RO', 'AC', 'MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA'):
            return "Cliente elegível para Frete grátis"

        return "Cliente não elegivel para frete grátis"

cep = int(input("Digite seu CEP: "))

resultado = define_frete(cep)
print(resultado)