#	TAREA 3 METODOS COMPUTACIONALES
# 		COD: 201615516


#_______________________________________________________________________________________________________________________________________
#Importo los paquetes necesarios

import numpy as np
import matplotlib.pylab as plt
from scipy import fftpack

#_______________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________

#Almaceno mi imagen como un arreglo numpy

imagen = plt.imread('arbol.png')

#_______________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________

FT=fftpack.fft2(imagen)
FT_shift=fftpack.fftshift(FT)
abs_FT_shift=abs(FT_shift)
log_AFS= np.log(abs_FT_shift)


plt.figure()
plt.title("Transformada de Fourier")
plt.imshow(log_AFS)
plt.savefig("MartinezSebastian_FT2D.pdf")

#_______________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________

def maximo(FT_shift):
	temp=0
	for i in range (np.shape(FT_shift)[0]):		
		for j in range (np.shape(FT_shift)[0]):
			if temp<FT_shift[i][j]:
				temp=FT_shift[i][j]
				
	return temp

pru=maximo(FT_shift)
print pru


def filtro(maximo,minimo,FT_shift):
	for i in range (np.shape(FT_shift)[0]):		
		for j in range (np.shape(FT_shift)[0]):
			if (FT_shift[i][j]>minimo and FT_shift[i][j]<maximo):
				FT_shift[i][j]=0
			else:
				FT_shift[i][j]=FT_shift[i][j]

	return FT_shift


filtrada=filtro(pru,2200,FT_shift)
FT_shift=fftpack.ifftshift(filtrada)
inv_filtrada=fftpack.ifft2(FT_shift)



plt.figure()
plt.title("Transformada de Fourier filtrada")
plt.imshow(np.log(abs(filtrada)))
plt.savefig("MartinezSebastian_FT2D_filtrada.pdf")


plt.figure()
plt.title("Imagen filtrada")
plt.imshow(abs(inv_filtrada), cmap='gray')
plt.savefig("MartinezSebastian_Imagen_filtrada.pdf")




#_______________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________


