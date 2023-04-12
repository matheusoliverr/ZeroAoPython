#Dadas 2 strings, a e b, retorne uma string no formato menor+maior+menor, com a string menor por fora e a string maior por dentro.
#As strings passadas nunca serão de tamanho igual, mas elas podem ser vazias (length 0).


def solution(a, b):
    firstCount = ((" ".join(a)).count(" "))+1
    secondCount = ((" ".join(b)).count(" "))+1
    
    if firstCount > secondCount:
        result = b+a+b
    else:
        result = a+b+a
    return result