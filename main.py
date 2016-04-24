from Graph import Graph
from Dijkstra import Dijkstra
from Floyd import Floyd
from Prima import Prima
from Kruskal import Kruskal

if __name__ == "__main__":
    g = Graph("in.txt", False)

    d = Dijkstra(g)
    f = Floyd(g)
    p = Prima(g)
    k = Kruskal(g)

    d.run(0)
    f.run()
    p.run()
    k.run()
