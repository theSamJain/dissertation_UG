# 3D Composite Simpson
# Only odd number of nodes
import numpy as np

def ws(nx, ny, nz):
    if((nx%2 == 0) or (ny%2 == 0) or (nz%2 == 0)):
        raise(ValueError("Number of nodes should be odd!"))

    row1 = np.array([])
    for i in range(1, nx-1):
        if (i%2 == 0):
            row1 = np.append(row1, 2)
        else:
            row1 = np.append(row1, 4)
    row1 = np.insert(row1, 0, 1)
    row1 = np.append(row1, 1)
    row1 = row1.reshape(1, -1)

    col1 = np.array([])
    for i in range(1, ny-1):
        if (i%2 == 0):
            col1 = np.append(col1, 2)
        else:
            col1 = np.append(col1, 4)    
    col1 = np.insert(col1, 0, 1)
    col1 = np.append(col1, 1)
    col1 = col1.reshape(-1, 1)

    height1 = np.array([])
    for i in range(1, nz-1):
        if (i%2 == 0):
            height1 = np.append(height1, 2)
        else:
            height1 = np.append(height1, 4)    
    height1 = np.insert(height1, 0, 1)
    height1 = np.append(height1, 1)
    
    w2d = np.dot(col1, row1)
    w3d = np.full((nx, ny, nz), w2d)    
    for index in range(nz):
        w3d[index] = w3d[index]*height1[index]
    
    return w3d

def simpson3D(xx, yy, zz, func):
    h = xx[1]-xx[0]
    k = yy[1]-yy[0]
    m = zz[1]-zz[0]
    func_matrix = np.zeros(shape = [len(xx), len(yy), len(zz)])

    for i in range(len(xx)):
        for j in range(len(yy)):
            for l in range(len(zz)):
                func_matrix[i][j][l] = func(xx[i], yy[j], zz[l])

    weights = ws(len(xx), len(yy), len(zz))
    result = h*k*m*np.sum((func_matrix*weights).flatten())/27
    return result

if __name__ =='__main__':
    func = lambda x, y, z: np.exp(x+y+z)
    a = 0; b = 1; nx = 21
    c = 0; d = 1; ny = 21
    e = 0; f = 1; nz = 21
    xx = np.linspace(a, b, nx)
    yy = np.linspace(c, d, ny)
    zz = np.linspace(e, f, nz)
    result = simpson3D(xx, yy, zz, func)
    print(result)