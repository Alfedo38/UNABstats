class MaxHeapNBA:
    def __init__(self):
        self.heap = []

    def insertar(self, item, prioridad):
        # Guardamos la tupla (prioridad, item)
        self.heap.append((prioridad, item))
        self._flotar(len(self.heap) - 1)

    def extraer_maximo(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()[1]
        
        raiz = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._hundir(0)
        return raiz[1]

    def _flotar(self, index):
        padre = (index - 1) // 2
        while index > 0 and self.heap[index][0] > self.heap[padre][0]:
            self.heap[index], self.heap[padre] = self.heap[padre], self.heap[index]
            index = padre
            padre = (index - 1) // 2

    def _hundir(self, index):
        n = len(self.heap)
        while 2 * index + 1 < n:
            hijo_izq = 2 * index + 1
            hijo_der = 2 * index + 2
            mayor = hijo_izq

            if hijo_der < n and self.heap[hijo_der][0] > self.heap[hijo_izq][0]:
                mayor = hijo_der

            if self.heap[index][0] >= self.heap[mayor][0]:
                break

            self.heap[index], self.heap[mayor] = self.heap[mayor], self.heap[index]
            index = mayor

    def obtener_top_n(self, n):
        # Extrae los N elementos con mayor prioridad
        resultado = []
        # Hacemos una copia para no vaciar el heap original
        copia_heap = MaxHeapNBA()
        copia_heap.heap = self.heap.copy()
        
        for _ in range(min(n, len(self.heap))):
            resultado.append(copia_heap.extraer_maximo())
        return resultado