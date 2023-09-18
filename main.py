import matplotlib.pyplot as pp
import numpy as np

data5 = np.loadtxt(fname = 'gap5um.txt')
X1 = []
Y1 = []
for i in range(len(data5)):
    for j in range(2):
        if j==0:
            X1.append(data5[i][j])
        else:
            Y1.append(data5[i][j])
data10 = np.loadtxt(fname = 'gap10um.txt')
X2 = []
Y2 = []
for i in range(len(data10)):
    for j in range(2):
        if j==0:
            X2.append(data10[i][j])
        else:
            Y2.append(data10[i][j])
data20 = np.loadtxt(fname = 'gap20um.txt')
X3 = []
Y3 = []
for i in range(len(data20)):
    for j in range(2):
        if j==0:
            X3.append(data20[i][j])
        else:
            Y3.append(data20[i][j])
data40 = np.loadtxt(fname = 'gap40um.txt')
X4 = []
Y4 = []
for i in range(len(data40)):
    for j in range(2):
        if j==0:
            X4.append(data40[i][j])
        else:
            Y4.append(data40[i][j])
#f = np.loadtxt("gap5um.txt", usecols=[0])
#Z = np.zeros([len(f),len(w)], dtype=float)
#for i in range(len(w)):
#    Z[:,i] = np.loadtxt("gap5um.txt", usecols=[1])

pp.figure()
pp.plot(X1, Y1, label="gap = 5um")
pp.plot(X2, Y2, label="gap = 10um")
pp.plot(X3, Y3, label="gap = 20um")
pp.plot(X4, Y4, label="gap = 40um")
pp.title("Z1.1 vs gap width")
pp.xlabel("frequency (GHz)")
pp.ylabel("Impedance (Ohms)")
pp.legend()
pp.show()