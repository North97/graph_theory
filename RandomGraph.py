import random


def generate(count_of_vertex, count_of_edges, rang):
    """ Генерация случайного связного неориентированного графа.

    Аргументы:
    count_of_vertex -- кол-во вершин
    count_of_edges -- кол-во ребер
    rang -- диапазон веса [0; rang]
    """
    with open("in.txt", "w") as file:
        file.write("%d %d\n" % (count_of_vertex, count_of_edges))
        random.seed()
        temp = []
        i = 0
        while i < count_of_edges:
            v1 = random.randint(0, count_of_vertex - 1)
            v2 = random.randint(0, count_of_vertex - 1)
            if [v1, v2] not in temp and [v2, v1] not in temp and v1 != v2:
                t = [v1, v2]
                temp.append(t)
                d = random.randint(1, rang + 1)
                file.write("%d %d %d\n" % (v1, v2, d))
                i += 1

generate(5, 10, 10)
