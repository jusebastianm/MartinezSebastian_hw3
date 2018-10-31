#	TAREA 3 METODOS COMPUTACIONALES
# 		COD: 201615516


#_______________________________________________________________________________________________________________________________________
#Importo los paquetes necesarios

import numpy as np
import matplotlib.pylab as plt
from scipy.fftpack import fft, fftfreq, ifft
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
plt.ylabel("y (t) ")
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
plt.xlabel("Frecuencias")
plt.ylabel("DFT")
plt.savefig("MartinezSebastian_TF.pdf")

#_______________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________
#Mensaje

print "___________________________________________________________________________________________________________________"
print "___________________________________________________________________________________________________________________"
print "___________________________________________________________________________________________________________________"

frec_prin=[]
for i in range(len(frecuencia)):
	if (abs(DFT[i])/N)>0.65:
		frec_prin.append(frecuencia[i])
print "Las frecuencias principales de mi signal son", frec_prin, "que son donde se presentan los picos mas altos de mi transformada de Fourier"

print "___________________________________________________________________________________________________________________"
print "___________________________________________________________________________________________________________________"
print "___________________________________________________________________________________________________________________"


#_______________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________

#Filtro de frecuencias

def filtro_bajos(FT, filtro, transfor):
	frec_filtrada=[]
	for i in range(len(FT)):
		if (abs(FT[i]) > filtro):
			transfor[i]=0
			frec_filtrada.append(transfor[i])
		else:	
			frec_filtrada.append(transfor[i])
	return frec_filtrada


prueba= filtro_bajos(frecuencia,1000.0, (DFT))
inv= ifft(prueba)
plt.figure()
plt.title("Transformada discreta de Fourier con Filtrado")
plt.plot(signal_x,inv)
plt.xlabel("Frecuencia")
plt.ylabel("Inversa DFT")
plt.savefig("MartinezSebastian_filtrada.pdf")



#_______________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________

print "___________________________________________________________________________________________________________________"
print "___________________________________________________________________________________________________________________"
print "___________________________________________________________________________________________________________________"

print "No puede hacer la transformada de Fourier de los datos porque mi delta de tiempo (espaciado en x) no es constante para todo el arreglo haciendo que se generen huecos en la transformada."


print "___________________________________________________________________________________________________________________"
print "___________________________________________________________________________________________________________________"
print "___________________________________________________________________________________________________________________"

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
for i in range(n_puntos):
	for j in range(len(DFT_cuadra)):
		DFT_cuadra[i] = DFT_cuadra[i] + (y_cuadratica[j]*(e**((-1j)*2*pi*j*i/n_puntos)))


f_cubica= Spline_Interpolation(signal_x,signal_y,cubica, minimo_x, maximo_x, n_puntos)
x_cubica= f_cubica[0]
y_cubica= f_cubica[1]
dt_cubica=x_cubica[1]-x_cubica[0]
frecuencia_cubica= fftfreq(n_puntos,dt_cubica)
DFT_cubica=np.linspace(0,0,n_puntos)
for i in range(n_puntos):
	for j in range(len(DFT_cubica)):
		DFT_cubica[i] = DFT_cubica[i] + (y_cubica[j]*(e**((-1j)*2*pi*j*i/n_puntos)))

plt.figure()
f, (ax1,ax2,ax3)= plt.subplots(3,sharex=True,sharey=True)
plt.xlabel("Frecuencia")

ax1.set_title("Transformadas discretas de Fourier")
ax1.plot(frecuencia, abs(DFT)/N, color='r', label="Signal DFT")
ax2.plot(frecuencia_cuadra,abs(DFT_cuadra)/n_puntos, color='darkblue',label="Signal cuadratic DFT")
plt.ylabel("DFT")
ax3.plot(frecuencia_cubica,abs(DFT_cubica)/n_puntos, color='c', label="Signal cubic DFT")
ax1.legend(loc=0)
ax2.legend(loc=0)
ax3.legend(loc=0)
plt.xlim(-1000,1000)
plt.savefig("MartinezSebastian_TF_interpola.pdf")
#_______________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________


print "___________________________________________________________________________________________________________________"
print "___________________________________________________________________________________________________________________"
print "___________________________________________________________________________________________________________________"

print "las diferencias encontradas entre la transformada de Fourier de la signal original y las de las interpolaciones son que la original tiene algunos picos mas notorios o sobresalientes respecto a las interpolaciones. Esto se ve justificado en mejora del espaciado en el arreglo que refleja cada una de las interpolaciones."


print "___________________________________________________________________________________________________________________"
print "___________________________________________________________________________________________________________________"
print "___________________________________________________________________________________________________________________"


#_______________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________





filtros_cuadra = filtro_bajos(frecuencia_cuadra,1000, DFT_cuadra)
filtros_cubica = filtro_bajos(frecuencia_cubica,1000, DFT_cubica)



filtros_original_2 = filtro_bajos(frecuencia,500, DFT)
filtros_cuadra_2 = filtro_bajos(frecuencia_cuadra,500, DFT_cuadra)
filtros_cubica_2 = filtro_bajos(frecuencia_cubica,500, DFT_cubica)


plt.figure()
f, (ax1,ax2)= plt.subplots(2,sharex=True,sharey=True)
plt.xlim(-1000,1000)
plt.xlabel("Frecuencia")
plt.ylabel("Inversa DFT")
ax1.set_title("Transformadas discretas de Fourier con filtros de 500 HZ")
ax1.plot(signal_x, ifft(filtros_original_2), color='r',marker="*", label="Signal DFT")
ax1.plot(x_cuadratica, ifft(filtros_cuadra_2), color='darkblue', label="Signal cuadratic DFT")
ax1.plot(x_cubica, ifft(filtros_cubica_2), color='c',linestyle='--', label="Signal cubic DFT")
ax1.legend(loc=0)
plt.xlim(min(signal_x),max(signal_x))
ax2.set_title("Transformadas discretas de Fourier con filtros de 1000 HZ")
ax2.plot(signal_x, inv, color='r',marker="*",label="Signal DFT")
ax2.plot(x_cuadratica, ifft(filtros_cuadra), color='darkblue', label="Signal cuadratic DFT")
ax2.plot(x_cubica, ifft(filtros_cubica), color='c', linestyle='--',label="Signal cubic DFT")
ax2.legend(loc=0)

plt.savefig("MartinezSebastian_2Filtros.pdf")


