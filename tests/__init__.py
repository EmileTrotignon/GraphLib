from tests.context import *
from GraphLib import *


def graph_test():
    g = Graph([[1, 2],
               [0, 2, 5],
               [0, 1, 3, 4],
               [2, 5],
               [2, 5],
               [1, 3, 4]])
    assert [str(i) for i in g.breadth_first_search(0)] == [Path(g, [0]),
                                                           Path(g, [0, 1]),
                                                           Path(g, [0, 2]),
                                                           Path(g, [0, 1, 5]),
                                                           Path(g, [0, 2, 3]),
                                                           Path(g, [0, 2, 4])]

    assert g.neighbour_list == [[1, 2], [0, 2, 5], [0, 1, 3, 4], [2, 5], [2, 5], [1, 3, 4]]

    assert g.dijkstra(0, 5) == Path(g, [0, 1, 5]) == Path(g).dijkstra(0, 5)


def weighted_graph_test():
    wg = WeightedGraph([[(1, 1), (2, 1)],
                        [(0, 1), (2, 2), (5, 10)],
                        [(0, 1), (1, 2), (3, 3), (4, 1)],
                        [(2, 3), (5, 4)],
                        [(2, 1), (5, 1)],
                        [(1, 10), (3, 4), (4, 1)]])
    assert wg.dijkstra(0, 5) == WeightedPath(wg, [0, 2, 4, 5]) == WeightedPath(g).dijkstra(0, 5)
    # wp1 = WeightedPath(wg, vertice_list=[0, 1, 2])
    # wp2 = WeightedPath(wg, vertice_list=[0, 2])
    # wp.dijkstra(0, 5)
    # print(wg.dijkstra(0, 5))
    # print([str(i) for i in wg.breadth_first_search(0)])
    # print(weird_matching(['c', 'd', 'e'], ['a', 'b', 'c']))
    # just checking stuff


def weighted_vertices_graph_test():
    # Cycle graph
    circuit = WeightedVerticesGraph([[1, 5],
                                     [0, 2],
                                     [1, 3],
                                     [2, 4],
                                     [3, 5],
                                     [0, 4]],
                                    [0, 50, 0, 10, 0, 50])

    assert len(circuit.gen_max_path(1)) == 110
    assert sum([len(i) for i in circuit.gen_max_pathes([1, 5], [2, 2])]) == 160
    assert sum([len(i) for i in circuit.gen_max_pathes([1, 5], [2, 3])]) == 210
    assert sum([len(i) for i in circuit.gen_max_pathes([1, 5], [3, 3])]) == 210
    assert sum([len(i) for i in circuit.gen_max_pathes([1, 5], [5, 5])]) == 210

    circuit2 = WeightedVerticesGraph([[1],
                                      [0, 2, 5],
                                      [1, 3],
                                      [2, 4, 5],
                                      [3],
                                      [1, 3]],
                                     [50, 10, 50, 10, 50, 100])
    circuit3 = WeightedVerticesGraph([[1],
                                      [0, 2],
                                      [1, 3, 11],
                                      [2, 4],
                                      [3, 5],
                                      [4, 6],
                                      [5, 7, 9],
                                      [6, 8],
                                      [7],
                                      [6, 10],
                                      [9, 11],
                                      [2, 10]],
                                     [30, 0, 50, 0, 100, 0, 50, 0, 40, 0, 10, 0])
    circuit4 = WeightedVerticesGraph([[1],
                                      [0, 2],
                                      [1]],
                                     [10, 0, 10])
    # vroum = str(circuit3.gen_max_pathes([0, 8], [2, 2]))
    # vroum2 = str(circuit.gen_max_path(0))
    print(circuit4.gen_max_pathes([0], [4, 4]))
    # print('vroum :', vroum)
    # print('vroum2 :', vroum2)


def utilities_test():
    assert weird_matching(['c', 'd', 'e'], ['a', 'b', 'c']) == [['c', 'c', 'c'], ['d', 'c', 'c'], ['e', 'c', 'c'],
                                                                ['c', 'd', 'c'], ['d', 'd', 'c'], ['e', 'd', 'c'],
                                                                ['c', 'e', 'c'], ['d', 'e', 'c'], ['e', 'e', 'c'],
                                                                ['c', 'c', 'd'], ['d', 'c', 'd'], ['e', 'c', 'd'],
                                                                ['c', 'd', 'd'], ['d', 'd', 'd'], ['e', 'd', 'd'],
                                                                ['c', 'e', 'd'], ['d', 'e', 'd'], ['e', 'e', 'd'],
                                                                ['c', 'c', 'e'], ['d', 'c', 'e'], ['e', 'c', 'e'],
                                                                ['c', 'd', 'e'], ['d', 'd', 'e'], ['e', 'd', 'e'],
                                                                ['c', 'e', 'e'], ['d', 'e', 'e'], ['e', 'e', 'e']]
