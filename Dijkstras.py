from Node import *
from Edge import *
from Graph import *
import math
from queue import PriorityQueue

'''
This program asks for a desired start Node, and will
provide you length of the shortest path to every other node in the graph, 
inf if the node is unreachable from starting point

For this program, the format of the input file must be
a0,b0,l0
a1,b1,l1
...
an,bn,ln

where (ax,bx) is an edge of length lx, with
ax being the start node, bx the end node of edge ex
ax,bx will be read as strings, with the node label being of type string,
and lx will be a floating point number
'''

if __name__ == '__main__':

    g = Graph()
    file = input('name of input file: ').strip()

    #False flag is because we want an undirected graph
    g.fillGraph(file)

    unvisited_nodes = g.getAllNodes()

    start_label = input('start node: ').strip()
    start = Node(start_label)
    distance = dict()
    for node in unvisited_nodes:
        distance[node] = math.inf

    distance[start] = 0
    q = PriorityQueue()
    arr = []
    for node in unvisited_nodes:
        q.put((distance[node], node))


    while not q.empty():
        x = q.get()

        for edge in g.getEdgesFromStart(x[1]):
            if distance[edge.getEndNode()] > distance[edge.getStartNode()] + edge.getLabel():
                distance[edge.getEndNode()]  = distance[edge.getStartNode()] + edge.getLabel()
                q.put((distance[edge.getStartNode()] + edge.getLabel(), edge.getEndNode()))


    print('Distances from', start)
    for node in g.getNodesAlphabetical():
        print(node, distance[node])