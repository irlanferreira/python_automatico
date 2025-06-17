transporte = input("Digite um meio de transporte: ")
match transporte:
    case "carro":
        print("Veículo terrestre.")
    case "bicicleta":
        print("Veículo sustentável.")
    case "avião" | "helicóptero":
        print("Transporte aéreo")
    case _:
        print("Transporte desconhecido")