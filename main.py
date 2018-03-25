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

from typing import List, Tuple


class Path:

    def __init__(self, graph, vertice_list=None):

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

    def __len__(self):

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

    def __getitem__(self, item: int):

        return self._vertices_list[item]

    def is_same(self, other) -> bool:

        return (self[0] == other[0]) \
               and (self[-1] == other[-1])

    def is_better(self, other) -> bool:

        return self.is_same(other) and len(self) < len(other)

    def is_worst(self, other) -> bool:

        return self.is_same(other) and len(self) >= len(other)

    def expand(self):

        return [self + i for i in self.graph.get_neighbours(self[-1])
                if i != self._vertices_list[len(self._vertices_list) - 2]]

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

    def get_neighbours(self, vertex):

        return self.neighbour_list[vertex]

    def is_link(self, vertex1, vertex2):

        return vertex2 in self.get_neighbours(vertex1)

    def get_weight(self, vertex1: int, vertex2: int):

        if self.is_link(vertex1, vertex2):
            return 1

    def dijkstra(self, start_vertex, end_vertex):

        return self.PathClass(self).dijkstra(start_vertex, end_vertex)

    def breadth_first_search(self, start_vertex: int):

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

        super(type(self), self).__init__([])
        self.neighbour_list = weighted_neighbour_list

    def __repr__(self):

        return f'WeightedGraph({self.neighbour_list})'

    def get_neighbours(self, vertex: int) -> List[int]:

        return [i[0] for i in self.neighbour_list[vertex]]

    def get_weight(self, vertex1: int, vertex2: int) -> float:

        if self.is_link(vertex1, vertex2):
            i = self.get_neighbours(vertex1).index(vertex2)
            return self.neighbour_list[vertex1][i][1]


if __name__ == '__main__':
    g = Graph([[1, 2], [0, 2, 5], [0, 1, 3, 4], [2, 5], [2, 5], [3, 4]])
    print([str(i) for i in g.breadth_first_search(0)])
    # p = Path(g)
    # p.dijkstra(0, 5, log=True)

    # g.get_neighbours(0)
    # print(p)

    wg = WeightedGraph([[(1, 1), (2, 1)],
                        [(0, 1), (2, 2), (5, 10)],
                        [(0, 1), (1, 2), (3, 3), (4, 1)],
                        [(2, 3), (5, 4)],
                        [(2, 1), (5, 1)], [(3, 4), (4, 1)]])
    # wp = WeightedPath(wg)
    # wp1 = WeightedPath(wg, vertice_list=[0, 1, 2])
    # wp2 = WeightedPath(wg, vertice_list=[0, 2])
    # wp.dijkstra(0, 5, log=True)

    print([str(i) for i in wg.breadth_first_search(0)])
