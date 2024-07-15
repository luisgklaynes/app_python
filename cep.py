import requests as rq

#def consultar_cep(cep):
cep = "81130130"
url = f'https://viacep.com.br/ws/{cep}/json/'  
response = rq.get(url)
dados = response.json()

# print(dados)

#print(consultar_cep(81130040))

# import requests

# def consultar_cep(cep):
#     url = f'https://viacep.com.br/ws/{cep}/json/'
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         dados = response.json()
#         if 'erro' in dados:
#             return "CEP não encontrado."
#         return dados
#     else:
#         return f"Erro na consulta do CEP: {response.status_code}"

# # Exemplo de uso
# cep = "81130130"  # CEP de exemplo
# resultado = consultar_cep(cep)
# print(resultado)