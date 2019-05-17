from typing import *
import functools
from GraphLib.utilities import *
from GraphLib.Path import Path


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

            del (new_pathes[0])
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

        path_class = self.PathClass

        def aux(start_path: path_class):
            return max([aux(path) for path in start_path.no_cycle_expand()]
                       + [aux(path) for path in start_path.reversed().no_cycle_expand()] + [start_path])

        first_path = self.PathClass(self, [start_vertex])
        return aux(first_path)

    def gen_max_pathes(self, start_vertices: List[int], pathes_length_list: List[Union[int, None]], min_len=2) \
            -> Tuple[PathClass]:

        path_class = self.PathClass

        def evualuate_path_vect(vector: Tuple[path_class]) -> int:

            return sum(len(path) for path in vector) if vector is not None else 0

        def is_vector_valid(vector: Tuple[path_class]) -> bool:

            return all(all(path.is_overlapping(other) for other in vector if other is not path)
                       and (path.number_of_vertices() <= pathes_length_list[k]
                            if pathes_length_list is not None else True)
                       for k, path in enumerate(vector))

        def is_vector_long_enough(vector: Tuple[path_class]):

            return all(p.number_of_vertices() >= min_len or p.number_of_vertices() == 0 for p in vector)

        @functools.lru_cache(maxsize=None)  # Memoization
        def aux(start_vector: Tuple[path_class]) -> Tuple[path_class]:

            next_pathes = no_duplicate([(path.no_cycle_expand(), path.reversed().no_cycle_expand())
                                        for path in start_vector])

            next_forward_vectors = [[functional_copy(start_vector, path, k)
                                     for path in pathes_list
                                     if is_vector_valid(functional_copy(start_vector, path, k))]
                                    for k, (pathes_list, r_pathes_list) in enumerate(next_pathes)]

            next_backward_vectors = [[functional_copy(start_vector, path, k)
                                      for path in r_pathes_list
                                      if is_vector_valid(functional_copy(start_vector, path, k))]
                                     for k, (pathes_list, r_pathes_list) in enumerate(next_pathes)]

            next_vectors = no_duplicate(sum(next_forward_vectors + next_backward_vectors, []))

            rec_results = [aux(vect) for vect in next_vectors
                           if is_vector_long_enough(aux(vect))]

            if not is_vector_long_enough(start_vector):

                if not rec_results:
                    return tuple(self.PathClass(self, vertice_list=[]) for p in start_vector)

                return max(rec_results, key=evualuate_path_vect)

            if not rec_results:
                return start_vector

            mm = max(rec_results, key=evualuate_path_vect)

            return max(start_vector, mm, key=evualuate_path_vect)

        start_vectors = [tuple(self.PathClass(self, vertice_list=[i])
                               if i is not None else self.PathClass(self) for i in li)
                         for li in weird_matching(start_vertices + [None], list(range(len(pathes_length_list))))]
        # print('srt', start_vectors)
        return max([aux(vector) for vector in start_vectors], key=evualuate_path_vect)
