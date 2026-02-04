veiculos= input("Ingrese el veiculo: ")
match veiculos:
    case "moto":
        print("puede pasar")
    case "auto":
        print("puede pasar")
    case "camion":
        print("puede pasar")
    case _:
        print("Acceso denegado")
hora= float(input("Ingrese le hora: "))
if hora>6 and hora<9 or hora>17 and hora<20:
    print("Se le aplicara un cargo extra")
else:
    print("No se le aplicara ningun cargo extra")
