def configPeaje():
    hora= float(input("Ingrese le hora: "))
    telepass= input("Posee telepass? ")

try:
    veiculos= input("Ingrese el veiculo: ")
    hora = 0
    telepass = ""
    moto=5
    auto=10
    camion=20
    match veiculos:
        
        case "moto":
            configPeaje()
            if hora>6 and hora<9 or hora>17 and hora<20:
                moto+=20
            if telepass == "si":
                moto-=2
            print(f"Se autoriza el paso con un valor de: {moto}")    
        case "auto":
            configPeaje()
            if hora>6 and hora<9 or hora>17 and hora<20:
                auto+=20
            if telepass == "si":
                auto-=2
            else:
                if telepass == "no":
                    print(f"Se autoriza el paso con un valor de: {auto}")    
        case "camion":
            configPeaje()
            if hora>6 and hora<9 or hora>17 and hora<20:
                camion+=20
            if telepass == "si":
                camion-=2
            print(f"Se autoriza el paso con un valor de: {camion}")    
        case _:
            print("Acceso denegado")

except ValueError:
    print("Ingrese el valor requerido")