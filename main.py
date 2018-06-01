# ==================================================================================================================== #
# ==================================================================================================================== #
#                                                                                                                      #
#  * main.py                  *                                                                |=---::++.--.++.:.-:.   #
#                                                                                                    -:-   -:-    -:-  #
#  * By : Emile Trotignon     *                                                                     :+:   :+:     :+:  #
#                                                                                                  :=:   :=:     :=:   #
# ---------------------------------------------------------------------------------------:==+-----+=+---+=+::===:+---- #
#                                                                                        +#+     +#:   :#:             #
#  * Created the : 19/02/2018 *                                                         =#=     =#=   =#=              #
#                                                                                       =#=    =#=   =#=               #
#  * TIPE : GraphLib          *                                                           :=##=+---+=#==---=|  * SUP * #
#                                                                                                                      #
# ==================================================================================================================== #
# ==================================================================================================================== #

from copy import copy
from typing import List, Tuple, Union


def functional_copy(destination: list, item, key: int) -> list:

    result = copy(destination)
    result[key] = item
    return result


def weird_matching(list_end: list, list_begin: list) -> List[list]:

    base = len(list_end)
    n_digits = len(list_begin)
    result = []
    current = [0] * n_digits
    print(list_begin, list_end)
    result.append(copy(current))
    while current != [base - 1] * n_digits:
        print('bou')

        current[0] += 1
        i = 0

        while current[i] == base:
            print('boubouboubyy')
            current[i] = 0
            i += 1
            current[i] += 1

        result.append(copy(current))

    return [[list_end[n] for n in r] for r in result]


class Path:

    GraphClass = 'Graph'

    def __init__(self, graph: 'GraphClass', vertice_list: List[int]=None):

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

    def is_overlapping(self, other: 'Path') -> bool:

        return all([vertex in other for vertex in self])

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
                if i not in self._vertices_list]

    def dijkstra(self, start_vertex: int, end_vertex: int, log=False):

        border_list = [type(self)(self.graph, vertice_list=[start_vertex])]
        new_best_path = border_list[0]

        if log:
            print([str(pa) for pa in border_list])

        while new_best_path[-1] != end_vertex:

            # not optimised
            new_pathes = sum(([p for p in path.expand() if not any(p.is_worst(p2) for p2 in border_list)]
                             for path in border_list), [])

            if log:
                print([str(pa) for pa in border_list])

            new_best_path = min(new_pathes)
            border_list.append(new_best_path)

        self._vertices_list = new_best_path._vertices_list
        return new_best_path


class Graph:

    PathClass = Path

    def __init__(self, neighbour_list: List[List[int]]):

        self.neighbour_list = neighbour_list

    def __repr__(self):

        return f'Graph({self.neighbour_list})'

    def get_neighbours(self, vertex: int) -> List[int]:

        return self.neighbour_list[vertex]

    def is_link(self, vertex1: int, vertex2: int) -> bool:

        return vertex2 in self.get_neighbours(vertex1)

    def get_weight(self, vertex1: int, vertex2: int) -> int:

        if self.is_link(vertex1, vertex2):
            return 1

    def dijkstra(self, start_vertex, end_vertex) -> PathClass:

        return self.PathClass(self).dijkstra(start_vertex, end_vertex)

    def breadth_first_search(self, start_vertex: int) -> List[PathClass]:

        status_list = [0] * len(self.neighbour_list)
        status_list[start_vertex] = 1
        new_pathes = [self.PathClass(self, vertice_list=[start_vertex])]
        path_list = new_pathes[:]

        while new_pathes:
            u = new_pathes[0]
            print('new_path = ', [str(p) for p in new_pathes])
            print('u.expand() = ', [str(p) for p in u.expand()], '\n')

            for path in u.expand():

                if status_list[path[-1]] == 0:
                    status_list[path[-1]] = 1
                    new_pathes.append(path)
                    path_list.append(path)

            del(new_pathes[0])
            status_list[u[-1]] = 2

        return path_list

    def depth_first_search(self, start_vertex: int):
        """
        Depth first search algorithm
        /!\ Not done yet /!\
        """
        pass

    def gen_max_path(self, start_vertex: int) -> PathClass:
        """Generate the longest path passing through the starting vertex
        """

        def aux(start_path: self.PathClass):
            return max([aux(path) for path in start_path.no_cycle_expand()]
                       + [aux(path) for path in start_path.reversed().no_cycle_expand()] + [start_path])

        first_path = self.PathClass(self, [start_vertex])
        return aux(first_path)

    def gen_max_pathes(self, start_vertices: List[int], pathes_length_list: List[Union[int, None]], min_len=2) \
            -> List[PathClass]:

        Vector = List[self.PathClass]
        print('debut gen max pathes')

        def evualuate_path_vect(vector: List[self.PathClass]) -> int:
            print('eval', vector)

            return sum(len(path) for path in vector) if vector is not None else 0

        def is_vector_valid(vector: List[self.PathClass]) -> bool:

            return all(all(path.is_overlapping(other) for other in vector if other is not path)
                       and (path.number_of_vertices() <= pathes_length_list[k]
                            if pathes_length_list is not None else True)
                       for k, path in enumerate(vector))

        def aux(start_vector: List[self.PathClass]) -> List[self.PathClass]:

            # List[Tuple[Expansion, Expansion]]
            print('debut aux', start_vector)

            next_pathes = [(path.no_cycle_expand(), path.reversed().no_cycle_expand()) for path in start_vector]
            print('nxt2', str(start_vector[0].no_cycle_expand()))
            next_vectors = sum(([functional_copy(start_vector, path, k)
                                 for path in pathes_list
                                 if is_vector_valid(functional_copy(start_vector, path, k))] +
                                [functional_copy(start_vector, path, k)
                                 for path in r_pathes_list
                                 if is_vector_valid(functional_copy(start_vector, path, k))]
                                for k, (pathes_list, r_pathes_list) in enumerate(next_pathes)),
                               [])
            print('nxt', next_vectors)
            print(start_vector)
            returner = max((start_vector if all(min_len <= path.number_of_vertices()
                           for k, path in enumerate(start_vector))
                           else []),
                           *[aux(vect) for vect in next_vectors], [], key=evualuate_path_vect)

            print('aux', returner)
            return returner

        start_vectors = [[self.PathClass(self, vertice_list=[i]) for i in li] for li in weird_matching(start_vertices, list(range(len(pathes_length_list))))]
        print(start_vectors)
        print('krkrkrk', [aux(vector) for vector in start_vectors])
        #return max(aux(vector) for vector in start_vectors)


class WeightedPath(Path):

    weighted = False

    def __len__(self):

        if self._len is None:
            s = 0

            for k, v in enumerate(self._vertices_list):

                if v != self[-1]:
                    # print(f'Logging : k : {k}, v : {v}, vertices_list: {self.vertices_list}')
                    s += self.graph.get_weight(v, self._vertices_list[k + 1])
            # print(f'len({self}) = {s}')
            self._len = s

        return self._len

    def __repr__(self):

        return f'WeightedPath({self.graph}, vertice_list={self._vertices_list})'

    def __str__(self):

        s = ''
        for k, v in enumerate(self._vertices_list):
            s += str(v)

            if v != self[-1]:
                s += f' -({self.graph.get_weight(v, self._vertices_list[k + 1])})-> '

        return s


class WeightedGraph(Graph):

    PathClass = WeightedPath

    def __init__(self, weighted_neighbour_list: List[List[Tuple[int, int]]]):

        super().__init__([])
        self.neighbour_list = weighted_neighbour_list

    def __repr__(self):

        return f'WeightedGraph({self.neighbour_list})'

    def get_neighbours(self, vertex: int) -> List[int]:

        return [i[0] for i in self.neighbour_list[vertex]]

    def get_weight(self, vertex1: int, vertex2: int) -> float:

        if self.is_link(vertex1, vertex2):
            i = self.get_neighbours(vertex1).index(vertex2)
            return self.neighbour_list[vertex1][i][1]


class WeightedVerticesPath(Path):

    GraphClass = 'WeightedVerticesGraph'

    def __len__(self):
        if self._len is None:
            self._len = sum(self.graph.weight_list[i] for i in self._vertices_list)


class WeightedVerticesGraph(Graph):

    def __init__(self, neighbour_list: List[List[int]], weight_list):
        super().__init__(neighbour_list)
        self.weight_list = weight_list

    def __repr__(self):

        return f'WeightedVerticesGraph({self.neighbour_list}, {self.weight_list})'

    def get_weight(self, vertex1: int, vertex2: int) -> float:

        if self.is_link(vertex1, vertex2):
            return self.weight_list[vertex1] + self.weight_list[vertex2]


if __name__ == '__main__':
    g = Graph([[1, 2],
               [0, 2, 5],
               [0, 1, 3, 4],
               [2, 5],
               [2, 5],
               [1, 3, 4]])
    # print([str(i) for i in g.breadth_first_search(0)])
    pprime = Path(g)
    pprime.dijkstra(0, 5)
    # print(g.dijkstra(0, 5))
    # g.get_neighbours(0)
    # print(p)

    wg = WeightedGraph([[(1, 1), (2, 1)],
                        [(0, 1), (2, 2), (5, 10)],
                        [(0, 1), (1, 2), (3, 3), (4, 1)],
                        [(2, 3), (5, 4)],
                        [(2, 10), (5, 1)],
                        [(3, 4), (4, 1)]])
    wp = WeightedPath(wg)
    # print(wg.dijkstra(0, 5))
    # wp1 = WeightedPath(wg, vertice_list=[0, 1, 2])
    # wp2 = WeightedPath(wg, vertice_list=[0, 2])
    # wp.dijkstra(0, 5)
    # print(wg.dijkstra(0, 5))
    # print([str(i) for i in wg.breadth_first_search(0)])
    # print(weird_matching(['c', 'd', 'e'], ['a', 'b', 'c']))
    # just checking stuff

    circuit2 = WeightedVerticesGraph([[1, 5], [0, 2], [1, 3], [2, 4], [3, 5], [0, 4]], [0, 50, 0, 10, 0, 50])
    circuit = WeightedVerticesGraph([[1], [0, 2, 5], [1, 3], [2, 4, 5], [3], [1, 3]], [50, 10, 50, 10, 50, 100])
    vroum = circuit.gen_max_pathes([0], [1000])
    print('vroum :', vroum)