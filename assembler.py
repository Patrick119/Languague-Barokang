from semantic import *

def generar_suma(f, resultado, operando1, operando2):
    f.write("add $" + resultado + ", $" + operando1 + ", $" + operando2 + "\n")

def generar_resta(f, resultado, operando1, operando2):
    f.write("sub $" + resultado + ", $" + operando1 + ", $" + operando2 + "\n")

def generar_multiplicacion(f, resultado, operando1, operando2):
    f.write("mul $" + resultado + ", $" + operando1 + ", $" + operando2 + "\n")

def generar_operaciones(f, operaciones):
    for operacion in operaciones:
        tipo_operacion = operacion[0]
        resultado = operacion[1]
        operando1 = operacion[2]
        operando2 = operacion[3]

        if tipo_operacion == "suma":
            generar_suma(f, resultado, operando1, operando2)
        elif tipo_operacion == "resta":
            generar_resta(f, resultado, operando1, operando2)
        elif tipo_operacion == "multiplicacion":
            generar_multiplicacion(f, resultado, operando1, operando2)

def generar_sumas_anidadas(f, sumas_anidadas):
    for suma in sumas_anidadas:
        generar_operaciones(f, suma)

def generar_codigo_ensamblador():
    f = open("ensambladorPro.s", "w")
    f.write(".data\n")
    if len(contenedor_mostar) > 0:
        for i in range(len(contenedor_mostar)):
            f.write("out_string" + str(i) + ": .asciiz " + '"' + str(contenedor_mostar[i]) + '"\n')

    f.write(".text\n")
    f.write(".globl main\n")
    f.write("main:\n")
    if len(contenedor_asig) > 0:
        for i in range(len(contenedor_asig)):
            f.write("li $" + str(i + 1) + ", " + str(int(contenedor_asig[i][1])) + "\n")

    if "contenedor_sumas" in globals() and len(contenedor_sumas) > 0:
        generar_sumas_anidadas(f, contenedor_sumas)

    if "contenedor_condicionales" in globals() and len(contenedor_condicionales) > 0:
        for condicional in contenedor_condicionales:
            operando1 = condicional[0]
            operando2 = condicional[1]
            etiqueta_verdadero = condicional[2]
            etiqueta_falso = condicional[3]
            f.write("beq $" + operando1 + ", $" + operando2 + ", " + etiqueta_verdadero + "\n")
            f.write("j " + etiqueta_falso + "\n")
            f.write(etiqueta_verdadero + ":\n")
            # Instrucciones si la condición es verdadera
            f.write(etiqueta_falso + ":\n")

    if "contenedor_funciones" in globals() and len(contenedor_funciones) > 0:
        for funcion in contenedor_funciones:
            nombre_funcion = funcion[0]
            f.write(nombre_funcion + ":\n")
            # Código de la función
            f.write("jr $ra\n")

    f.close()

    f = open("ensambladorPro.s")
    ensamblador_producido = f.read()
    f.close()

generar_codigo_ensamblador()
