from typing import *
from GraphLib.Graph import Graph
from GraphLib.WeightedVerticesPath import WeightedVerticesPath


class WeightedVerticesGraph(Graph):
    PathClass = WeightedVerticesPath

    def __init__(self, neighbour_list: List[List[int]], weight_list):
        super().__init__(neighbour_list)
        self.weight_list = weight_list

    def __repr__(self):
        return f'WeightedVerticesGraph({self.neighbour_list}, {self.weight_list})'

    def __getitem__(self, key):
        return self.weight_list[key]

    def get_weight(self, vertex1: int, vertex2: int) -> float:
        if self.is_link(vertex1, vertex2):
            return self.weight_list[vertex1] + self.weight_list[vertex2]
