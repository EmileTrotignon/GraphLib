from typing import *
from GraphLib.Graph import Graph
from GraphLib.WeightedPath import WeightedPath


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
