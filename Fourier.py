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
plt.xlabel("Frecuencia")
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

filtros = filtro_bajos(frecuencia,filtro)

plt.figure()
plt.title("Transformada discreta de Fourier con Filtrado")
plt.plot(filtros, abs(DFT))
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


f_cubica= Spline_Interpolation(signal_x,signal_y,cubica, minimo_x, maximo_x, n_puntos)
x_cubica= f_cubica[0]
y_cubica= f_cubica[1]





#_______________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________



