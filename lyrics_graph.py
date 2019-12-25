import pyphonetics
from networkx import Graph, algorithms as graph_algorithms
from itertools import permutations


class RhymeGraph:
    def __init__(self, sentences):
        self._rs = pyphonetics.RefinedSoundex()
        self.g = Graph()
        self.g.add_nodes_from(sentences)
        for sentence1 in sentences:
            for sentence2 in sentences:
                w = self._distance(sentence1, sentence2)
                self.g.add_edge(sentence1, sentence2, weight=w)

    def _distance(self, sentence1, sentence2):
        return self._rs.distance(RhymeGraph.last_word(sentence1),
                                 RhymeGraph.last_word(sentence2))

    @staticmethod
    def last_word(s):
        s = s.strip()
        k = len(s) - 1
        while k > 0 and s[k] != ' ':
            k -= 1
        return s[k+1:]

    def path_dist(self, path):
        total_weight = 0
        for ind, node in enumerate(path):
            total_weight += self.g.edges[path[ind - 1]][node]['weight']
        return total_weight

    def min_path(self, length):
        all_paths = list(permutations(self.g.nodes, length))
        min_path = all_paths[0]
        min_path_dist = self.path_dist(min_path)
        for path in all_paths:
            dist = self.path_dist(path)
            if dist < min_path_dist:
                min_path = path
                min_path_dist = dist
        return min_path
