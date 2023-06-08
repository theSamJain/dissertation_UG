# 2D Composite Simpson
# Only odd number of nodes
import numpy as np

def ws(nx, ny):
    if((nx%2 == 0) or (ny%2 == 0)):
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

    w = np.dot(col1, row1)
    return w

def simpson2D(xx, yy, func):
    h = xx[1]-xx[0]
    k = yy[1]-yy[0]
    func_matrix = np.zeros(shape = [len(xx), len(yy)])

    for i in range(len(xx)):
        for j in range(len(yy)):
            func_matrix[i][j] = func(xx[i], yy[j])

    weights = ws(len(xx), len(yy))
    result = h*k*np.sum((func_matrix*weights).flatten())/9
    return result

if __name__ =='__main__':

    func = lambda x, y: x*y
    a = 0; b = 1; nx = 3
    c = 0; d = 1; ny = 3
    xx = np.linspace(a, b, nx)
    yy = np.linspace(c, d, ny)
    result = simpson2D(xx, yy, func)
    print(result)