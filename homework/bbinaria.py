def bbinaria(ordenados, buscado):
    n = len(ordenados)
    print("Tengo", n, ordenados, "y busco por", buscado)
    if n == 0: # no hay nada
        return False
    pos = n // 2 # div. entera
    pivote = ordenados[pos]
    if pivote == buscado:
        return True # encontrado
    elif buscado < pivote: # viene antes del pivote
        return bbinaria(ordenados[: pos], buscado)
    else: # pivote < buscado # viene desp. del pivote
        return bbinaria(ordenados[pos + 1 :], buscado)

# print(bbinaria([x for x in range(4, 30, 5)], 15))

desde = 4
hasta = 63
paso = 3
ubicar = 12
ordenados = [97, 99, 10, 44, 15, 80, 56, 91, 60, 9]

print(bbinaria([x for x in range(desde, hasta + 1, paso)], ubicar))
