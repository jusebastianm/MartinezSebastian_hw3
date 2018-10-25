import numpy as np
import matplotlib.pylab as plt
from scipy.fftpack import fft, fftfreq
import math

e=math.e
pi=np.pi

#Importo los datos de signal e incompletos
signal = np.genfromtxt("signal.dat", delimiter= ",")
incompletos = np.genfromtxt("incompletos.dat", delimiter= ",")

#Separo las columnas en arrays
signal_x= signal[:,0]
signal_y= signal[:,1]


#Grafico signal
plt.figure()
plt.title("Signal")
plt.xlabel("Frecuencia")
plt.ylabel("Amplitud")
plt.plot(signal_x,signal_y)
plt.savefig("MartinezSebastian_signal.pdf")

#Fourier para signal
N = len(signal_x)
f=[]
dt=[]
t=[]
for i in range(len(signal_x)):
	f.append(signal_x[i])
	dt.append(1/(f[i]*32))
	t.append((N-1)*dt[i])

DFT= np.linspace(0,0,N)
for i in range(N):
	for j in range(len(t)):
		DFT[i]= DFT[i]+ (signal_y[j]*e**((-1j)*2*pi*j*i/N))

#Grafica Fourier para signal
plt.figure()
plt.title("Transformada de Fourier")
plt.xlabel("Frecuencia")
plt.ylabel("Amplitud")
plt.plot(signal_x,DFT)
plt.savefig("MartinezSebastian_TF.pdf")

#Prueba

#fft_x=fft(signal_y)/N # FFT Normalized
#freq=[]
#for i in range(len(dt)):
#	freq.append(fftfreq(N, dt[i]))

#plt.figure()
#plt.title("Prueba")
#plt.xlabel("x")
#plt.ylabel("y")
#plt.plot(freq,fft_x)
#plt.savefig("prueba.pdf")


#Mensaje

print "Las frecuencias principales de mi signal son"

#Filtro pasa bajos


filtro = 1000.0 #Hz

data_filtro=[]
def filtro_bajos(FT, filtro):
	for i in range(len(FT)):
		if FT[i] < filtro:
			data_filtro.append(FT[i])
		if FT[i] >= filtro:
			FT[i] = 0
			data_filtro.append(FT[i])
	return data_filtro

filtro_data= filtro_bajos(signal_y,filtro)
plt.figure()
plt.title("Filtro pasa bajos")
plt.xlabel("Frecuencia")
plt.ylabel("Amplitud")
plt.plot(signal_x,filtro_data)
plt.savefig("MartinezSebastian_filtrada.pdf")



