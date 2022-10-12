import arbol_binario

if __name__ == '__main__':
    arbolito = arbol_binario.ArbolBinario()
    arbolito.crear_desde_archivo('arbolchar.txt')
    arbolito.pre_orden()
    print('\n')
    tmp = arbolito.recorrido_en_orden_por_nivel()
    print(tmp)
    print('\n')
    tmp2 = arbolito.nodo_mas_profundo()
    print(tmp2.valor)
    arbolito.insertar('Z')
    print(arbolito.recorrido_en_orden_por_nivel())

    print(arbolito.buscar_iterativo('R'))
    print(arbolito.buscar_iterativo('J'))

    print('\n')

    print(arbolito.buscar_recursivo('R'))
    print(arbolito.buscar_recursivo('J'))