#Sua função vai receber uma string nos parâmetros e retornar de acordo com a tabela abaixo:

#Chave	                Valor
#"Jabroni"	            "Patron Tequila"
#"School Counselor"	    "Anything with Alcohol"
#"Programmer"	        "Hipster Craft Beer" 
#"Bike Gang Member"	    "Moonshine"
#"Politican"	        "Your tax dollars"
#"Rapper"	            "Cristal"
#qualquer outra coisa	"Beer"
 

#Nota: qualquer outra coisa é um caso base: se a string passada por parâmetro não existir na nossa tabela, retornar 'Beer'.

#Atente-se em cobrir os casos em que certas palavras não vêm com a formatação correta. 
#Exemplo: o parâmetro "pOLitiCIaN" ainda deve retornar "Your tax dollars".


def get_drink_by_profession(param):
    drinks = {
        "jabroni": "Patron Tequila",
        "school counselor": "Anything with Alcohol",
        "programmer": "Hipster Craft Beer",
        "bike gang member": "Moonshine",
        "politician": "Your tax dollars",
        "rapper": "Cristal"
    }
    param = param.lower()
    for key, value in drinks.items():
        if key == param:
            return value
    return "Beer"