import csv

def carregar_arquivo(arquivo):
    return open(arquivo, newline='')

def obter_dados(arquivo):
    leitor = csv.DictReader(arquivo, delimiter=',')
    return leitor

arquivo_csv = carregar_arquivo('CarRentalData.csv')
dados = obter_dados(arquivo_csv)

teslas_alugados = 0

for carro in dados:
    carro = dict(carro)
    if carro['vehicle.make'] == 'Tesla':
        teslas_alugados = teslas_alugados + 1

print(teslas_alugados)