#P-Pn=0
# с точностью до 10-7
# 3664186.998 P
# -130°C
#
import numpy as np
import matplotlib.pyplot as mp

Pn=3664186.99
b=3.19*(10**(-5))
V=np.linspace(b+(10**(-5)),10**(-3),1000)
R=8.314
T=-130+273.15
a=0.1382
P=((R*T)/(V-b)-(a/(V**2)))
y=P-Pn
max=[]
min=[]
fig,ax=mp.subplots()
mp.plot(V,y, label='зависимость P от V', color ='black' )
mp.legend()
ax.set_xlabel("V")
ax.set_ylabel("P-Pn")
mp.show()
eps=10**(-7)
def solve(g,m,eps):
    while m-g>=2*eps:
        c=(g+m)/2
        if y(g)*y(c)<=0:
            m=c
        else:
            g=c
    return(c)
print(solve(0.00004,0.00007, eps))

