#PIDE UN NUMERO ENTERO AL USUARIO E INDICA MEDIANTE UN MENSAJE SI EL NUMERO INGRESADO EN PAR O IMPAR

while True:
    try:
        E = int(input("introduce un valor:\n"))
        Res = E%2
        if Res == 0:
            print(f"el numero {E} es par")
            
        else:
            print(f"el numero {E} es inpar")
            
        break 
    except ValueError:
        print(f"el valor que indico no es valido debido a que no es un numero entero\n vuelva a intentarlo\n")