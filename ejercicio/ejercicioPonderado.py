import funciones as fn

trabajadores = []

while True:
    print("""bienvenido al sistema de pago de sueldos
             ****************************************
             1. Registrar trabajador
             2. lista los trabajadores
             3. imprimir planilla de sueldos
             4. salir.
          """)
    
    opc = int(input(" ingrese una opcion de 1 a la  4 "))

    if opc == 1:
        fn.registrarTrabajador(trabajadores)
    elif opc == 2:
        fn.listarTrabajadores(trabajadores)
    elif opc == 3:
        fn.imprimirPlantillas(trabajadores)
    elif opc == 4:
        break
    else:
        print(" opc Opcion no valida, escoja una opcion dentro de los parametros entregados nuevamente ")            