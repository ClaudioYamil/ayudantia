#ESCRIBE UN PROGRAMA QUE PIDA AL USUARIO SU NOMBRE Y SU EDAD POR TECLADO. LUEGO DEBE IMPRIMIR UN MENSAJE DE SALUDO

nombre = ""
edad = None

while True:
    nombre = str(input("introduce tu nombre: \n")).strip()
    if nombre:
        break
    
    else:
        print("aun no has introducido tu nombre \nintentelo de nuevo \n")
        
while True:
    try:
        
        edad = int(input("introduce tu edad: \n"))
        if edad <= 0 or edad >120:
            print("dato invalido\n")
            
        else:
            
            break
    except ValueError:
        print ("valor invalido\n")
        
print (f"que tal {nombre} de {edad}")
        
        
    
        
    