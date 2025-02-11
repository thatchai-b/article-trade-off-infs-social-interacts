import EoN
from def_networks import *

def SIS_EoN_dynamics_ER(N, n, N_inf_init, tau, gamma, Tmax):
    G = nx.fast_gnp_random_graph( N, n/(N-1) )
    nodes_init_inf = G.nodes()
    t, S, I = EoN.fast_SIS(G, tau, gamma, initial_infecteds=nodes_init_inf, tmax=Tmax)
    return t, S, I

def SIS_EoN_dynamics_nreg(N, n, N_inf_init, tau, gamma, Tmax):
    G = nx.random_regular_graph( n, N )
    nodes_init_inf = G.nodes()
    t, S, I = EoN.fast_SIS(G, tau, gamma, initial_infecteds=nodes_init_inf, tmax=Tmax)
    return t, S, I

def SIS_EoN_dynamics_geom(N, n, N_inf_init, tau, gamma, Tmax):
    geom_degseq = [0, 0]
    G = Geometric_network(N, n, geom_degseq)
    nodes_init_inf = G.nodes()
    t, S, I = EoN.fast_SIS(G, tau, gamma, initial_infecteds=nodes_init_inf, tmax=Tmax)
    return t, S, I