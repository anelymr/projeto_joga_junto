"""
---------------Criando um ambiente virtual
python -m venv pvenv
pvenv\Scripts\activate

---------------intalando pacotes
pip install nomedopacote

---------------para exibir lista de pacotes instalados
pip freeze > requirements.txt

---------------Exemplo do MATHEUS
import requests

response = requests.get('https://viacep.com.br/ws/13142342/json/')
data = response.json()

print(data)
"""
#---------------Atividade - Crie um dicionario com nome e cep
import requests

squad_um = {
            'Giovana': '03817070',
            'Mylena': '13142342',
            'Laiane': '40285001'
        }

for nome, cep in squad_um.items():
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    
    data = response.json()
    cidade = data['localidade']
    print(f'{nome} mora em {cidade}')