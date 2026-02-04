veiculos= input("Ingrese el veiculo: ")
hora= float(input("Ingrese le hora: "))
telepass= input("Posee telepass? ")
moto=5
auto=10
camion=20
match veiculos:
    case "moto":
        if hora>6 and hora<9 or hora>17 and hora<20:
            moto+=20
        if telepass == "si":
            moto-=2
        print(f"Se autoriza el paso con un valor de: {moto}")    
    case "auto":
        if hora>6 and hora<9 or hora>17 and hora<20:
            print("Se le aplicara un cargo extra")
        else:
            print("No se le aplicara ningun cargo extra")
            print("puede pasar")
    case "camion":
        if hora>6 and hora<9 or hora>17 and hora<20:
            print("Se le aplicara un cargo extra")
        else:
            print("No se le aplicara ningun cargo extra")
            print("puede pasar")
    case _:
        print("Acceso denegado")
