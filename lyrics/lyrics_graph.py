import pyphonetics
from networkx import Graph, algorithms as graph_algorithms
from random import randint


class RhymeGraph:
    def __init__(self, sentences):
        self.max_phrases = 20

        # Limit it to the shortest 20 sentences
        if len(sentences) > self.max_phrases:
            sentences = sorted(sentences, key=lambda a: len(a))
            sentences = sentences[:20]

        self._rs = pyphonetics.RefinedSoundex()
        self.g = Graph()
        self.g.add_nodes_from(sentences)

        for sentence1 in sentences:
            for sentence2 in sentences:
                w = self._distance(sentence1, sentence2)
                self.g.add_edge(sentence1, sentence2, weight=w)

    def _distance(self, sentence1, sentence2):
        l1 = self.last_word(sentence1)
        l2 = self.last_word(sentence2)
        try:
            return self._rs.distance(l1, l2)
        except IndexError:
            return float('inf')

    def path_dist(self, path):
        total_weight = 0
        for ind, node in enumerate(path):
            total_weight += self.g.edges[path[ind - 1]][node]['weight']
        return total_weight

    def min_path(self, length):
        start_point = list(self.g.nodes)[randint(0, self.max_phrases)]
        path = [start_point]
        for i in range(length - 1):
            curr = path[-1]
            neighbors = self.g.neighbors(curr)
            closest_neighbor = neighbors[0]
            closest_dist = self.g[curr][closest_neighbor]['weight']
            for neighbor in neighbors[1:]:
                if self.g.edges[curr][neighbor]['weight'] < closest_dist:
                    closest_neighbor = neighbor
            path.append(closest_neighbor)

    @staticmethod
    def last_word(s):
        return s.split(' ')[-1]
