# ==================================================================================================================== #
#                                                                                                                      #
#  * __init__.py              *                                                                    |=---::++.--.++.:.-:#
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

from GraphLib.Path import Path
from GraphLib.Graph import Graph
from GraphLib.WeightedPath import WeightedPath
from GraphLib.WeightedGraph import WeightedGraph
from GraphLib.WeightedVerticesPath import WeightedVerticesPath
from GraphLib.WeightedVerticeGraph import WeightedVerticesGraph
from GraphLib.utilities import *
if __name__ == '__main__':
    print(weird_matching(['c', 'd', 'e'], ['a', 'b', 'c']))
