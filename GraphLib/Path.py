from GraphLib.utilities import *


class Path:
    GraphClass = 'Graph'

    def __init__(self, graph: 'GraphClass', vertice_list: List[int] = None):

        if vertice_list is None:
            vertice_list = []
        self.graph = graph
        self._vertices_list = vertice_list
        self._len = None
        len(self)

    def __add__(self, other):

        if type(other) == int:
            path_sum = type(self)(self.graph, vertice_list=self._vertices_list + [other])
            path_sum._len = self._len + self.graph.get_weight(path_sum[-2], path_sum[-1])
            return path_sum

    def __len__(self) -> int:

        if self._len is None:
            self._len = len(self._vertices_list)

        return self._len

    def __lt__(self, other):

        return len(self) < len(other)

    def __le__(self, other):

        return len(self) <= len(other)

    def __gt__(self, other):

        return len(self) > len(other)

    def __ge__(self, other):

        return len(self) >= len(other)

    def __repr__(self) -> str:

        return f'Path({self.graph}, vertice_list={self._vertices_list})'

    def __str__(self) -> str:

        s = ''

        for k, v in enumerate(self._vertices_list):
            s += str(v)

            if k < len(self._vertices_list) - 1:
                s += ' -> '

        return s

    def __getitem__(self, item: int) -> int:

        return self._vertices_list[item]

    def __eq__(self, other):

        return self._vertices_list == other._vertices_list

    def __hash__(self):
        s = ''
        for vertex in self:
            s += str(vertex)
        s += str(hash(self.graph))
        return int(s)

    def is_overlapping(self, other: 'Path') -> bool:

        return all(vertex in other for vertex in self)

    def number_of_vertices(self):

        return len(self._vertices_list)

    def reversed(self) -> 'Path':
        return type(self)(self.graph, self._vertices_list[::-1])

    def is_same(self, other) -> bool:

        return (self[0] == other[0]) \
               and (self[-1] == other[-1])

    def is_better(self, other: 'Path') -> bool:

        return self.is_same(other) and len(self) < len(other)

    def is_worst(self, other: 'Path') -> bool:

        return self.is_same(other) and len(self) >= len(other)

    def expand(self) -> List['Path']:

        return [self + i for i in self.graph.get_neighbours(self[-1])
                if i != self._vertices_list[len(self._vertices_list) - 2]]

    def no_cycle_expand(self) -> List['Path']:

        return [self + i for i in self.graph.get_neighbours(self[-1])
                if i not in self._vertices_list] if len(self) > 0 else []

    def dijkstra(self, start_vertex: int, end_vertex: int):

        border_list = [type(self)(self.graph, vertice_list=[start_vertex])]
        new_best_path = border_list[0]

        while new_best_path[-1] != end_vertex:
            # not optimised
            new_pathes = sum(([p for p in path.expand() if not any(p.is_worst(p2) for p2 in border_list)]
                              for path in border_list), [])

            new_best_path = min(new_pathes)
            border_list.append(new_best_path)

        self._vertices_list = new_best_path._vertices_list
        return new_best_path
