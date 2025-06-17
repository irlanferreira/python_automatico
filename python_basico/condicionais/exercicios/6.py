opcao = int(input("Escolha uma opção\n1. Pizza\n2. Sushi\n3. Salada"))
match opcao:
    case 1:
        print("Você escolheu pizza!")
    case 2:
        print("Você escolheu sushi!")
    case 3:
        print("Você escolheu salada!")
    case _:
        print("Opção inválida.")