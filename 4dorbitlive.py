import numpy as np
import matplotlib.pyplot as plt

def vec(a,b,c,d = 0):
    return np.array([a,b,c],dtype=np.float64)

p = vec(5,0,0)

v = vec(1,1.5,0)

o = vec(0,0,0)

mass_diff = 5

ov = (0-v/mass_diff) + vec(1,0,0)

dt = .001
N = 10000
X = np.zeros((N),dtype=np.float64)
Y = np.zeros((N),dtype=np.float64)
Z = np.zeros((N),dtype=np.float64)
W = np.zeros((N),dtype=np.float64)

oX = np.zeros((N),dtype=np.float64)
oY = np.zeros((N),dtype=np.float64)
oZ = np.zeros((N),dtype=np.float64)
oW = np.zeros((N),dtype=np.float64)

cX = np.zeros((N),dtype=np.float64)
cY = np.zeros((N),dtype=np.float64)
cZ = np.zeros((N),dtype=np.float64)
cW = np.zeros((N),dtype=np.float64)

fig = plt.figure()
ax = fig.subplots(1,1)

for n in range(N):
    p+=v*dt
    o += ov*dt

    p_o = o - p
    a = p_o*1/(np.linalg.norm(p_o)**3)*100
    v+= a*dt
    ov += a*dt/mass_diff

    c = (p + o*mass_diff)/(1+mass_diff)

    X[n] = p[0]
    Y[n] = p[1]
    Z[n] = p[2]
    oX[n] = o[0]
    oY[n] = o[1]
    oZ[n] = o[2]
    cX[n] = c[0]
    cY[n] = c[1]
    cZ[n] = c[2]

    ax.clear()
    ax.plot(X[:n], Y[:n], oX[:n], oY[:n], cX[:n], cY[:n])
    mx = max(max(np.max(X), np.max(Y)), max(np.max(oX), np.max(oY)))
    my = min(np.min(X), np.min(Y))
    ax.set_xlim(my, mx)
    ax.set_ylim(my, mx)
    plt.pause(0.01)

plt.show()
