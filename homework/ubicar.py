valores = [97, 99, 10, 44, 15, 80, 56, 91, 60, 9]
interes = 38

from arbol import Arbol
a = Arbol()

for valor in valores:
    a.agrega(valor)

print(a)

def ubicar(nodo, buscado):
    print("Estamos en", nodo.contenido)
    if nodo.contenido == buscado:
        return True
    if buscado < nodo.contenido and nodo.izquierdo is not None:
        return ubicar(nodo.izquierdo, buscado)
    if buscado > nodo.contenido and nodo.derecho is not None:
        return ubicar(nodo.derecho, buscado)
    return False
 
ubicar(a.raiz, interes)
