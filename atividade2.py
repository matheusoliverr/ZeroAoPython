#Ele irá sobreviver? Um herói está a caminho do castelo para completar sua missão. 
#Entretanto, lhe foi dito que o castelo é protegido por alguns dragões muito poderosos! 
#Cada dragão necessita de duas munições para ser derrotado, e o nosso herói não faz ideia de quantas munições ele deve levar... 
#Assumindo que ele irá pegar um número específico de munições e partirá para a batalha contra um número específico de dragões, 
#ele irá sobreviver?

#Nota: Você receberá a quantidade de balas do herói e a quantidade de dragões do castelo.


def hero(bullets, dragons):
    if bullets/dragons >= 2:
        return True
    else:
        return False