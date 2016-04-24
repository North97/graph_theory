INT_MAX = 1000000000


class Dijkstra:
    """ Класс, реализующий алгоритм Дейкстры.

    Поля:
    parents -- список родителей i-ой вершины
    visited -- список посещенных вершин
    path -- список кратчайших путей в i-ую вершину
    length -- список кратчайших длин путей в i-ую вершину
    graph -- ссылка на объект класса Graph
    """
    parents = []
    visited = []
    path = []
    length = []
    graph = {}

    def __init__(self, graph):
        """ Инициализация основных полей класса.

        Аргументы:
        graph -- объект класса Graph
        """
        self.graph = graph
        for i in range(self.graph.count_of_vertex):
            self.length.append(INT_MAX)
            self.visited.append(False)
            self.parents.append(-1)
            self.path.append([])

    def run(self, start_vertex):
        """ Реализация алгоритма Дейкстры.

        Аргументы:
        start_vertex -- вершина, с которой начинается алгоритм
        """
        try:
            if start_vertex < 0 or start_vertex >= self.graph.count_of_vertex:
                raise Exception("Индекс стартовой вершины вышел за допустимые границы.")

            self.length[start_vertex] = 0

            for i in range(self.graph.count_of_vertex):
                vertex = self.find_min_vertex()

                if self.length[vertex] == INT_MAX or vertex not in self.graph.graph:
                    break

                self.visited[vertex] = True

                for item in self.graph.graph[vertex].keys():
                    if self.graph.graph[vertex][item] + self.length[vertex] < self.length[item]:
                        self.length[item] = self.graph.graph[vertex][item] + self.length[vertex]
                        self.parents[item] = vertex
            self.path_recovery(start_vertex)
            self.print_result(start_vertex)
        except Exception:
            print("В приложении возникла ошибка.")

    def path_recovery(self, start_vertex):
        """Восстанавливает пути из исходной вершины во все остальные.

        Аргументы:
        start_vertex -- вершина, с которой начинается алгоритм
        """
        for i in range(self.graph.count_of_vertex):
            if i != start_vertex:
                self.path[i].append(i)
                temp = self.parents[i]

                while temp != -1:
                    self.path[i].append(temp)
                    temp = self.parents[temp]
                self.path[i].reverse()

    def print_result(self, start_vertex):
        """ Вывод на экран результат работы алгоритма.

        Аргументы:
        start_vertex -- вешина, из котороей стартует алгоритм
        """
        result_string = "-----------------------------------------------------------------------------\n"
        result_string += "Алгоритм Дейкстры. Запуск из вершины " + str(start_vertex) + ".\n"
        for i in range(self.graph.count_of_vertex):
            if i != start_vertex:
                result_string += "Расстояние до вершины " + str(i) + ": \t" + str(self.length[i]) + "\t\tПуть: "
                for item in self.path[i][:-1]:
                    result_string += str(item) + " -> "
                result_string += str(self.path[i][-1]) + "\n"
        result_string += "-----------------------------------------------------------------------------\n"
        print(result_string)

    def find_min_vertex(self):
        """ Возвращает индекс минимального расстояния в списке путей. """
        current_minimum = INT_MAX
        result = -1
        for i in range(self.graph.count_of_vertex):
            if self.length[i] < current_minimum and not self.visited[i]:
                current_minimum = self.length[i]
                result = i
        return result
