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
#вручную ввели минимумы и максимумы(примерно)

step=((1*(10**(-4)))-(6.3*(10**(-5))))/1000
len=0
for i in range(999):
    x=step*i + (6.3*(10**(-5)))
    line=(((P(x)-P(x+step))**2)+step**2)**(1/2)
    len=len+line
print(len)



