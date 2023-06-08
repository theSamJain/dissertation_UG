import random
import numpy as np

def montecarlo(xx, yy, func, n = None):
    if(n is None):
        n = max(len(xx), len(yy))

    xarr, yarr = [], []
    func_sum = 0
    for i in range(n):
        x, y = random.uniform(xx[0], xx[-1]), random.uniform(yy[0], yy[-1])
        xarr.append(x), yarr.append(y)
        func_sum += func(x, y)
    result = (xx[-1]-xx[0])*(yy[-1]-yy[0])*func_sum/(n)
    return(result)

def montecarlo3d(xx, yy, zz, func, n = None):
    if(n is None):
        n = max(len(xx), len(yy), len(zz))

    xarr, yarr, zarr = [], [], []
    func_sum = 0
    for i in range(n):
        x, y, z = random.uniform(xx[0], xx[-1]), random.uniform(yy[0], yy[-1]), random.uniform(zz[0], zz[-1])
        xarr.append(x), yarr.append(y), zarr.append(z)
        func_sum += func(x, y, z)
    result = (xx[-1]-xx[0])*(yy[-1]-yy[0])*(zz[-1]-zz[0])*func_sum/(n)
    return(result)

# def montecarlo_nd(coords, func, n = None):
#     if(n is None):
#         n = max()

#     func_sum = 0
#     random_basis_coords = []
#     for i in range(len(coords)):
#         random_basis_coords.append(random.uniform(coords[i][1], coords[i][-1], n)) 
#         # x, y, z = random.uniform(xx[0], xx[-1]), random.uniform(yy[0], yy[-1]), random.uniform(zz[0], zz[-1])
#     for j in range(n):
#         # func_sum += func(random_basis_coords[])
#     result = (xx[-1]-xx[0])*(yy[-1]-yy[0])*(zz[-1]-zz[0])*func_sum/(n)
#     return(result)

if __name__ == '__main__':
    xx = np.linspace(0, 1, 100)
    yy = np.linspace(0, 1, 100)
    zz = np.linspace(0, 1, 100)
    func = lambda x, y, z: np.exp(x+y+z)
    print(montecarlo3d(xx, yy, zz, func, 10**6))