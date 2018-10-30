#	TAREA 3 METODOS COMPUTACIONALES
# 		COD: 201615516


#_______________________________________________________________________________________________________________________________________
#Importo los paquetes necesarios

import numpy as np
import matplotlib.pylab as plt
from scipy.fftpack import fft, fftfreq
import math
from scipy import interpolate 
e=math.e
pi=np.pi


#_______________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________

#Importo los datos de signal e incompletos

signal = np.genfromtxt("signal.dat", delimiter= ",")
incompletos = np.genfromtxt("incompletos.dat", delimiter= ",")

#Separo las columnas en arrays
signal_x= signal[:,0]
signal_y= signal[:,1]


#_______________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________

#Grafico signal
plt.figure()
plt.title("Signal")
plt.xlabel("Tiempo (s)")
plt.ylabel("Frecuencia ")
plt.plot(signal_x,signal_y)
plt.savefig("MartinezSebastian_signal.pdf")

#_______________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________

#Aplicacion de la transformada discreta de Fourier

N=len(signal_x)
dt=signal_x[1]-signal_x[0]
frecuencia= fftfreq(N,dt)
DFT= np.linspace(0,0,N)

for i in range(N):
	for j in range(len(DFT)):
		DFT[i] = DFT[i] + (signal_y[j]*(e**((-1j)*2*pi*j*i/N)))
		

plt.figure()
plt.plot(frecuencia, abs(DFT)/N)
plt.title("Transformada discreta de Fourier")
plt.xlabel("Frecuencia")
plt.ylabel("DFT")
plt.savefig("MartinezSebastian_TF.pdf")

#_______________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________
#Mensaje

print "___________________________________________________________________________________________________________________"
print "___________________________________________________________________________________________________________________"
print "___________________________________________________________________________________________________________________"

print "Las frecuencias principales de mi signal son"



#_______________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________

#Filtro de frecuencias



data_filtro=[]

def filtro_bajos(FT, filtro):
	for i in range(len(FT)):
		if FT[i] < filtro:
			data_filtro.append(FT[i])
		if FT[i] >= filtro:
			FT[i] = 0
			data_filtro.append(FT[i])
	return data_filtro

filtros = filtro_bajos(frecuencia,1000)

plt.figure()
plt.title("Transformada discreta de Fourier con Filtrado")
plt.plot(filtros, abs(DFT))
plt.xlabel("Frecuencia")
plt.ylabel("DFT")
plt.xlim(-1000,1000)
plt.savefig("MartinezSebastian_filtrada.pdf")



#_______________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________

print "___________________________________________________________________________________________________________________"
print "___________________________________________________________________________________________________________________"
print "___________________________________________________________________________________________________________________"

print "No puede hacer la transformada de Fourier de los datos porque"

#_______________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________


minimo_x= min(signal_x)
maximo_x=max(signal_x)

cuadratica='quadratic'
cubica='cubic'
	
n_puntos=512


#Defino mi funcion donde me retorna un array de datos interpolados en x y y

def Spline_Interpolation(x,y,tipo, minimo, maximo, n):
	f_interpolated= interpolate.interp1d(x, y, kind=tipo)
	x_interpolated= np.linspace(minimo,maximo, n)
	data_interpolated= np.array([x_interpolated, f_interpolated(x_interpolated)])
	return data_interpolated

f_cuadratica= Spline_Interpolation(signal_x,signal_y,cuadratica, minimo_x, maximo_x, n_puntos)
x_cuadratica=f_cuadratica[0]
y_cuadratica=f_cuadratica[1]
dt_cuadra=x_cuadratica[1]-x_cuadratica[0]
frecuencia_cuadra= fftfreq(n_puntos,dt_cuadra)
DFT_cuadra=np.linspace(0,0,n_puntos)
for i in range(N):
	for j in range(len(DFT_cuadra)):
		DFT_cuadra[i] = DFT_cuadra[i] + (y_cuadratica[j]*(e**((-1j)*2*pi*j*i/n_puntos)))


f_cubica= Spline_Interpolation(signal_x,signal_y,cubica, minimo_x, maximo_x, n_puntos)
x_cubica= f_cubica[0]
y_cubica= f_cubica[1]
dt_cubica=x_cubica[1]-x_cubica[0]
frecuencia_cubica= fftfreq(n_puntos,dt_cubica)
DFT_cubica=np.linspace(0,0,n_puntos)
for i in range(N):
	for j in range(len(DFT_cubica)):
		DFT_cubica[i] = DFT_cubica[i] + (y_cubica[j]*(e**((-1j)*2*pi*j*i/n_puntos)))
plt.figure()
f, (ax1,ax2,ax3)= plt.subplots(3,sharex=True,sharey=True)
plt.xlabel("Frecuencia")
plt.ylabel("DFT")
ax1.set_title("Transformadas discretas de Fourier")
ax1.plot(frecuencia, abs(DFT)/N, color='r', label="Signal DFT")
ax2.plot(frecuencia_cuadra,abs(DFT_cuadra)/n_puntos, color='darkblue',label="Signal cuadratic DFT")
ax3.plot(frecuencia_cubica,abs(DFT_cubica)/n_puntos, color='c', label="Signal cubic DFT")
ax1.legend(loc=0)
ax2.legend(loc=0)
ax3.legend(loc=0)
plt.savefig("MartinezSebastian_TF_interpola.pdf")
#_______________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________


print "___________________________________________________________________________________________________________________"
print "___________________________________________________________________________________________________________________"
print "___________________________________________________________________________________________________________________"

print "las diferencias encontradas entre la transformada de Fourier de la signal original y las de las interpolaciones son que las frecuencias positivamente mas grandes se alcanzan a distinguir con las interpolaciones, mientras que con la orginal no"


#_______________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________

data_filtro_2=[]
def filtro_bajos_2(FT, filtro):
	for i in range(len(FT)):
		if FT[i] < filtro:
			data_filtro_2.append(FT[i])
		if FT[i] >= filtro:
			FT[i] = 0
			data_filtro_2.append(FT[i])
	return data_filtro_2

#_______________________________________________________________________________________________________________________________________
data_filtro_cuadra=[]
def filtro_bajos_cuadra(FT, filtro):
	for i in range(len(FT)):
		if FT[i] < filtro:
			data_filtro_cuadra.append(FT[i])
		if FT[i] >= filtro:
			FT[i] = 0
			data_filtro_cuadra.append(FT[i])
	return data_filtro_cuadra

data_filtro_cuadra_2=[]
def filtro_bajos_cuadra_2(FT, filtro):
	for i in range(len(FT)):
		if FT[i] < filtro:
			data_filtro_cuadra_2.append(FT[i])
		if FT[i] >= filtro:
			FT[i] = 0
			data_filtro_cuadra_2.append(FT[i])
	return data_filtro_cuadra_2
#_______________________________________________________________________________________________________________________________________

#_______________________________________________________________________________________________________________________________________
data_filtro_cubica=[]
def filtro_bajos_cubica(FT, filtro):
	for i in range(len(FT)):
		if FT[i] < filtro:
			data_filtro_cubica.append(FT[i])
		if FT[i] >= filtro:
			FT[i] = 0
			data_filtro_cubica.append(FT[i])
	return data_filtro_cubica

data_filtro_cubica_2=[]
def filtro_bajos_cubica_2(FT, filtro):
	for i in range(len(FT)):
		if FT[i] < filtro:
			data_filtro_cubica_2.append(FT[i])
		if FT[i] >= filtro:
			FT[i] = 0
			data_filtro_cubica_2.append(FT[i])
	return data_filtro_cubica_2

#_______________________________________________________________________________________________________________________________________




filtros_cuadra = filtro_bajos_cuadra(frecuencia_cuadra,1000)
filtros_cubica = filtro_bajos_cubica(frecuencia_cubica,1000)



filtros_original_2 = filtro_bajos_2(frecuencia,500)
filtros_cuadra_2 = filtro_bajos_cuadra_2(frecuencia_cuadra,500)
filtros_cubica_2 = filtro_bajos_cubica_2(frecuencia_cubica,500)



plt.figure()
f, (ax1,ax2)= plt.subplots(2,sharex=True,sharey=True)
plt.xlim(-1000,1000)
plt.xlabel("Frecuencia")
plt.ylabel("DFT")
ax1.set_title("Transformadas discretas de Fourier con filtros de 500 HZ")
ax1.plot(filtros_original_2, abs(DFT), color='r', label="Signal DFT")
ax1.plot(filtros_cuadra_2, abs(DFT_cuadra)/n_puntos, color='darkblue',linestyle='-.', label="Signal cuadratic DFT")
ax1.plot(filtros_cubica_2, abs(DFT_cubica)/n_puntos, color='c',linestyle='--', label="Signal cubic DFT")
ax1.legend(loc=0)

ax2.set_title("Transformadas discretas de Fourier con filtros de 1000 HZ")
ax2.plot(filtros, abs(DFT), color='r', label="Signal DFT")
ax2.plot(filtros_cuadra, abs(DFT_cuadra)/n_puntos, color='darkblue',linestyle='-.', label="Signal cuadratic DFT")
ax2.plot(filtros_cubica, abs(DFT_cubica)/n_puntos, color='c', linestyle='--',label="Signal cubic DFT")
ax2.legend(loc=0)
plt.savefig("MartinezSebastian_2Filtros.pdf")


