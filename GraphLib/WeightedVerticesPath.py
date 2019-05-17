from GraphLib.Path import Path


class WeightedVerticesPath(Path):
    GraphClass = 'WeightedVerticesGraph'

    def __len__(self):
        # if self._len is None:
        self._len = sum(self.graph.weight_list[i] for i in self._vertices_list)
        return self._len

    def __repr__(self):
        return self.__str__()

    def __str__(self) -> str:
        s = ''
        for k, v in enumerate(self._vertices_list):
            s += str(v) + f'({self.graph.weight_list[v]})'

            if v != self[-1]:
                s += ' -> '

        return s

    def is_overlapping(self, other: 'Path'):
        """Check for overlapping pathes. An overlap at a city is acceptable"""

        r = all((vertex not in other) or (self.graph[vertex] != 0) for vertex in self)

        return r

    def number_of_vertices(self):

        return sum(1 for v in self if self.graph.weight_list[v])
