from GraphLib.Path import Path


class WeightedPath(Path):
    weighted = False

    def __len__(self):

        if self._len is None:
            s = 0

            for k, v in enumerate(self._vertices_list):

                if v != self[-1]:
                    s += self.graph.get_weight(v, self._vertices_list[k + 1])

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
