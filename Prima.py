INT_MAX = 1000000000000000000


class Prima:
    """ Класс, реализующий алгоритм Прима.

    Поля:
    visited -- массив посещенных вершин
    vertex -- множество посещенных вершин
    spanning_tree -- минимальный остов графа graph
    graph -- объект класса Graph
    """
    visited = []
    vertex = set()
    spanning_tree = []
    graph = {}

    def __init__(self, graph):
        """ Инициализация основных полей класса.

        Аргументы:
        graph -- объект класса Graph
        """
        self.graph = graph
        for i in range(self.graph.count_of_vertex):
            self.visited.append(False)

    def run(self):
        """ Реализация алгоритма Примы. """
        self.vertex.add(0)
        while len(self.spanning_tree) < self.graph.count_of_vertex - 1:
            from_v = -1
            to_v = -1
            minimum = INT_MAX
            for value in self.vertex:
                for child in self.graph.graph[value]:
                    if not self.visited[child]:
                        if self.graph.graph[value][child] < minimum:
                            if [child, value] not in self.spanning_tree:
                                minimum = self.graph.graph[value][child]
                                from_v = value
                                to_v = child
            self.visited[to_v] = True
            self.vertex.add(to_v)
            self.spanning_tree.append([from_v, to_v])
        self.print_result()

    def print_result(self):
        """ Вывод результатов работы алгоритма на экран. """
        print("-----------------------------------------------------------------------------")
        print("Алгоритм Прима.")
        print("Ребра остовного дерева:")
        for elem in self.spanning_tree:
            print("%d -- %d" % (elem[0], elem[1]))
        print("-----------------------------------------------------------------------------\n")
