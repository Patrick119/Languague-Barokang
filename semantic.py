import parser
import numpy as np
from collections import deque  

print ("\n                             ANALIZADOR SEMANTICO\n")

print ("\nTABLA DE SIMBOLOS:\n")

class simbolo:
    def __init__(self, t, lex, tp, pos, lin, scope):
        self.token = t
        self.lexema = lex
        self.tipo = tp
        self.posicion = pos
        self.linea = lin
        self.scope = scope

class tipos:
    def __init__(self, t, lex, tp, pos, lin,atributo, scope):
        self.token = t
        self.lexema = lex
        self.tipo = tp
        self.posicion = pos
        self.linea = lin
        self.scope = scope
        self.atributo = atributo

n = 0
es_yoyo = False
tabla_de_simbolos = []
tabla_de_atributos = []
funcion_actual = None
funcion_actual_aux = None

def insertar_parametros(arbol):
    if arbol.elemento == "PARAMETERS":
        tabla_de_simbolos.append(
            simbolo(arbol.hijos[1].token, arbol.hijos[1].token.value, "variable", arbol.hijos[1].token.lexpos,
                    arbol.hijos[1].token.lineno, funcion_actual))
    elif arbol.elemento == "FUNCIONSTRUCTURE":
        tabla_de_simbolos.append(
            simbolo(arbol.hijos[1].token, arbol.hijos[1].token.value, "sv", arbol.hijos[1].token.lexpos,
                    arbol.hijos[1].token.lineno, funcion_actual))
    elif arbol.elemento=="DEFINITION_PARAMETERS" and arbol.hijos[0].elemento!="e":
        tabla_de_simbolos.append(
            simbolo(arbol.hijos[2].token, arbol.hijos[2].token.value, "variable", arbol.hijos[2].token.lexpos,
                    arbol.hijos[2].token.lineno, funcion_actual))
    elif arbol.elemento=="DECLARACION" and  arbol.hijos[0].elemento!="TIPODEDATO":
        tabla_de_simbolos.append(
            simbolo(arbol.hijos[0].token, arbol.hijos[0].token.value, "ret_asi", arbol.hijos[0].token.lexpos,
                    arbol.hijos[0].token.lineno, funcion_actual))
    elif arbol.elemento=="DECLARACION" and  arbol.hijos[0].elemento=="TIPODEDATO":
        tabla_de_simbolos.append(
            simbolo(arbol.hijos[1].token, arbol.hijos[1].token.value, "variable", arbol.hijos[1].token.lexpos,
                    arbol.hijos[1].token.lineno, funcion_actual))
    
    for x in arbol.hijos:
        insertar_parametros(x)

def repetido(r):
    for i in reversed(r):
        if i.tipo=="ret_asi":
            for j in reversed(tabla_de_simbolos):
                if i.tipo == "variable" and i.lexema==j.lexema:
                    return True
def comp():
    arr=[]
    for x in reversed(tabla_de_simbolos):
        if x.tipo == "ret_asi":
            arr.append(x)
    parser.ver_error(1)
                        
def comprobar_existencia_llamada():

    for x in reversed(tabla_de_simbolos):
        if x.tipo == "ret_asi":
            for y in reversed(tabla_de_simbolos):
                if y.tipo=="variable" and y.lexema==x.lexema:
                    print("correcto")

def insertar_tipo(arbol):
    
    if arbol.elemento == "PARAMETERS":
        tabla_de_atributos.append(
            tipos(arbol.hijos[1].token, arbol.hijos[1].token.value, "variable", arbol.hijos[1].token.lexpos,
                    arbol.hijos[1].token.lineno,arbol.hijos[0].hijos[0].token.value ,funcion_actual))
    elif arbol.elemento=="DEFINITION_PARAMETERS" and arbol.hijos[0].elemento!="e":
        tabla_de_atributos.append(
            tipos(arbol.hijos[2].token, arbol.hijos[2].token.value, "variable", arbol.hijos[2].token.lexpos,
                    arbol.hijos[2].token.lineno,arbol.hijos[1].hijos[0].token.value ,funcion_actual))
    elif arbol.elemento=="DECLARACION" and  arbol.hijos[0].elemento!="TIPODEDATO" and parser.treeGenerator.ejecutarAnchoPrimero(parser.arbolito)!=1:
        tabla_de_atributos.append(
            tipos(arbol.hijos[0].token, arbol.hijos[0].token.value, "ret_asi", arbol.hijos[0].token.lexpos,
                    arbol.hijos[0].token.lineno,"asignacion/retorno" ,funcion_actual))
    elif arbol.elemento=="DECLARACION" and  arbol.hijos[0].elemento=="TIPODEDATO":
        tabla_de_atributos.append(
            tipos(arbol.hijos[1].token, arbol.hijos[1].token.value, "variable", arbol.hijos[1].token.lexpos,
                    arbol.hijos[1].token.lineno,arbol.hijos[0].hijos[0].token.value,funcion_actual))
    elif arbol.elemento=="ASIGNACION2" and arbol.hijos[0].elemento=="igualdad":
        tabla_de_atributos.append(
            tipos(arbol.hijos[1].hijos[0].hijos[0].hijos[0].token, arbol.hijos[1].hijos[0].hijos[0].hijos[0].token.value, "asigna_variables", arbol.hijos[1].hijos[0].hijos[0].hijos[0].token.lexpos,
                    arbol.hijos[1].hijos[0].hijos[0].hijos[0].token.lineno,"asignacion",funcion_actual))
        
    for x in arbol.hijos:
        insertar_tipo(x)
def comprobar_asignacion():
    for x in reversed(tabla_de_atributos):
        if x.tipo == "asignacion/retorno":
            for y in reversed(tabla_de_atributos):
                if y.tipo=="variable" and y.lexema==x.lexema:
                    print("correcto")

insertar_parametros(parser.arbolito)
for i in range(len(tabla_de_simbolos)):    
   print(tabla_de_simbolos[i].token,tabla_de_simbolos[i].tipo)
comprobar_existencia_llamada()
#comp()
insertar_tipo(parser.arbolito)
for i in range(len(tabla_de_atributos)):    
   print(tabla_de_atributos[i].token,tabla_de_atributos[i].atributo)

comprobar_asignacion()
marca=False
def chek_val():
   for i in range(len(tabla_de_atributos)):
       if tabla_de_atributos[i].atributo=="asignacion":
           var=tabla_de_atributos[i-1].lexema
           for j in range(len(tabla_de_atributos)):
               if var==tabla_de_atributos[j].lexema and tabla_de_atributos[j].atributo!="asignacion retorno":
                   if tabla_de_atributos[i].token=="num" and tabla_de_atributos[j].atributo=="op":
                       print("accion correcta")
                       marca=True
                   if tabla_de_atributos[i].token=="ch" and tabla_de_atributos[j].atributo=="ch":
                       print("accion correcta")
                       marca=True
                   if tabla_de_atributos[i].token=="dec" and tabla_de_atributos[j].atributo=="dec":
                       print("accion correcta")
                       marca=True
                   else:
                       print("\n\n          ERROR SEMANTICO ENCONTRADO, INCORRECTA DECLARACION DE TIPOS\n")
contenedor_asig=[]
contenedor_mostar=[]

def conte_valores(arbol):

    if arbol.elemento=="COUT2":
        contenedor_mostar.append(arbol.hijos[2].hijos[0].token.value)

    for x in arbol.hijos:
        conte_valores(x)                 

if(marca!=True):
    chek_val()
    
def almacenar(x):
  temp = type(x)is int
  return temp

for i in range(len(tabla_de_atributos)):
    if tabla_de_atributos[i].atributo=="asignacion/retorno" and  tabla_de_atributos[i+1].atributo=="asignacion":
        pair=(tabla_de_atributos[i].lexema,tabla_de_atributos[i+1].lexema)
        contenedor_asig.append(pair)

conte_valores(parser.arbolito)

