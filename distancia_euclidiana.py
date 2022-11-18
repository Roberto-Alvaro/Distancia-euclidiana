from multiprocessing.resource_sharer import stop
from tracemalloc import start
import pandas as pd # Importacion estandar de la libreria Pandas
import numpy  as np # Importacion estandar de la libreria NumPy
from scipy.spatial import distance_matrix
from scipy.stats import zscore

def evaluacionAmbito(df):
    print("-------------------Evalucion del ambito-------------------")
    decena = False
    centena = False
    milesimas = False

    for key in df:
        for val in df[key]:
            if val in range(0, 99):
                decena = True
            if val in range(100, 999):
                centena = True
            if val in range(1000, 9999):
                milesimas = True

    if decena and centena:
        return True
    elif decena and milesimas:
        return True
    elif centena and milesimas:
        return True
    else:
        return False

def calculoMatrixDistan(ruta):
    df = pd.read_excel(ruta, sheet_name = 'Hoja1')
    print(df)
    archivo_lista = []
    filas, columnas = df.shape

    if(filas <= 256 and columnas <= 30):
        print("Exito, su tabla de datos es aceptada, en su tamaño")
        ambito = evaluacionAmbito(df)
        if(ambito == True):
            print("-------------------Puntacion Z-------------------")
            datos = df.values
            punt_z = zscore(datos)
            result = pd.DataFrame(distance_matrix(punt_z, punt_z, p=2)) #Distancia euclidiana
            #print(result)
            return result
        else:
            #ojo distancia
            result = pd.DataFrame(distance_matrix(df.values, df.values), index=df.index, columns=df.index) #Distancia euclidiana
            #print("Tu distancia euclidiana: \n", result)
            return result
    else:
        print("error")
        print("Su numero de registros, supera a 256: ", filas)
        print("Su numero de variables, supera a 30: ", columnas)

ruta = ("C:/Users/espar/Desktop/Algoritmos-agrupamiento/Libro1.xlsx")
result  = calculoMatrixDistan(ruta)

try:
    result.to_excel('C:/Users/espar/Desktop/Algoritmos-agrupamiento/resultado.xlsx', index=False)
except:
    print("")
#result.to_csv('C:/Users/espar/Desktop/Algoritmos-agrupamiento/resultado.txt', sep='|') #En txt
