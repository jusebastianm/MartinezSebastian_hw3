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
datas=np.genfromtxt("WDBC.txt", delimiter= ",", dtype='U16')
data_necesario= data_original[:,2:,]

#_______________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________

#Implemento el calculo propio de la matriz de covarianza usando la siguiente formula



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

#Separo mis componentes en Maligno y benigno

print "___________________________________________________________________________________________________________________________"
print "___________________________________________________________________________________________________________________________"
print "___________________________________________________________________________________________________________________________"



tipo_cancer=datas[:,1]
index_tipo=data_original[:,0]
malignos_index=[]
benignos_index=[]
for i in range(len(tipo_cancer)):
	if tipo_cancer[i]==u'M':
		malignos_index.append(i)
	else:
		benignos_index.append(i)

malignos_y=[]
malignos_x=[]
benignos_x=[]
benignos_y=[]
for i in range(len(malignos_index)):
	malignos_y.append(data_necesario[malignos_index[i]])
	malignos_x.append(index_tipo[malignos_index[i]])
	benignos_y.append(data_necesario[benignos_index])
	benignos_x.append(index_tipo[benignos_index])


print malignos_y





