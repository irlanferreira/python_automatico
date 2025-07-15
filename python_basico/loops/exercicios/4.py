pizza = 0
hamburguer = 0
while True:
    voto = int(input("Vote: \n1.Pizza\n2.Hambúrguer\n3.Sair\n"))
    match voto:
        case 1:
            pizza += 1
        case 2:
            hamburguer += 2
        case 3:
            break
        case _:
            print(f"Opção inválida!")

print(f"RESULTADOS\nPizza:{pizza}\nHambúrguer: {hamburguer}")