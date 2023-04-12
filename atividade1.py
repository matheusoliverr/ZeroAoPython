#Sua função irá receber a idade (integer) e deve retornar a bebida de acordo com a idade:
#Se a idade for menor que 14 deve retornar 'drink toddy';
#Se a idade for menor que 18 deve retornar 'drink coke';
#Se a idade for menor que 21 deve retornar 'drink beer';
#Se a idade for maior ou igual a 21 deve retornar 'drink whisky';


def people_with_age_drink(age):
    if age > 20: return 'drink whisky'
    if age > 17: return 'drink beer'
    if age > 13: return 'drink coke'
    return 'drink toddy'