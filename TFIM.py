import numpy as np
import functools as ft
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [7, 6]

def hamiltonian(N, J, h):
    H = np.zeros((2**N, 2**N))
    I = np.array([[1, 0], [0, 1]])
    sig_x = np.array([[0, 1], [1, 0]])
    sig_z = np.array([[1, 0], [0, -1]])
    
    nearest_interactions = np.tile(I, (N, 1, 1))
    nearest_interactions[0] = sig_z
    nearest_interactions[1] = sig_z

    magnetic_interaction = np.tile(I, (N, 1, 1))
    magnetic_interaction[0] = sig_x

    for i in range(N-1):
        H += -J* ft.reduce(np.kron, nearest_interactions)
        nearest_interactions = np.roll(nearest_interactions, 1, axis=0)

    for j in range(N):
        H += -h* ft.reduce(np.kron, magnetic_interaction)
        magnetic_interaction = np.roll(magnetic_interaction, 1, axis=0)
    
    return H

def basis(N):
    n_states = 2**N
    basis = [None]*n_states

    for i in range(n_states):
        basis[i] = [int(str(bit).replace('0', '-1')) for bit in bin(i)[2:].zfill(N)]

    return basis

def magnetization(state, basis):
    M = 0
    for i, bstate in enumerate(basis):
        bstate_M = 0
        for spin in bstate:
            bstate_M += (state[i]**2 * spin) / len(bstate)
        assert abs(bstate_M) <= 1
        M += abs(bstate_M)
    return M

N = np.arange(4, 11, 1)
j = 1
h = 10**np.linspace(-4.5, 4.5, 30)
data = []

# fig = plt.figure()

for index, n in enumerate(N):
    basis_states = basis(n)
    ls = []
    for magfield in h:
        m = 0
        H = hamiltonian(N = n, J = j, h = magfield)
        vals, vecs = np.linalg.eigh(H)
        groundstate = vecs[:, 0]
        m = magnetization(groundstate, basis_states)
        ls.append(m)
    data.append(ls)

    plt.figure("TFIM")
    plt.plot(h/j, data[index], linewidth= 0.5, marker = ".", label = "N = {:}".format(n))
    
# plt.locator_params(axis = 'x', nbins = 7)

# ax = fig.add_subplot(111)

# x_ticks = np.append(ax.get_xticks(), 1)
plt.xlabel("Relative coupling strength $g/J$ (dimensionless)")
plt.ylabel("Magnetization (m)")
plt.xscale('log')
# ax.set_xticks(x_ticks)
plt.legend()
plt.show()

# np.savetxt(r"C:\Users\jains\Desktop\transverse_field.txt", np.column_stack([*data]))