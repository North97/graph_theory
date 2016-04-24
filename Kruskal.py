from DisjointSetUnion import DisjointSetUnion


class Kruskal:
    """ Класс, реализующий алгоритм Краскала.

    Поля:
    graph -- объект класса Graph
    spanning_tree -- минимальный остов графа graph
    dsu -- система непересекающихся множеств для поддержания компонент связности. Объект класса DisjointSetUnion
    """
    graph = {}
    spanning_tree = []
    dsu = None

    def __init__(self, graph):
        """ Инициализация основных полей класса.

        Аргументы:
        graph -- объект класса Graph
        """
        self.graph = graph
        self.dsu = DisjointSetUnion(range(self.graph.count_of_vertex))

    def run(self):
        """ Реализация алгоритма Краскала. Асимптотика -- O(m log(n)). """
        for elem in self.graph.edges.keys():
            for pair in self.graph.edges[elem]:
                if self.dsu.find_set(pair[0]) != self.dsu.find_set(pair[1]):
                    self.spanning_tree.append(pair)
                    self.dsu.union(pair[0], pair[1])
        self.print_result()

    def print_result(self):
        """ Вывод результатов работы алгоритма на экран. """
        print("-----------------------------------------------------------------------------")
        print("Алгоритм Краскала.")
        print("Ребра остовного дерева:")
        for elem in self.spanning_tree:
            print("%d -- %d" % (elem[0], elem[1]))
        print("-----------------------------------------------------------------------------\n")
