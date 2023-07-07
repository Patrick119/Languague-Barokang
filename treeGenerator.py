from collections import deque

class Arbol:
    def __init__(self, elemento, sid, token=None):
        self.sid = sid
        self.elemento = elemento
        self.hijos = []
        self.token = token
    def ingresar_elemento(self,arbol,element,padre,i,tok=None):
        subarbol = buscarSubarbol(arbol, padre)
        subarbol.hijos.append(Arbol(element,i,tok))
def buscarSubarbol(arbol, e):
    cola = deque()
    cola.append(arbol)

    while len(cola) != 0:
        subarbol = cola.popleft()

        if subarbol.sid == e:
            return subarbol

        cola.extend(subarbol.hijos)

    return None
  
def profundidad(arbol):
    if len(arbol.hijos) == 0: 
        return 1
    return 1 + max(map(profundidad, arbol.hijos)) 

def grado(arbol):
    return max(map(grado, arbol.hijos) + [len(arbol.hijos)])

def ejecutarProfundidadPrimero(arbol):
    print(arbol.elemento)
    for hijo in arbol.hijos:
        ejecutarProfundidadPrimero(hijo)
        
def recorrido_arbol(arbol, pila):
    if arbol.elemento == arbol.elemento.lower() and arbol.elemento != "e":
        arbol.token = pila.pop(0)
    for subarbol in arbol.hijos:
        recorrido_arbol(subarbol, pila)
        
def ejecutarAnchoPrimero(arbol):
    cola = deque()
    cola.append(arbol)
    while len(cola) != 0:
        nodo = cola.popleft()
        print(nodo.elemento)
        for subarbol in nodo.hijos:
            cola.append(subarbol)


def ret_elec(element):
    if element == element.lower():
        return element
