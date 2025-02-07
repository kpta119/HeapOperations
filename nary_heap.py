from math import floor, ceil, log


class NaryHeap:
    def __init__(self, n, table=[]):
        self._table = table
        self._nodes = 0
        self._n = n
        self._build_heap()

    def get_table(self):
        return self._table

    def _heapify(self, i):
        largest = i
        for n in range(0, self._n):
            if (
                (self.get_child_of(n, i) < len(self._table)) and (
                    self._table[self.get_child_of(n, i)] > self._table[largest]
                )
            ):
                largest = self.get_child_of(n, i)
        if largest != i:
            self._swap(i, largest)
            self._heapify(largest)

    def _build_heap(self):
        n = len(self._table)
        for i in reversed(range(n//self._n+1)):
            self._heapify(i)

    def get_parent_of(self, x):
        return (x - 1) // self._n

    def get_child_of(self, x, i):
        return self._n * i + 1 + x

    def _go_upwords(self, i):
        while i > 0 and self._table[self.get_parent_of(i)] < self._table[i]:
            self._swap(self.get_parent_of(i), i) 
            i = self.get_parent_of(i)

    def push(self, i):
        self._table.extend([i])
        i_index = len(self._table) - 1
        self._go_upwords(i_index)

    def pop(self):
        last_index = len(self._table) - 1
        self._swap(last_index, 0)
        self._table.pop()
        self._heapify(0)

    def _swap(self, n, x):
        tmpr = self._table[n]
        self._table[n] = self._table[x]
        self._table[x] = tmpr

    def print(self):
        number_of_lines = ceil(
            log(len(self._table)*self._n-len(self._table)+1, self._n)
            )
        if self._n**number_of_lines > 150:
            width = 150
        else:
            width = self._n**number_of_lines
        last_row = -1
        for i, n in enumerate(self._table):
            n = str(n)
            if i:
                row = ceil(log((i+1)*self._n-(i+1)+1, self._n)) - 1
            else:
                print(n.center(self._n**(number_of_lines)), end="")
                continue
            if row != last_row:
                print()
            columns = self._n**row
            col_width = floor(self._n**(number_of_lines)/columns)
            print(n.center(col_width), end="")
            last_row = row




