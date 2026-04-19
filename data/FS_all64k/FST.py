import numpy as np
import sys as sys
import glob as glob

logAr = [  1,    2,    3,    4,    5,    6,    7,    9,   10,   12, 
          15,   18,   21,   24,   29,   34,   40,   47,   55,   64,   75, 
          88,  103,  121,  142,  166,  194,  226,  265,  309,  362,  422, 
         494,  577,  674,  787,  919, 1074, 1254, 1465, 1711, 1998]



inf = sorted(glob.glob(sys.argv[1]+"/FS_*.dat"))
outf = sys.argv[2]
k1 = int(sys.argv[3])
k2 = 2*k1; k3 = 4*k1; k4 = 8*k1
print(k1, k2, k3, k4)
time = []
fsk1, fsk2, fsk3, fsk4 = [], [], [], []
oldval = 0.0
for i,f in enumerate(inf):
    kk, fs = np.loadtxt(f, unpack=True, usecols=(0,1)) 
    if(fs[k4+2] != oldval):
       oldval = fs[k4+2]
       time.append(logAr[i])
       fsk4.append(fs[k4+2])
       fsk1.append(fs[k1+2])
       fsk2.append(fs[k2+2])
       fsk3.append(fs[k3+2])

time = np.asarray(time)
fsk1 = np.asarray(fsk1)
fsk2 = np.asarray(fsk2)
fsk3 = np.asarray(fsk3)
fsk4 = np.asarray(fsk4)

np.savetxt(outf, np.vstack([time, fsk1, fsk2, fsk3, fsk4]).T, fmt="%0.5e")

