README.txt
=============================
Guía de ejecución del proyecto
=============================

Este proyecto está compuesto por varios notebooks que implementan el flujo completo de análisis y modelado de datos.
El orden de ejecución recomendado es el siguiente:

1️-ETL (Extracción, Transformación y Carga)
--------------------------------------------
Ejecuta los notebooks denominados como ETL en cualquier entorno Jupyter.

Orden sugerido:
1. ETL-Orders.ipynb
2. ETL-Holidays.ipynb
3. ETL-Football.ipynb
4. ETL-Euribor.ipynb
5. ETL-Climate.ipynb

Estos notebooks limpian, transforman y preparan las distintas fuentes de datos necesarias para el análisis posterior.
Vuelcan los dataframes resultantes en la carpeta "raw data".

2️-EDA (Exploratory Data Analysis)
-----------------------------------
Una vez completado el proceso ETL, ejecuta el notebook TFM-EDA.ipynb.
Este notebook toma los dataframes de la carpeta "raw data".
Aquí se realiza un análisis exploratorio de los datos combinados para averiguar los insights.
Se finaliza guardando el dataset post-EDA en la carpeta "clean data".

3️-Preprocesamiento, Modelado y Evaluación
-------------------------------------------
Por último, ejecuta:
- TFM-Preprocess-Model-Evaluate.ipynb.

Este notebook utiliza los datos procesados post-EDA de "clean data" para:
- Aplicar preprocesamiento final.
- Entrenar modelos de Machine Learning.
- Evaluar su rendimiento y generar resultados finales.

💡 Notas:
---------
- Asegúrate de tener todas las dependencias y rutas de datos configuradas antes de ejecutar los notebooks.
- Si los archivos están en formato .html, puedes visualizarlos directamente en un navegador o convertirlos a .ipynb si deseas ejecutarlos en Jupyter Notebook.
- En caso de haber perdido algún .csv, las carpetas "backup raw data" y "backup clean data" contienen todo lo necesario
para la reejecución. Solo hay que copiar el contenido a los directorios correspondientes.
- ETL-Orders.ipynb y ETL-Climate.ipynb utilizan requieren dos directorios adicionales: "datos pedidos" contiene los informes de pedidos
para la extracción; "datos metereologicos" contiene archivos parciales de datos climatológicos (antes de fusionarse en "raw data").