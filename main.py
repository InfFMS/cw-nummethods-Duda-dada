
# Задание 1: Построение графиков
# Построить графики уравнения Ван-дер-Ваальса при температурах -140, -130, -120, -110, -
# 100 градусов Цельсия. Выделить красным цветом кривую, начиная с которой начинаются
# изменения в поведении функции (см. пояснение)

import numpy as np
import matplotlib.pyplot as mp
b=3.19*(10**(-5))
V=np.linspace (b+(10**(-5)),10**(-3),1000)
#1)
fig,ax=mp.subplots()
R=8.314
T1=-140+273.15
T2=-130+273.15
T3=-120+273.15
T4=-110+273.15
T5=-100+273.15
a=0.1382
P1=((R*T1)/(V-b)-(a/(V**2)))
P2=((R*T2)/(V-b)-(a/(V**2)))
P3=((R*T3)/(V-b)-(a/(V**2)))
P4=((R*T4)/(V-b)-(a/(V**2)))
P5=((R*T5)/(V-b)-(a/(V**2)))
mp.plot(V,P1, label='зависимость P1 от V', color ='black')
mp.legend()
mp.plot(V,P2, label='зависимость P2 от V', color ='grey')
mp.legend()
mp.plot(V,P3, label='зависимость P3 от V', color ='pink' )
mp.legend()
mp.plot(V,P4, label='зависимость P4 от V', color ='red' )
mp.legend()
mp.plot(V,P5, label='зависимость P5 от V', color ='purple' )
mp.legend()
ax.set_xlabel("V")
ax.set_ylabel("P")
mp.show()
# #2)
# b=3.19*(10**(-5))
# V=np.linspace (b+(10**(-5)),10**(-3),1000)
# #1)
# fig,ax=mp.subplots()
# R=8.314
# T=-140+273.15
# a=0.1382
# P=((R*T)/(V-b)-(a/(V**2)))
# mp.plot(V,P, label='зависимость P от V', color ='black' )
# ax.set_xlabel("V")
# ax.set_ylabel("P")
# mp.show()
#
# #3)
# b=3.19*(10**(-5))
# V=np.linspace (b+(10**(-5)),10**(-3),1000)
# #1)
# fig,ax=mp.subplots()
# R=8.314
# T=-140+273.15
# a=0.1382
# P=((R*T)/(V-b)-(a/(V**2)))
# mp.plot(V,P, label='зависимость P от V', color ='black' )
# ax.set_xlabel("V")
# ax.set_ylabel("P")
# mp.show()
#
# #4)
# b=3.19*(10**(-5))
# V=np.linspace (b+(10**(-5)),10**(-3),1000)
# #1)
# fig,ax=mp.subplots()
# R=8.314
# T=-140+273.15
# a=0.1382
# P=((R*T)/(V-b)-(a/(V**2)))
# mp.plot(V,P, label='зависимость P от V', color ='black' )
# ax.set_xlabel("V")
# ax.set_ylabel("P")
# mp.show()
#
# #5)
# b=3.19*(10**(-5))
# V=np.linspace (b+(10**(-5)),10**(-3),1000)
# #1)
# fig,ax=mp.subplots()
# R=8.314
# T=-140+273.15
# a=0.1382
# P=((R*T)/(V-b)-(a/(V**2)))
# mp.plot(V,P, label='зависимость P от V', color ='black' )
# ax.set_xlabel("V")
# ax.set_ylabel("P")
# mp.show()
