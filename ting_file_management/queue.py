class Queue:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if (self.isEmpty()):
            return None
        return self._data.pop(0)

    def search(self, index):
        if (len(self._data) <= index or index < 0):
            raise IndexError
        return self._data[index]

    def isEmpty(self):
        return not self._data
