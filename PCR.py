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

print "___________________________________________________________________________________________________________________________"
print "___________________________________________________________________________________________________________________________"
print "___________________________________________________________________________________________________________________________"
print "Mi matriz de covarianza es la siguiente"
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
print "Los parametros mas importantes en base a mis autovectores son los que tienen direccion positiva ya que se ve una tendencia a crecer en el componente prinicpal 1"

#_______________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________

#Separo mis componentes en Maligno y benigno

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
benignos_y=[]
for i in range(len(malignos_index)):
	malignos_y.append(data_necesario[malignos_index[i]])
	benignos_y.append(data_necesario[benignos_index[i]])



mal = np.matmul(malignos_y,eigenvectors)
bien = np.matmul(benignos_y,eigenvectors)

plt.figure()
plt.scatter(mal[:,0],mal[:,1], label="Malignos", color='r')
plt.scatter(bien[:,0],bien[:,1], label="Benignos", color='g', marker='*')
plt.title("Analisis de componentes principales para un tipo de Cancer")
plt.legend(loc=0)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.savefig("MartinezSebastian_PCA.pdf")

#_______________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________

#Los parametros mas importantes

print "___________________________________________________________________________________________________________________________"
print "___________________________________________________________________________________________________________________________"
print "___________________________________________________________________________________________________________________________"
print "El analisis de componentes principales (PCA) es util en este caso porque permite mostrar los datos variables de manera que no esten correlacionados entre si y ademas disminuye la dimension y redundancia del mismo conjunto de datos. De esta forma, es posible diagnosticar a un paciente tomando en cuenta el grafico realizado en el punto anterior ya que en el, los pacientes con cancer benigno nunca se veran correlacionados con de cancer maligno. "



