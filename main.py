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

from typing import *


class Graph:

    def __init__(self, neighbour_list: List[List[int]]):

        self.neighbour_list = neighbour_list

    def __repr__(self):

        return f'Graph({self.neighbour_list})'

    def neighbours(self, vertice):

        return self.neighbour_list[vertice]


class Path:

    def __init__(self, graph: Graph, vertice_list=[]):

        self.graph = graph
        self.vertices_list = vertice_list

    def __len__(self):
        return len(self.vertices_list)

    def __eq__(self, other):
        return self == other

    def __lt__(self, other):
        return len(self) < len(other)

    def __le__(self, other):
        return len(self) <= len(other)

    def __gt__(self, other):
        return len(self) > len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __repr__(self):

        return f'Path({self.graph}, vertice_list={self.vertices_list})'

    def __str__(self):

        s = ''

        for k, v in enumerate(self.vertices_list):
            s += str(v)

            if k < len(self.vertices_list) - 1:
                s += ' -> '

        return s

    def __getitem__(self, item: int):

        return self.vertices_list[item]

    def expand(self):

        return [Path(self.graph, vertice_list=self.vertices_list + [i])
                for i in self.graph.neighbours(self.get_last_vertex())
                if i != self.vertices_list[len(self.vertices_list) - 2]]

    def get_last_vertex(self):

        return self[len(self) - 1]

    def dijkstra(self, start_vertex, end_vertex, log=False):

        border_list = [Path(self.graph, vertice_list=[start_vertex])]
        path_to_explore = border_list[0]

        if log:
            print([str(pa) for pa in border_list])

        while path_to_explore.get_last_vertice() != end_vertex:

            new_pathes = path_to_explore.expand()
            ok_pathes = [path for path in new_pathes if path.get_last_vertex() == end_vertex]

            if log:
                print([str(pa) for pa in border_list + new_pathes])

            if len(ok_pathes) > 0:
                self.vertices_list = ok_pathes[0]
                return ok_pathes[0]

            border_list += path_to_explore.expand()
            border_list.remove(path_to_explore)
            path_to_explore = min(border_list)


g = Graph([[1, 2], [0, 2, 5], [0, 1, 3, 4], [2, 5], [2, 5], [3, 4]])

p = Path(g)
p.dijkstra(0, 5, log=True)

print(str(p))
