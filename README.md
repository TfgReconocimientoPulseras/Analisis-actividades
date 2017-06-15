# Analisis-actividades
En este repositorio se encuentran los ficheros utilizados para el análisis de datos y la construcción de los árboles de decisiones.

## Datos
* **Datos_train**: Datos recogidos para ser usados en la fase de entrenamiento.
* **Datos_val**: Datos recogidos para ser usadis en la fase de validación.
* **DatosMovil**: Datos recogidos directamente desde el móvil.

## Documentos
* **caracteristicas.txt**: Nos indica las características utilizadas para el reconomiento de actividades.
* **clases.txt**: Las actividades que se reconocen.
* **ifelse_codigo.txt**: Conjunto de "if-else" que se implementa en la app para el reconocimiento de las actividades.

## Informes
* **Informe con cross-validation**: Los datos son los recogidos desde la pulsera,las medidas utilizadas son: media, varianza, desviacion,mediana, máximo y mínimo.
* **Informe con ftt,corr**: Los datos son recogidos por la pulsera,se añaden dos medidas nuevas fft y corr en los acelerometros. Los datos se dividen antes de procesarlos en train y validación.
* **Movil**: Datos recogidos con el movil,nuevas metricas añadidas:media de la fft,fft de scipy,skew,desviacion de la fft,suma de la fft..ect.Se realizan tres prubas: 12 personas de train y 1 de validación
 
 ## Scripts
 * **ProcesarDatos**: Hace una segmentación de los datos en ventanas y calcula las métricas.
 * **llamadaAProcesar**: Llama al script ProcesarDatos.py con todos los archivos que se encuentren en la carpeta
 * **Final**: Une todos los archivos procesados para generar el fichero para entrenamiento.
 * **codigoArbol**: Crear un árbol con los datos de entrenamiento y devuelve el código de "if-elses" para implementar en la app.
 * **codigoClaseJava**: Variante del script codigoArbol. Este script devuelve un string que representa una clase java y dentro de la clase contiene el codigo con los "if-else" que representan el arbol de decisiones.
 * **mejoresParametrosArbol**: Script que comprueba que valores son los más adecuados para los parámetros min_samples_split y min_samples_leaf, para contruir el árbol de decisiones y que tenga mayor exactitud.
