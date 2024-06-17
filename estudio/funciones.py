

CARGOS =["ceo", "desarollador", "analista"]

def listarTrabajadores(trabajadores):
    print("lista de trabajadores ingresados")
    print("********************************")
    for trabajador in trabajadores:
        print(trabajador)


def  imprimirPlantilla(trabajadores):
    cargoSeleccionado = input(" ingresa el cargo del trabajador \n")
    if cargoSeleccionado == "":
        trabajadoresImprimidos = trabajadores
        nombreArchivo = "Plantillatodos.txt"
    elif cargoSeleccionado in CARGOS :
        trabajadoresImprimidos = []
        for trabajador in trabajadores:
            if trabajador["Cargo"] == cargoSeleccionado:
                trabajadoresImprimidos.append(trabajador)
        nombreArchivo =f"plantilla_{cargoSeleccionado}.txt"
    else:
        print("cargo no valido")
        return

    with open(nombreArchivo, "w") as archivo:
        for trabajador in trabajadoresImprimidos:
            archivo.write(f"Nombre y Apellido: {trabajador["Nombre"]}\n")
            archivo.write(f"Cargo: {trabajador["Cargo"]}\n") 
            archivo.write(f"Sueldo Bruto: {trabajador["sueldoBruto"]}\n") 
            archivo.write(f"Descuento salud: {trabajador["DescSalud"]}\n") 
            archivo.write(f"Descuento Afp: {trabajador["DescAfp"]}\n") 
            archivo.write(f"Descuento por Cesantia: {trabajador["DescCesantia"]}\n") 
            archivo.write(f"Liquido a pagar: {trabajador["LiquidoaPagar"]}\n\n")  


def registrarTrabajadores(trabajadores):
    nombre = input(" introdusca su nombre completo ") 
    cargo = input("introdusca su cargo en la empresa (ceo/desarollador/analista) ").lower()
    print ("a sido registrado de forma correcta ")
    while cargo not in CARGOS:
        print("cargo no existe intente nuevamente")
        cargo = input("introdusca su cargo en la empresa (ceo/desarollador/analista) ").lower()
        print ("a sido registrado de forma correcta ")
    sueldoBruto = int(input("ingrese su sueldo minimo en USD del trabajador "))
    desSalud = sueldoBruto *0.07
    descAfp = sueldoBruto * 0.12
    descCesantia = sueldoBruto * 0.03
    liquidoAPagar = sueldoBruto - descAfp - desSalud
    trabajadores.append({
        "Nombre" : nombre,
        "Cargo"  : cargo,
        "sueldoBruto": sueldoBruto,
        "DescAfp" : descAfp,
        "DescCesantia" : descCesantia,
        "DescSalud" : desSalud,
        "LiquidoaPagar" : liquidoAPagar
    })    
