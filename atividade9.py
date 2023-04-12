#Crie uma função que aceite uma lista e um item, e retorne True caso o item pertença à lista, e False caso não pertença.


def include(arr,item):
    result = False
    for a in arr:
        if a == item:
            result = True
    return result