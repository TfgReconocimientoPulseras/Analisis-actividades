import os, os.path
from os import walk
import ProcesarDatos


j = 0;
for (path, ficheros, archivos) in walk("./Ficheros"):
	for i in  archivos:
		if (j % 3 == 0):
			nombre = i.split('-')
			persona = nombre[0]
			actividad = nombre[1]
			ProcesarDatos.getStatisticsValues(('%s-%s' %(persona, actividad)), 3)
		j = j + 1;


os.unlink('ProcesarDatos.pyc')
