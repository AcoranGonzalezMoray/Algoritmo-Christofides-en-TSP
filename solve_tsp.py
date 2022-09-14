import itertools
from collections import namedtuple
import networkx as nx
import math
import os

Point = namedtuple("Point", ['x', 'y'])

def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)
    
    
def complete_graph(points):
    """ Creates a complete graph """
    G = nx.Graph()
    for x in range(len(points)-1):
        G.add_node(x)
        G.add_edge(x, x+1, weight = length(points[x], points[x+1]))#next x+1, points[x+1]
    return G



def solve_Christofides(points):
    #--------------------------------------------------------/
    G = complete_graph(points)
    min = nx.minimum_spanning_tree(G) # árbol de expansión mínimo
    Odd_min = []
    #--------------------------------------------------------/
    for node in min.nodes: # Seleccion de los nodos de min de grado impar
        if (min.degree(node) % 2 != 0):  #Recorrido y  Selección de Impar
            # Se multiplica el peso de los vértices por -1 y cuando usemos  max_weight_matching() obtendremos el emparejamiento
            # perfecto de coste mínimo
            Odd_min.append(node * -1)
    #--------------------------------------------------------/
    Odd = nx.complete_graph(Odd_min)     # Grafo con los nodos de grado impar
    Emp = nx.max_weight_matching(Odd, maxcardinality=True) # emparejamiento perfecto de coste maximo (modificado para minimo)
    #--------------------------------------------------------/
    List = []
    for i in Emp:
        List += (i[0] * -1, i[1] * -1)
    #--------------------------------------------------------/
    ListOrderMult = []
    IterZip = zip(*[iter(List)] * 2)
    for i in IterZip:
        ListOrderMult.append(i)
    min.add_edges_from(ListOrderMult)
    #--------------------------------------------------------/
    MinCost = []
    for i in nx.eulerian_circuit(min):
        if i[0] not in MinCost:
            MinCost.append(i[0])
    #--------------------------------------------------------/
    return MinCost
