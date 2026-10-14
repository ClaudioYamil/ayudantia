#CREA UN PROGRAMA QUE PIDA DOS NUMEROS ENTEROS AL USUARIO. 
#EL PRINT DEBE MOSTRAR: LA SUMA DE AMBOS, LA MULTIPLICACION, EL RESIDUO DE LA DIVISON
print("====== calculadora =======")
while True:
    try:

        nu = int(input("ingrese su primer valor: \n"))
        nu2 = int(input("ingrese el segundo valor \n"))
        print(f"suma: {nu + nu2}\nresta: {nu * nu2}\nresiduo: {nu % nu2}")
        break
    except:
        print("introdujo caracteres no validos para la operacion\nvuelva a intentarlo\n")