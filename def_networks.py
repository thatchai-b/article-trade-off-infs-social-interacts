import scipy.stats
import networkx as nx
import numpy as np

def Geometric_network(N, n, geom_degseq):
    while abs( sum(geom_degseq)/len(geom_degseq) - n ) > 0.05:
        sum_degseq = 1
        while sum_degseq % 2 > 0:
            geom_degseq = scipy.stats.geom.rvs(1./n, loc=0, size=N)
            sum_degseq = sum(geom_degseq)
        G_geom = nx.configuration_model(geom_degseq)
        G_geom = nx.Graph(G_geom)
        G_geom.remove_edges_from(nx.selfloop_edges(G_geom))
        geom_degseq = [d for n, d in G_geom.degree()]
    return G_geom


def Clustered_network(N):
    while True:
        rng = np.random.default_rng()
        e = rng.poisson(2, N)              # Two random values can be changed to other distrbutions
        t = rng.poisson(1, N)
        #e = np.random.negative_binomial(1, 0.2, N)           # How I choose the number of  first value? -- 1 for link, 2 for two-star?
        #t = np.random.negative_binomial(2, 0.2, N)
        if sum(e)%2 == 0 and sum(t)%3 == 0:
            deg_tri = []
            for i in np.arange(N):
                et = (e[i], t[i])
                deg_tri.append(et)
            break
    # to make sure that random numbers practically constructed: first and second numbers are divisible by 2 and 3 respectively
    # This section shows multigraph G with degree and joint triangle degree sequence as input
    G = nx.random_clustered_graph(deg_tri)
    return G

def simplegiantcomp(G):
    for component in list(nx.connected_components(G)): #retain  only a giant component
        if len(component)<10:
            for node in component:
                G.remove_node(node)
    return G