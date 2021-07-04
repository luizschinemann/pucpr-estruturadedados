from node import Node
# sequencial = []


class LinkedList:
    def __init__(self):
        self.head = None
        self.file = None
        self.frequency = None
        self._size = 0

    def append(self, file, frequency):
        if self.head:
            # inserção quando a lista ja possui elementos
            pointer = self.head
            file = self.file
            frequency = self.frequency
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(file, frequency)
        else:
            # primeira inserção
            self.head = Node(file, frequency)
        self._size = self._size + 1

    """RETORNA O TAMANHO DA LISTA"""
    def __len__(self):
        return self._size

    def get(self, index):
        pass

    def set(self, index, file, frequency):
        pass

    def __getitem__(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("List index out of range")

        if pointer:
            return pointer.file + " => (" + str(pointer.frequency) +")"
        else:
            raise IndexError("List index out of range")

    def __setitem__(self, index, file, frequency):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("List index out of range")

        if pointer:
            pointer.data = file
            pointer.frequency = frequency
        else:
            raise IndexError("List index out of range")


