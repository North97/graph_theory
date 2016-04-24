INT_MAX = 1000000000


class Floyd:
    """ Класс, реализующий алгоритм Флойда.

    Поля:
    graph -- объект класса Graph
    length -- результирующая матрица расстояний между вернишами
    parent -- результрующая матрица предков вершин
    """
    graph = {}
    length = []
    parent = []

    def __init__(self, graph):
        """ Инициализация полей класса. Задание матрицы смежности.

        Аргументы:
        graph -- объект класса Graph
        """
        self.graph = graph
        self.length = [[INT_MAX for j in range(graph.count_of_vertex)] for i in range(graph.count_of_vertex)]
        self.parent = [['XX' for j in range(graph.count_of_vertex)] for i in range(graph.count_of_vertex)]
        for i in range(graph.count_of_vertex):
            for j in range(graph.count_of_vertex):
                if i in self.graph.graph:
                    if j in self.graph.graph[i]:
                        self.length[i][j] = graph.graph[i][j]

    def run(self):
        """ Реализация алгоритма флойда с сохранением предков. """
        for i in range(self.graph.count_of_vertex):
            for j in range(self.graph.count_of_vertex):
                for k in range(self.graph.count_of_vertex):
                    if j != k and self.length[j][i] + self.length[i][k] < self.length[j][k]:
                        self.length[j][k] = self.length[j][i] + self.length[i][k]
                        self.parent[j][k] = i
        self.print_result()

    def print_result(self):
        """ Вывод результатов алгоритма на экран. """
        print("-----------------------------------------------------------------------------\n" +
              "Алгоритм Флойда.")
        self.print_matrix(self.length)
        print()
        self.print_matrix(self.parent)
        print("-----------------------------------------------------------------------------\n")

    def print_matrix(self, matrix):
        """ Вывод матрицы.

        Аргументы:
        matrix -- двумерный массив, представляющий собой матрицу self.graph.count_of_vertex ^ 2 элементов
        """
        print('/', end="\t")
        for i in range(self.graph.count_of_vertex):
            print(i, end="\t")
        print()
        for i in range(self.graph.count_of_vertex):
            print(i, end="\t")
            for j in range(self.graph.count_of_vertex):
                print('XX' if matrix[i][j] == INT_MAX else matrix[i][j], end="\t")
            print()
