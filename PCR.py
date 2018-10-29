#	TAREA 3 METODOS COMPUTACIONALES
# 		COD: 201615516


#_______________________________________________________________________________________________________________________________________
#Importo los paquetes necesarios

import numpy as np
import matplotlib.pylab as plt

#_______________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________

#Almaceno los datos WDBC

data_original = np.genfromtxt("WDBC.txt", delimiter= ",")
data_necesario= data_original[:,2:,]

#_______________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________

#Implemento el calculo propio de la matriz de covarianza usando la siguiente formula

#a = A - 11'A ( 1 / n )#

def matrix_covariance(datos):
    variables = np.shape(datos)[1]
    puntos = np.shape(datos)[0]
    resultado = np.ones([variables, variables])
    for i in range(variables):
        for j in range(variables):
            promedio_1 = np.mean(datos[:,i])
            promedio_2 = np.mean(datos[:,j])
            resultado[i,j] = np.sum((datos[:,i]-promedio_1) * (datos[:,j]-promedio_2))/(puntos -1.0)
    return resultado

covariance= matrix_covariance(data_necesario)
print covariance
print "___________________________________________________________________________________________________________________________"
print "___________________________________________________________________________________________________________________________"
print "___________________________________________________________________________________________________________________________"

#_______________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________

#Calculo de los eigenvalues y eigenvectors y los imprimo en mensajes 

eigenvalues, eigenvectors= np.linalg.eig(covariance)

for i in range(len(eigenvalues)):
	print "El autovalor ", eigenvalues[i], "tiene como autovector a ", eigenvectors[i]

#_______________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________

#Los parametros mas importantes


print "___________________________________________________________________________________________________________________________"
print "___________________________________________________________________________________________________________________________"
print "___________________________________________________________________________________________________________________________"
print "Los parametros mas importantes en base a mis autovectores son"

#_______________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________

#Separo mir componentes en Maligno y benigno

print "___________________________________________________________________________________________________________________________"
print "___________________________________________________________________________________________________________________________"
print "___________________________________________________________________________________________________________________________"

tipo_cancer=data_original[:,1]
print np.shape(tipo_cancer)

malignos=[]
for i in range(len(tipo_cancer)):
	if tipo_cancer[i]=='nan':
		tipo_cancer[i]=1

	
	

