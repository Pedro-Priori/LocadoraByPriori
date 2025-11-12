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


def mostrar_lista_de_carros(lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        print("[{}] {} - R$ {} /dia".format(i , car[0], car[1]))



mostrar_lista_de_carros(carros)


while True: 
    os.system("cls")

    print("==============================")
    print("Bem Vindo a Locadora ByPriori") 
    print("==============================")
    print("Qual seus interesses")
    print("==============================")
    print("1 Ver tabela de carros e preços")
    print("2 Alugar um carro")
    print("3 Devolver um carro")
    print("4 sair")

    op = int(input())

    os.system("cls")
    if op == 1:
        pass
    elif op == 2:
        pass 
    elif op == 3:
        pass 