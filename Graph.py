class Graph:
    """ Класс, описывающий граф и работу с ним.

    Поля:
    graph -- представление графа в виде вложенных ассоциативных массивов {vertex: {vertex: edge_length, ...}, ...}
    count_of_vertex -- количество вершин графа
    count_of_edge -- количество ребер графа
    edges -- массив ребер графа, ассоциативный их весам
    """
    graph = {}
    count_of_vertex = int()
    count_of_edge = int()
    edges = {}

    def __init__(self, filename="in.txt", is_directed=True):
        """ Инициализация графа из файла в формате:
            [count_of_vertex] [count_of_edge]
            [from_vertex] [to_vertex] [edge_weight]
            ...
            [from_vertex] [to_vertex] [edge_weight]

        Аргументы:
        filename -- имя входного файла (default "in.txt")
        is_directed -- ориентированность графа (default True)
        """
        with open(filename, "r") as file:
            line = file.readline().split(' ')
            self.count_of_vertex = int(line[0])
            self.count_of_edge = int(line[1])

            for line in file.readlines()[:-1]:  # [:-1] - Специально для платформы Linux. Срез без последней строки
                temp = [int(item) for item in line.split(' ')]
                self.__add_edge(temp[0], temp[1], temp[2])
                self.__add_weight(temp[0], temp[1], temp[2])
                if not is_directed:
                    self.__add_edge(temp[1], temp[0], temp[2])

    def __add_edge(self, from_verb, to_verb, weight):
        """ Добавление ребра в граф.

        Аргументы:
        from_verb -- начало узла
        to_verb -- конец узла
        weight -- длина ребра
        """
        if from_verb not in self.graph:
            self.graph[from_verb] = {}
        self.graph[from_verb][to_verb] = weight

    def __add_weight(self, from_verb, to_verb, weight):
        """ Добавление ребра в ассоциаивный массив ребер.

        Аргументы:
        from_verb -- начало узла
        to_verb -- конец узла
        weight -- длина ребра
        """
        if weight not in self.edges:
            self.edges[weight] = []
        self.edges[weight].append([from_verb, to_verb])
