import queue
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
