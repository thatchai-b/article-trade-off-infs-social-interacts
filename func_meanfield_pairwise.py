def Istar_MF(N, ntau, gamma):
    Istar_mf = N*(1 - (gamma/(ntau)))
    Istar_mf[ntau < gamma] = 0
    return Istar_mf

def Istar_PW(N, n, tau, gamma, kappa):
    numlink_value = n*N
    first_term = ( tau *kappa* numlink_value + 2*gamma*kappa*N + tau *kappa*N - 2*gamma*N)
    sqrt_term  = (4*gamma*N*(kappa* numlink_value - numlink_value+N) + tau *(N-numlink_value)**2)
    denom      = 2*(gamma*kappa**2 + gamma - 2*gamma*kappa - tau *kappa)

    Istar_pos = ( (-1)*first_term + kappa*(tau * sqrt_term)**(1/2) ) / denom
    Istar_pos[n*tau*kappa < gamma] = 0
    return Istar_pos