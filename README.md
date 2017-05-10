# Analisis-actividades

## Datos
Se encuentran los datos recogidos para hacer las pruebas,se dividen en movil y pulsera.
En la pulsera los datos son recogidos de 4 personas y se realizan 5 actividades: Andar,barrer,estar de pie,subir y bajar escaleras.
En el movil los datos de 13 personas y 4 actividades: barrer, estar quieto, escaleras y andar

## Informe
* **Informe con cross-validation**: Los datos sson los recogidos desde la pulsera,las medidas utilizadas son:media,varianza,desviacion,
                                     mediana,maximo y minimo.
* **Informe con ftt,corr**:Los datos son recogidos por la pulsera,se añaden dos medidas nuevas fft y corr en los acelerometros.
                          Los datos se dividen antes de procesarlos en train y validación.
 ## Script
 * **llamadaAProcesar**: Llama al script ProcesarDatos.py con todos los archivos que se encuentren en la carpeta
 * **ProcesarDatos** : Hace una segmentación de los datos en ventanas y calculas las métricas.
 * **Final** : Une todos los archivos procesados para generar el fichero para entrenamiento.

