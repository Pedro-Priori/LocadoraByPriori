import os 

cars = [
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


def mostrar_lista_de_cars(list_cars):
        for i, car in enumerate(list_cars):
            print("[{}] {} - R$ {} /dia".format(i , car[0], car[1]))



mostrar_lista_de_cars(cars)


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
        op = int(input())
        os.system("cls")
        if op == 1:
            print("==============================")
            mostrar_lista_de_cars(cars)
            print("==============================")
        
        elif op == 2:
            print("==============================")
            mostrar_lista_de_cars(cars)
            print("==============================")
            print("Escolha um Carro")
            cod_car = int(input())
            print("Por quantos dias você deseja alugar este carro?")
            dias = int(input())
            os.system("cls")

            print("Você escolheu {} por {} dias".format(cars[cod_car][0],dias))
            print("O alugel Totalizaria R$ {}. Deseja Alugar ?".format(dias * cars[cod_car][1]))

            print("0 - Sim | 1 - Não ")
            conf = int(input())
            if conf == 0:
                print("Parabens voce alugou o {} por {} dias".format(cars[cod_car][0],dias))
                alugados.append(cars.pop(cod_car))
        elif op == 3:
            if len(alugados) == 0:
                print("Sem carros para devolver")
            else:
                print("Aqui a lista de carros alugados. Qual que você ira devolver? ")
                mostrar_lista_de_cars(alugados)
                print("Escolha o codigo do carro que você deseja devolver : ")
                cod = int(input())
                
                print("Obrigado por devolver o carro {} ".format(alugados[cod][0]))
                cars.append(alugados.pop(cod))
                        

        print("==============================")
        print("Deseja continua ?")
        print(" 0 - Continuar | 1 - Sair")
        if float(input()) == 1 : 
          break