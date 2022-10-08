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
