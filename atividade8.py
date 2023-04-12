#Nessa prática, vocês serão desafiados a criarem duas tuplas e juntar as duas em uma terceira tupla.


def joinTuple(a, b):
    my_tuple = ()
    for i in a:
        my_tuple += (i,)
    for i in b:
        my_tuple += (i,)
    return my_tuple
    
a = (1, 2, 3)
b=(4, 5, 6)

resultTuple = joinTuple(a, b)
print(resultTuple)