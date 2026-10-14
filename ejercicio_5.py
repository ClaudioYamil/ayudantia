#PIDE LA NOTA FINAL DE UN ESTUDIANTE DE 0 A 100,
# SI EL PROMEDIO ES MENOR IGUAL A 50 MOSTRAR REPROBADO CON LA NOTA DE REPROBACION Y SI ES MAYOR IGUAL A 51
# MOSTRAR APROBADO CON LA NOTA DE APROBACION

def e():
    print("dato invalido\nvuelva a intentarlo\n")
    
while True:
    try:
        nota = int(input("ingrese la nota final del estudiante: \n"))
        if nota <= 0 or nota > 100:
            e()
        elif nota <= 50:
            print(f"la nota dada de {nota} esta reprobada")
            break
        else:
            print(f"el estudiante aprobo con {nota}")
            break
             
    except:
        e()