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

import numpy as np


class Graph:

    def __init__(self, neighbour_list):

        self.neighbour_list = neighbour_list

    def neighbours(self, vertice):
        return self.neighbour_list[vertice]


class Path:

    def __init__(self, graph):
        self.graph = graph

    def dijkstra(self, start_vertice, end_vertice):
        border_list = [(start_vertice, 0)]

        k = 0
        while border_list[k] != end_vertice:
            border_list += [ (i, border_list[k][1] + 1) for i in border_list[k].neighour]
            k = min(range(len(border_list)), key=lambda x: border_list[x][1])
