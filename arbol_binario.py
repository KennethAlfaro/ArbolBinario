import queue
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

class ArbolBinario:

    def __init__(self):
        self.root = None

    def crear_desde_archivo(self,nombre):
        try:
            handle = open(nombre, 'r')
        except IOError:
            return None
        self.root = self._crear_desde_archivo(handle)
        handle.close()
        if self.root is None:
            return None
        return 1

    def _crear_desde_archivo(self, handle):
        c = handle.read(1)

        if c == '$':
            return None
        tmp = Nodo(c)
        tmp.left = self._crear_desde_archivo(handle)
        tmp.right = self._crear_desde_archivo(handle)

        return tmp

    def pre_orden(self):
        self._pre_orden(self.root)

    def _pre_orden(self, actual):
        if actual is None:
            return None

        print(actual.valor, end=' ')
        self._pre_orden(actual.left)
        self._pre_orden(actual.right)

    def orden(self):
        self._orden(self.root)

    def _orden(self, actual):
        if actual is None:
            return None


        self._pre_orden(actual.left)
        print(actual.valor, end=' ')
        self._pre_orden(actual.right)

    def pos_orden(self):
        self._pos_orden(self.root)

    def _pos_orden(self, actual):
        if actual is None:
            return None

        self._pre_orden(actual.left)
        self._pre_orden(actual.right)
        print(actual.valor, end=' ')

    def recorrido_en_orden_por_nivel(self):
        if self.root is None:
            return
        cola = queue.Queue()
        cola.put(self.root)

        while not cola.empty():
            tmp = cola.get()
            print(tmp.valor, end=' ')
            if tmp.left is not None:
                cola.put(tmp.left)
            if tmp.right is not None:
                cola.put(tmp. right)

    def nodo_mas_profundo(self):
        if self.root is None:
            return
        cola = queue.Queue()
        cola.put(self.root)

        while not cola.empty():
            tmp = cola.get()
            if tmp.left is not None:
                cola.put(tmp.left)
            if tmp.right is not None:
                cola.put(tmp. right)
        return tmp

    def insertar(self, key):
        if self.root is None:
            self.root = Nodo(key)
            return
        cola = queue.Queue()
        cola.put(self.root)

        while not cola.empty():
            tmp = cola.get()
            print(tmp.valor, end=' ')
            if tmp.left is not None:
                cola.put(tmp.left)
            else:
                tmp.left = Nodo(key)
                return
            if tmp.right is not None:
                cola.put(tmp.right)
            else:
                tmp.left = Nodo(key)
                return

    def _buscar_iterativo(self, key):
        if self.root is None:
            return
        cola = queue.Queue()
        cola.put(self.root)

        while not cola.empty():
            tmp = cola.get()
            if tmp.valor == key:
                return tmp
            if tmp.left is not None:
                cola.put(tmp.left)

            if tmp.right is not None:
                cola.put(tmp.right)
        return None

    def buscar_iterativo(self, key):
        if self._buscar_iterativo(key) is None:
            return False
        return True
    def buscar_recursivo(self, key):
        tmp = self._buscar_recursivamente(key, self.root)
        if tmp is not None:
            return True
        return False

    def _buscar_recursivamente(self, key, root):
            if root is None:
                return None
            elif root.valor == key:
                return root


            tmp = self._buscar_recursivamente(key, root.left)
            if tmp is not None:
                return tmp

            return self._buscar_recursivamente(key, root.right)

