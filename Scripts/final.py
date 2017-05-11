# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 18:56:06 2017


"""
import pandas as pd
import os.path 
from os import walk
def numeroActividad(actividad):
    numero = 0

    if(actividad=="andar"):
        numero=1
    elif(actividad=="escaleras"):
        numero=2
    elif(actividad=="quieto"):
        numero=3
    elif(actividad=="barrer"):
        numero=4
  
    return numero
                
    
    

def juntar():
     dfOutX = pd.DataFrame()
     dfOutY = pd.DataFrame()
     dfOutI = pd.DataFrame()
    
     directorioActual=os.getcwd()
     
     for (path, ficheros, archivos) in walk("./movil2"):
        for i in  archivos:
            print(i)
            actividada=i.split('_')
           # actividad2=actividada.spilt('-');
            actividad=actividada[1]
            
            os.chdir(directorioActual+"/movil2")
            dfX=pd.DataFrame()
            dfX = pd.read_csv(i, sep=';', index_col=0, error_bad_lines=False)
           
            os.chdir(directorioActual)
            numero=numeroActividad(actividad)
           
            numeroFilas=len(dfX)
            
            dfY=pd.DataFrame()
            lista=list()
            
            dfI=pd.DataFrame()
            listaInformacion=list()
            indices=dfX.index.tolist()  
            
           
            d=0
            for d in range(numeroFilas):
                lista.append(numero)
                dfX.index.tolist()
                listaInformacion.append(actividada[0])
                
            dfY=pd.DataFrame(lista)
            dfI=pd.DataFrame(listaInformacion)
          
            dfOutX = pd.concat([dfOutX, dfX])
            dfOutY = pd.concat([dfOutY, dfY])
            dfOutI = pd.concat([dfOutI, dfI])
     os.chdir(directorioActual)
     dfOutX.to_csv("X_train_movil5.csv",header=None, index=False)
     dfOutY.to_csv("y_train_movil5.csv",header=None, index=False)
     #dfOutI.to_csv("info_X_val_movil2.csv",header=None, index=False)
            
if __name__ == "__main__":
    juntar()
            
        
    