import lexer
import xlrd
import pandas as pd
import numpy as np
import time
from graphviz import Digraph
import treeGenerator

dot = Digraph()

print ("\n                           ANALIZADOR SINTÁCTICO\n")

def columnas(val):
    if val=="start":
        return 1
    if val=="keyleft":
        return 2
    if val=="keyright":
        return 3
    if val=="sv":
        return 4
    if val=="id":
        return 5
    if val=="leftpar":
        return 6
    if val=="rightpar":
        return 7
    if val=="retorno":
        return 8
    if val=="coma":
        return 9
    if val=="exit":
        return 10
    if val=="ride":
        return 11
    if val=="lr":
        return 12
    if val=="mst":
        return 13
    if val=="mayorsimbol":
        return 14
    if val=="menorsimbol":
        return 15
    if val=="menorigual":
        return 16
    if val=="mayorigual":
        return 17
    if val=="diferencia":
        return 18
    if val=="simi":
        return 19
    if val=="si":
        return 20
    if val=="contra":
        return 21
    if val=="contrasi":
        return 22
    if val=="miss":
        return 23
    if val=="op":
        return 24
    if val=="dec":
        return 25
    if val=="val":
        return 26
    if val=="ch":
        return 27
    if val=="float":
        return 28
    if val=="igualdad":
        return 29
    if val=="num":
        return 30
    if val=="cc":
        return 31
    if val=="suma":
        return 32
    if val=="resta":
        return 33
    if val=="multiplicacion":
        return 34
    if val=="division":
        return 35
    if val=="$":
        return 36

def filas(stra):
    if stra=="START":
        return 1
    if stra=="FUNCION_INICIAL":
        return 2
    if stra=="FUNCIONSTRUCTURE":
        return 3
    if stra=="PARAMETERS":
        return 4
    if stra=="DEFINITION_PARAMETERS":
        return 5
    if stra=="CONTROLSTRUCTURE1":
        return 6
    if stra=="CONTROLSTRUCTURE2":
        return 7
    if stra=="LEER":
        return 8
    if stra=="CIN2":
        return 9
    if stra=="NA":
        return 10
    if stra=="NADA":
        return 11
    if stra=="LLA":
        return 12
    if stra=="LLB":
        return 13
    if stra=="COUT":
        return 14
    if stra=="COUT2":
        return 15
    if stra=="SYMBOLS":
        return 16
    if stra=="IFELSEWHILE":
        return 17
    if stra=="VALUES":
        return 18
    if stra=="DECLARACION":
        return 19
    if stra=="TIPODEDATO":
        return 20
    if stra=="ASIGNACION1":
        return 21
    if stra=="ASIGNACION2":
        return 22
    if stra=="E":
        return 23
    if stra=="R":
        return 24
    if stra=="SELECT0":
        return 25
    if stra=="SELECT":
        return 26
    if stra=="LOGICAL_OPERATORS":
        return 27
    else:
        return 0

df = pd.read_excel("tableofBarokang.xlsx", 'Hoja1',  header=None)
tablita_parse = df.values

pila = ["START","$"]
entrada = lexer.cadena2
entrada.append("$")
pila_tokens = lexer.cadena3

continuar=True
i=0
j=0
p=0
aux=[]
pendientes=[]
arbolito = treeGenerator.Arbol(pila[0],0)
dot.node(str(j), pila[0])
padres=[0,-1]

while continuar:
  if pila[0]=="$" and entrada[0]=="$":
    continuar=False
    print("                   ¡FELICIDADES TU CADENA A SIDO ACEPTADA!")
  elif pila[0] == entrada[0]:
    pila = pila[1:]
    entrada.pop(0)
  elif pila[0][0]==(pila[0][0]).lower() and entrada[0][0]==(entrada[0][0]).lower():
    continuar=False
    print("                   ¡ERROR SINTACTICO!, cadena rechazada")
    print("                             Corrige la cadena")
  else:
    if columnas(entrada[0])!=0:
      reemplazo = tablita_parse[filas(pila[0])][columnas(entrada[0])]
      p=int(padres[0])
    else:
      continuar=False
      print("                   ¡ERROR SINTACTICO!, cadena rechazada")
      print("                             Corrige la cadena")
      break
    if reemplazo == "e":
      j=j+1
      h=j
      dot.node(str(h), "e")
      dot.edge(str(p),str(h))
      arbolito.ingresar_elemento(arbolito,"e",p,h)
      pila=pila[1:]
      padres=padres[1:]
    else:
      reemplazo=str(reemplazo)
      array_aux=reemplazo.split()
      pila = np.concatenate((array_aux,pila[1:]),axis=0)
      hijos = len(array_aux)
      aux.clear()
      for e in range(hijos):
        j=j+1
        if array_aux[e][0]==array_aux[e][0].upper():
          aux.append(j)
          arbolito.ingresar_elemento(arbolito,array_aux[e],p,j)
        else:
          arbolito.ingresar_elemento(arbolito,array_aux[e],p,j)
        h=j
        dot.node(str(h), array_aux[e])
        dot.edge(str(p),str(h))
      padres = np.concatenate((aux,padres[1:]),axis=0)
  i=i+1
print ("\n\n                            (Generando Gráfico)\n")

frase = ""
for punto in range(7):
    frase = frase[:punto+1]
    puntos = "●"
    espacios = " " * ((2 - len(frase) - len(puntos)) // 2)
    print(f"{espacios}{puntos}".rjust(10 + len(espacios)), end='', flush=True)
    time.sleep(1)

print(frase)
dot.view()
treeGenerator.recorrido_arbol(arbolito,pila_tokens)
print ("\n                      -*-*-    Gráfico Generado    -*-*-\n")
print ("\n#################################################################################\n")
