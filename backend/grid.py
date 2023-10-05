#! usr/bin/python3

class HexagonalGrid:
    def __init__(self, size, default_factory = None):
        self._data = []
        self.size = size
        if default_factory is None:
            default_factory = int
        self.type = default_factory
        self._data.append(default_factory())
        for i in range(2, size+1):
            self._data.extend([default_factory() for j in range(6*i-6)])
        print(len(self._data))
        self._linelength = list(range(1, size))+[size, size-1]*size+list(range(size-2, 0, -1))
        self._linestart = [0]
        for i in range(len(self._linelength)-1):
            self._linestart.append(self._linestart[-1]+self._linelength[i])
        print(self._linelength)

    def __repr__(self):
        lines = ["".join(str(c).center(6) for c in self._data[ls:ls+ll]).strip() for ls, ll in zip(self._linestart, self._linelength)]
        l = len(max(lines, key = len))
        return "\n".join(line.center(l) for line in lines)

    def get_indices(self):
        indices = HexagonalGrid(self.size)
        for x, l in enumerate(self._linelength):
            for y in range(l):
                indices[x,y] = f"{x},{y}"
        return indices

    def __getitem__(self, pos):
        x, y = pos
        if 0 <= x < self.size and 0 <= y < self._linelength[x]:
            index = self._linestart[x] + y
            return self._data[index]
        else:
            raise IndexError("Position hors de la grille hexagonale")

    def __setitem__(self, pos, value):
        x, y = pos
        if 0 <= x < self.size and 0 <= y < self._linelength[x]:
            index = self._linestart[x] + y
            self._data[index] = value
        else:
            raise IndexError("Position hors de la grille hexagonale")

a = HexagonalGrid(5)
print(a)

a[1,1] = 6
a[2,1] = 654
print(a)

print(a.get_indices())
