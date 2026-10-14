#PIDE AL USUARIO SU AÑO DE NACIMIENTO Y CALCULA CUANTOS AÑOS CUMPLIRA EN EL AÑO 2030 E IMPRIME EL RESULTADO
while True:
    try:
        nac = int(input("ingrese su fecha de nacimiento: \n"))
        future = 2030 - nac

        if 2030 < nac:
            print("vienes del futuro o que hijo")
            
        elif nac<=0:
            print("mamut")
            
        else:
            print(f"tu edad para el 2030 es de {future} años")
            break
    except:
        print("introduce un caracter entero por favor")
