import os
encendido = "Y"
while not encendido == "N":
    print("\n\t\t\t\tCIRCUITO N7\n")
    print("\t\t x                 y     x                y")
    print("\t\t  °┌──────Rc─────┐°       °──R1───┬──R2──°")
    print("\t\t   |             |                |       ")
    print("\t\t   Rb            Ra               R3      ")
    print("\t\t   |             |                |       ")
    print("\t\t   └──────°──────┘                °       ")
    print("\t\t          z                       z       ") 
    while True:
        opcion = input("\nElija una opcion:\n\tA)DELTA-ESTRELLA\n\tB)ESTRELLA-DELTA\n\tC)Salir\n\t\tOpcion: ").upper()
        if opcion == "A":
            print("\n\t\tLas ecuaciones para transformar son:")
            print("\t\t x                 y")
            print("\t\t  °┌──────Rc─────┐° ")
            print("\t\t   |             |  ")
            print("\t\t   Rb            Ra ")
            print("\t\t   |             |  ")
            print("\t\t   └──────°──────┘  ")
            print("\t\t          z         ") 
            print("\tR1 = Rb*Rc/Ra+Rb+Rc")
            print("\tR2 = Ra*Rc/Ra+Rb+Rc")
            print("\tR3 = Ra*Rb/Ra+Rb+Rc")
            print("Ingrese Ra, Rb ,Rc separado por espacios:\n")
            Ra, Rb, Rc = map(int, input().split())
            R1 = round((Rb*Rc/(Ra+Rb+Rc)),2)
            R2 = round((Ra*Rc/(Ra+Rb+Rc)),2)
            R3 = round((Ra*Rb/(Ra+Rb+Rc)),2)
            print("Los valores son: ")
            print("\t\t x                y")
            print("\t\t  °──R1───┬──R2──°")
            print("\t\t          |       ")
            print("\t\t          R3      ")
            print("\t\t          |       ")
            print("\t\t          °       ")
            print("\t\t          z       ") 
   
            print("\nR1:",R1)
            print("\nR2:",R2)
            print("\nR3:",R3)
            os.system('pause')
            break
        if opcion == "B":
            print("\n\t\tLas ecuaciones para transformar son:")
            print("\t\t x                y")
            print("\t\t  °──R1───┬──R2──°")
            print("\t\t          |       ")
            print("\t\t          R3      ")
            print("\t\t          |       ")
            print("\t\t          °       ")
            print("\t\t          z       ") 
            print("\tRa = (R1*R2+R2*R3+R3*R1)/R1")
            print("\tRb = (R1*R2+R2*R3+R3*R1)/R2")
            print("\tRc = (R1*R2+R2*R3+R3*R1)/R3")
            print("Ingrese R1, R2 ,R3 separado por espacios:\n")
            R1, R2, R3 = map(int, input().split())
            Ra = round((R1*R2+R2*R3+R3*R1)/R1,2)
            Rb = round((R1*R2+R2*R3+R3*R1)/R2,2)
            Rc = round((R1*R2+R2*R3+R3*R1)/R3,2)
            print("Los valores son: ")
            print("\t\t x                 y")
            print("\t\t  °┌──────Rc─────┐° ")
            print("\t\t   |             |  ")
            print("\t\t   Rb            Ra ")
            print("\t\t   |             |  ")
            print("\t\t   └──────°──────┘  ")
            print("\t\t          z         ") 
   
            print("\nRa:",Ra)
            print("\nRb:",Rb)
            print("\nRc:",Rc)
            os.system('pause')
            break
        if opcion == "C":
            encendido = input("\nSi desea seguir en el programa digite 'Y' caso contrario 'N':   ").upper()
            print("\n\n\tGracias, hasta luego!!")
            break
        