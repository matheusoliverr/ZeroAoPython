#Dado uma lista de inteiros, sua solução deverá retornar o menor número da lista. 
#Você pode assumir, para o proposito dessa prática, que nunca passaremos uma lista vazia para a sua função.


def find_smallest_int(arr):
    arr.sort()
    return arr[0]