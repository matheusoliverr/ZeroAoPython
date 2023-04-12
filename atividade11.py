#Parâmetros - Sua função receberá um dicionário no parâmetro.
#Procedimento - Criar uma lista;
#Se a quantidade e o valor for menor que 7, deve criar um dicionário com a chave sendo o nome da fruta 
#e o valor sendo a quantidade dela e adicionar esse dicionário a lista criada;
#Retorno - Deve retornar uma lista de dicionários contendo o nome da fruta como chave e a quantidade comprada como valor.


def comprar_frutas(frutas):
    list_frutas = []
    
    for fruta, info in frutas.items():
        if info["quantidade"] < 7 and info["preco"] < 7:
            list_frutas.append({fruta : info["quantidade"]})
    return list_frutas
        
lista_de_frutas = {
    "melancia": {"quantidade": 4, "preco": 10},
    "pera": {"quantidade": 2, "preco": 3},
    "uva": {"quantidade": 8, "preco": 8},
    "ameixa": {"quantidade": 5, "preco": 2},
    "abacaxi": {"quantidade": 15, "preco": 4},
    "banana": {"quantidade": 6, "preco": 4}
}

comprar_frutas(lista_de_frutas)