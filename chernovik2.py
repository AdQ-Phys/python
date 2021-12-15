import matplotlib.pyplot as plt
import numpy as np
from numpy import loadtxt
import matplotlib
from matplotlib.axes import Axes as ax

Ampl=loadtxt('Ampl.txt',delimiter='	',unpack=False)

def IFR(k,l,n,name):
	Raz=np.max(k)-np.min(k)
	k=np.sort(k)
	delta=Raz/l
	Inter=[k[0]]
	for i in range(1,l):
		j=k[0]+delta*i
		Inter.append(j)
	KolPop=[1]
	for i in range(0,len(Inter)-1):
		j=0
		for m in range(0,len(k)-1):
			if k[m]>Inter[i] and k[m]<=Inter[i+1]:
				j=j+1
		KolPop.append(j)
	KolPop[len(KolPop)-1]=1
	ver=[]
	for number in KolPop:
		ver.append(number/len(k))
	
	NakopVer=[ver[0]]
	for i in range(1,len(ver)-1):
		j=ver[0:i+1]
		k=np.sum(j)
		NakopVer=np.append(NakopVer,k)
	Inter2=Inter[1:len(Inter)]
	for i in range(0,len(NakopVer)):
		NakopVer[i]=NakopVer[i]*100
		
		
		
	NakopVer=np.round(NakopVer,decimals=2)
	Inter2=np.round(Inter2,decimals=2)
	ind=[]
	for i in range(1,len(NakopVer)-1):
		if NakopVer[i]==NakopVer[i-1]:
			ind=np.append(ind,i)
	ind=ind.astype(int)
	ind=list(ind)
	print(Inter2,NakopVer,ind)
	
	NakopVer=np.delete(NakopVer,ind)
	Inter2=np.delete(Inter2,ind)		
	fig=plt.figure()
	ax = fig.add_axes([0.2, 0.1, 0.6, 0.8])
	y1=[]
	for num in NakopVer:
		y=round(np.ceil(0.587972*(0.0953454+0.340013+num))+(np.tanh(0.836249*np.sqrt(-0.00999988+num))/0.0257725)+abs(np.tan(-0.0468725*num)))
		y1=np.append(y1,y)
	ax.plot(Inter2,y1,'ro',markersize=2)
	plt.grid(True)
	ax.set_yticks([0,13,27,40,55,70,86,101,114,128,141])
	ax.set_xticks([0.2,0.6,1,1.4,1.8,2.2,2.6])
	ax.set_xticklabels([0.2,0.6,1,1.4,1.8,2.2,2.6])
	ax.set_yticklabels([0.01,0.1,1,5,20,50,80,95,99,99.9,99.99])
	ax.set(xlim=(0.2,2.6),ylim=(0,141))
	plt.xlabel('E/A, КДж/кг')
	plt.ylabel(r'P(X$\leq$x),%')
	plt.title('Интегральная функция распределения('+name+')')
	plt.show()
	print(max(Inter2),min(Inter2))


print(IFR(Ampl,95,1,'123'))