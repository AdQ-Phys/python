������������ Windows                                   >;L7>20B5;L  W i n d o w s                                                                                                                                                                                                                                                                                                                                                                                                                                rtAmpl2=np.sort(Ampl2)
SortPotEn2=np.sort(PotEn2)
SortAmpl3=np.sort(Ampl3)
SortPotEn3=np.sort(PotEn3)
i=len(PotEn2)-1
while i>=0:
	if PotEn2[i]>120:
		PotEn2=np.delete(PotEn2,i)
		Ampl2=np.delete(Ampl2,i)
	i=i-1
i=len(PotEn3)-1
while i>=0:
	if PotEn3[i]>100:
		PotEn3=np.delete(PotEn3,i)
		Ampl3=np.delete(Ampl3,i)
	i=i-1
i=len(PotEn)-1
while i>=0:
	if PotEn[i]>150:
		PotEn=np.delete(PotEn,i)
		Ampl=np.delete(Ampl,i)
	i=i-1

AmplObsh=[]
AmplObsh=np.append(AmplObsh,Ampl)
AmplObsh=np.append(AmplObsh,Ampl2)
AmplObsh=np.append(AmplObsh,Ampl3)

PotEnObsh=[]
PotEnObsh=np.append(PotEnObsh,PotEn)
PotEnObsh=np.append(PotEnObsh,PotEn2)
PotEnObsh=np.append(PotEnObsh,PotEn3)

k1=PotEn/Ampl
k2=PotEn2/Ampl2
k3=PotEn3/Ampl3
k=[]
k=np.append(k,k1)
k=np.append(k,k2)
k=np.append(k,k3)

def linfun(x,y):
	xmean=np.mean(x)
	ymean=np.mean(y)
	xmean2=np.zeros(len(x))
	ymean2=np.zeros(len(x))
	xy=np.zeros(len(x))
	for i in range(0,len(x)):
		xmean2[i]=x[i]*x[i]
	for i in range(0,len(x)):
		ymean2[i]=y[i]*y[i]
	for i in range(0,len(x)):
		xy[i]=x[i]*y[i]
	xmean2=np.sum(xmean2)/len(x)
	ymean2=np.sum(ymean2)/len(x)
	xy=np.sum(xy)/len(x)
	a=(xmean2*ymean-xmean*xy)/(xmean2-xmean**2)
	b=(xy-xmean*ymean)/(xmean2-xmean**2)
	# return str(str(np.round(a,decimals=3))+'+'+str(np.round(b,decimals=3))+'*x')
	return a,b
	

def Koef_Kor(a,b):
	x=np.mean(a)
	y=np.mean(b)
	sumchis=0
	for i in range(0,len(a)-1):
		sumchis=sumchis+((a[i]-x)*(b[i]-y))
	sumznam1=0
	sumznam2=0
	for i in range(0,len(a)-1):
		sumznam1=sumznam1+(a[i]-x)**2
	for i in range(0,len(a)-1):
		sumznam2=sumznam2+(b[i]-y)**2
	r=(sumchis)/(np.sqrt(sumznam1)*np.sqrt(sumznam2))
	return r

r1=Koef_Kor(Ampl,PotEn)
r2=Koef_Kor(Ampl2,PotEn2)
r3=Koef_Kor(Ampl3,PotEn3)
r4=Koef_Kor(AmplObsh,PotEnObsh)

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
	# c=np.savetxt('NakopVer'+str(n)+'.txt',np.round(NakopVer,decimals=4),fmt='%.3f',delimiter=',')
	# d=np.savetxt('Inter'+str(n)+'.txt',np.round(Inter,decimals=2),fmt='%.2f',delimiter=',')
	# d=np.savetxt('KolPop'+str(n)+'.txt',np.round(KolPop,decimals=0),fmt='%.0f',delimiter=',')
	
		
	
def DovInter(n,k):
	Sred=np.mean(n)
	NormOtkl=np.std(n)
	Razmax=np.max(n)-np.min(n)
	Mediana=np.median(n)
	print('Средняя '+str(k+': ')+str(np.round(Sred,decimals=2))+'+'+str(np.round(NormOtkl,decimals=2)))
	print('Дисперсия '+str(k+': ')+str(np.round(NormOtkl,decimals=2)))
	print('Медиана '+str(k+': ')+str(np.round(Mediana,decimals=2)))
	a='Доверительный интервал '+str(k)+':'+str(np.round(Mediana-np.sqrt(NormOtkl),decimals=2))+'<m<'+str(np.round(Mediana+np.sqrt(NormOtkl),decimals=2))
	# return a

# print(DovInter(k,"для всей выборки"))
# print(DovInter(k1,"для Афганистана"))
# print(DovInter(k2,"для Китая"))
# print(DovInter(k3,"для Средней Азии"))


def ris(x,y,k,n):
	plt.figure(n)
	linvar=list(linfun(x,y))
	a=linvar[0]
	b=linvar[1]
	UrPotEn=a+b*x
	plt.plot(x,y,'ro',x,UrPotEn,'-')
	plt.xlabel('Амплитуда ВГВ, отн. ед.')
	plt.ylabel('Потенциальная энергия, Дж/кг')
	plt.title(k)
	plt.text(50,20,'E='+str(np.round(a,decimals=3))+'+'+str(np.round(b,decimals=3))+'A',rotation=0,fontsize=10)
	plt.text(50,10,'R='+str(np.round(Koef_Kor(x,y),decimals=3))+r'$\pm$',rotation=0,fontsize=10)
	plt.grid(True)
	plt.show()

	
#ris(Ampl,PotEn,'Афганистан(Вся выборка)',1)
#ris(Ampl2,PotEn2,'китай(Вся выборка)',2)
#ris(Ampl3,PotEn3,'Средняя Азия(Вся выборка)',3)
#ris(AmplObsh,PotEnObsh,'Вся выборка',4)



# print('R'+'='+str(np.round(r1,decimals=2)))
# print('Ocenka='+str(r1*np.sqrt(len(Ampl)-1)))
# print('R'+'='+str(np.round(r2,decimals=2)))
# print('Ocenka='+str(r2*np.sqrt(len(Ampl2)-1)))
# print('R'+'='+str(np.round(r3,decimals=2)))
# print('Ocenka='+str(r3*np.sqrt(len(Ampl3)-1)))
# print('R'+'='+str(np.round(r4,decimals=2)))
# print('Ocenka='+str(r4*np.sqrt(len(AmplObsh)-1)))



print(IFR(k,130,1,'Вся выборка'))
print(IFR(k1,70,2,'Афганистан'))
print(IFR(k2,50,3,'Китай'))
print(IFR(k3,40,4,'Средняя Азия'))
