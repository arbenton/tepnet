# numerical imports
import numpy as np
import scipy as sp
import networkx as nx
# io imports
import csv
# graphical imports
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("white")

# source: OWLTRAD http://www.ciolek.com/OWTRAD/DATA/tmcZWEm1300a.html
def read (path):

    """ Read csv assuming OWLTRAD schema, convert into edges and nodes """

    with open(path) as f:
        reader = csv.DictReader(f)
        edges, nodes = [], {}
        for row in reader:
            edges.append((row["NODE1"], row["NODE2"]))
            nodes[row["NODE1"]] = [eval(row["LONG1"]), eval(row["LAT1"])]
            nodes[row["NODE2"]] = [eval(row["LONG2"]), eval(row["LAT2"])]

    return nodes, edges

def network (edges):

    """ To do...?  """

    return nx.DiGraph(edges)

def transmission (graph, r=.5, m=.5):

    """ Create adjacency matrix and add to medicine matrix on diagonal """

    routes = r*nx.adjacency_matrix(graph)
    medicn = m*sp.eye(nx.number_of_nodes(graph))

    return routes + medicn

def iterpulse (transm, pulse, epochs):
    
    """ Apply sigmoid pulse to network for specified epochs """

    history = []
    for i in range(epochs):
        pulse = np.tanh(pulse * transm)
        history.append(pulse.tolist()[0])

    return history

def plot (history):

    fig = plt.figure(figsize=(9,9))
    plt.plot(history)
    plt.title("Infection Rate per Epoch")
    plt.xlabel("Epoch")
    plt.ylabel("Infection Rate")
    fig.savefig("zoom.png")    

def graph (graph, nodes, history):

    fig = plt.figure(figsize=(9,9))
    nx.draw(graph, nodes, node_color=history[-1], 
            node_size=25, cmap=plt.cm.Blues, arrows=False)
    fig.savefig("network.png")

if __name__ == "__main__":

    N, E = read("edges.csv")
    G = network(E)
    T = transmission(G)
    P = np.zeros(len(N))
    P[160] = .1 # some place gets sick
    H = iterpulse(T, P, 50)  
    plot(H) 
    #graph(G, N, H)
