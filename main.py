import arbol_binario

if __name__ == '__main__':
    arbolito = arbol_binario.ArbolBinario()
    arbolito.crear_desde_archivo('arbolchar.txt')
    arbolito.pre_orden()


