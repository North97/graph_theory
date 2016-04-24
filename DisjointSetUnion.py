class DisjointSetUnion:
    """ Класс, реализующий систему непересекающихся множеств.

    Поля:
    parent -- система непересекающихся множеств. множества реализованы в виде деревьев
    """
    parent = []

    def __init__(self, collection):
        """ Инициализация основных полей класса. """
        self.parent = [elem for elem in collection]
        for elem in collection:
            self.make_set(elem)

    def make_set(self, value):
        """ Создание множества с вершиной value.

        Аргументы:
        value -- вершина
        """
        self.parent[value] = value

    def find_set(self, value):
        """ Поиск множества заданной вершины.

        Аргументы:
        value -- вершина
        """
        if value == self.parent[value]:
            return value
        else:
            self.parent[value] = self.find_set(self.parent[value])
            return self.parent[value]

    def union(self, first, second):
        """ Объединение двух множеств.

        Аргументы:
        first -- вершина, содержащаяся в первом множестве
        second -- вершина, содержащаяся во втором множестве
        """
        first = self.find_set(first)
        second = self.find_set(second)
        if first != second:
            self.parent[second] = first
