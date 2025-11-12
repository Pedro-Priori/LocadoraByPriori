import os 

carros = [
    ("Chevrolet Tracker", 120),
    ("Fiat Strada", 109),
    ("Volkswagen Polo", 92),
    ("Chevrolet Onix", 94),
    ("Fiat Argo", 86),
    ("Hyundai HB20", 93),
    ("Fiat Mobi", 75),
    ("Renault Kwid", 73),
    ("Volkswagen T-Cross", 119),
    ("Hyundai Creta", 145),
    ("Jeep Renegade", 121),
    ("Chevrolet Onix Plus", 104),
    ("Fiat Toro", 153),
    ("Jeep Compass", 181),
    ("Volkswagen Nivus", 122)
]
alugados = []

print("===========================")
print("Bem Vindo a nossa Locadora")
print("===========================")


def mostrar_lista_de_carros(lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        print("[{}] {} - R$ {} /dia".format(i , car[0], car[1]))



mostrar_lista_de_carros(carros)