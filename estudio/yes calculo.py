import funciones as fn 

trabajadores = [] 

while True:
    print(""" 
          1.- registrar trabajador (ceo's/desarollador/analista):  
          2.- listar todos los los trabajadores ingresados
          3.- imprimir plantilla de sueldos
          4.- salir
           """)
    
    opc = int( input("escoja una variable de opcion desde la 1 a la 4\n"))
    if opc == 1:
        fn.registrarTrabajadores(trabajadores)
    elif opc == 2:
        fn.listarTrabajadores(trabajadores)
    elif opc == 3:
        fn.imprimirPlantilla(trabajadores)
    elif opc == 4:
        print("saliendo de la aplicacion. sayonaraa")
        break
    else:
        print("variable introducida de manera incorrecta, vuele a intentar")            