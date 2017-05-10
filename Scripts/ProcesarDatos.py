import pandas as pd
import argparse

import numpy as np
from datetime import datetime

from numpy.fft import fft, ifft, rfft, irfft
from numpy import sqrt, mean, absolute

def corr(df):
    cor=df.corr()
    return pd.DataFrame({'xy': [cor['accel-x']['accel-y']],'xz':[cor['accel-x']['accel-z']], 'yz':[cor['accel-y']['accel-z']]})
def tfft(df):
     X=fft(df['accel-x'])
     Y=fft(df['accel-y'])
     Z=fft(df['accel-z'])  
     return pd.DataFrame({'x': [sum(abs(X)**2)/len(df)],'y': [sum(abs(Y)**2)/len(df)], 'z':[sum(abs(Z)**2)/len(df)]})
    
def rms_flat(a):
   
    return sqrt(mean(absolute(a)**2))    
    
def getStatisticsValues(nombre, numeroFicheros, time1=1, overlap=500):
    df_final = pd.DataFrame()
 
   
    
    for i in range(0, int (numeroFicheros)):
        df = pd.read_csv("Datos\%s-%d.csv" %(nombre, i+1), sep=';', index_col=0, error_bad_lines=False)
       
        df.index = pd.to_datetime(df.index.values, unit='ms')
        
       
        dfResampleMean = df.resample('%dL' %(overlap)).mean()
        dfRollingMean = dfResampleMean.rolling('%ds' %(time1)).mean().add_suffix("_avg")
        df_out=dfRollingMean

        dfResampleMin = df.resample('%dL' %(overlap)).min()
        dfRollingMin = dfResampleMin.rolling('%ds' %(time1)).min().add_suffix("_min")
        df_out=df_out.join(dfRollingMin)
        
        dfResampleMax = df.resample('%dL' %(overlap)).max()
        dfRollingMax = dfResampleMax.rolling('%ds' %(time1)).max().add_suffix("_max")
        df_out=df_out.join(dfRollingMax)
        
#        dfResampleVar = df.resample('%dL' %(overlap)).var()
#        dfRollingVar = dfResampleVar.rolling('%ds' %(time1)).var()
#        dfRollingVar.columns = ['var_gyro-alpha', 'var_gyro-beta', 'var_gyro-gamma', 'var_ax', 'var_ay', 'var_az']
      

        
        
        dfResampleStd = df.resample('%dL' %(overlap)).std()
        dfRollingStd = dfResampleStd.rolling('%ds' %(time1)).std().add_suffix("_std")
        df_out=df_out.join(dfRollingStd)
       
        dfResampleCor=df.groupby(pd.TimeGrouper('%dL' %(overlap))).apply(corr).reset_index(1,drop=True).add_suffix("_cor")       
        df_out=df_out.join(dfResampleCor)
       
        
        dfResamplefft=df.groupby(pd.TimeGrouper('%dL' %(overlap))).apply(tfft).reset_index(1,drop=True).add_suffix("_fft")
        df_out=df_out.join(dfResamplefft)
        
        
        dfResampleMed = df.resample('%dL' %(overlap)).median()
        dfRollingMed = dfResampleMed.rolling('%ds' %(time1)).median().add_suffix("_med")
        df_out=df_out.join(dfRollingMed)
      
        
        

       
        df_final=df_final.append(df_out)
     
    df_final=df_final.fillna(df_final.mean())
    fecha = datetime.now().microsecond
   
    df_final.to_csv("val/%s-procesado-%s.csv" %(nombre, fecha), ';')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract features from inputFile and save them in outputFile')

    parser.add_argument("i",
                        help="File/s to be analyzed")
    parser.add_argument("n",
                        help="Number of files")
    parser.add_argument("-t", "--time", help="Time of window, i.e.= 1 second",
                    default=1)
    parser.add_argument("-o", "--overlap", help="overlap || 500ms -> 50.00perc verlap",
                    default=500)
    args = parser.parse_args()

    getStatisticsValues(args.i, args.n, args.time, args.overlap)
