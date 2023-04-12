#Ache a média de uma lista de números.
#Caso seja passada uma lista de tamanho 0 ou vazia ( [] ), o retorno deverá ser 0 ( zero )


def find_average(nums):
    return float(sum(nums)) / len(nums) if len(nums) !=0 else 0