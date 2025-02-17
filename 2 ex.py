import numpy as np
import matplotlib.pyplot as mp

b=3.19*(10**(-5))
V=np.linspace(b+(10**(-5)),10**(-3),1000)
R=8.314
T=-130+273.15
a=0.1382
P=((R*T)/(V-b)-(a/(V**2)))
max=[]
min=[]
fig,ax=mp.subplots()
mp.plot(V,P, label='зависимость P от V', color ='black' )
mp.legend()
ax.set_xlabel("V")
ax.set_ylabel("P")
mp.show()
for i in range(0,len(V)-1):
    if P[i]>P[i+1] and P[i]>P[i-1]:
        max.append([i])
for i in range(0,len(V)-1):
    if P[i]<P[i+1] and P[i]<P[i-1]:
        min.append([i])
print(max,min)
