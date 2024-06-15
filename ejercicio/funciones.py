CARGOS   = ["ceo", "desarollador","analista"]

def registrarTrabajador(trabajadores):
        nombre = input("ingrese nombre y apellido del trabajador ")
        cargo = input ("ingrese el cargo del trabajador (ceo/Desarollador/Analista de daros):  ").lower()
        print(" a sido registrado de manera exitosa en nuestra empresas ")
        while cargo not in CARGOS:
                print("Cargo no existe, intente nuevamente ")
                cargo = input ("ingrese el cargo del trabajador (ceo/Desarollador/Analista de daros):  ").lower()
                print(" a sido registrado de manera exitosa en nuestra empresas ")
        sueldoBruto = int(input("ingrese el sueldo Bruto del trabajador "))

        descSalud = sueldoBruto * 0.07
        descAfp = sueldoBruto * 0.12
        liquidoPagar = sueldoBruto - descAfp - descSalud

        trabajadores.append({
                "Nombre" : nombre,
                "Cargo" : cargo,
                "Sueldobruto" : sueldoBruto,
                "DescSalud" : descSalud,
                "DescAfp" : descAfp,
                "LiquidoPagar" : liquidoPagar
        })


def listarTrabajadores(trabajadores):
        print("lista de trabajadores ")
        for trabajador in trabajadores:
                print(trabajador)
            #print(trabajador["nombre"]) si quisiera mostrar los nombres de los trabajadores
def imprimirPlantillas(trabajadores):
        cargoSeleccionado = input("ingrese cargo para imprimir planilla o bien presione enter para seleccionar todos:  ").lower()
        if cargoSeleccionado == "":
                trabajadoresAImprimir = trabajadores
                nombreArchivo = "planillaTodos.txt"
        elif cargoSeleccionado in CARGOS:
                trabajadoresAImprimir = []
                for trabajador in trabajadores:
                        if trabajador["Cargo"] == cargoSeleccionado:
                                trabajadoresAImprimir.append(trabajador)
                nombreArchivo =f"planilla_{cargoSeleccionado}.txt" 
        else:
                print("cargo no valido")
                return                                                               
        
        with open(nombreArchivo,"w") as archivo:
                for trabajador in trabajadoresAImprimir:
                       archivo.write(f"Nombre y Apellido: {trabajador["Nombre"]}\n")
                       archivo.write(f"Cargo: {trabajador["Cargo"]}\n") 
                       archivo.write(f"Sueldo Bruto: {trabajador["Sueldobruto"]}\n") 
                       archivo.write(f"Descuento salud: {trabajador["DescSalud"]}\n") 
                       archivo.write(f"Descuento Afp: {trabajador["DescAfp"]}\n") 
                       archivo.write(f"Liquido a pagar: {trabajador["LiquidoPagar"]}\n\n")  