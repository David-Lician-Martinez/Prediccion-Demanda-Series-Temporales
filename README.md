# Prediccion de la Demanda en Servicios de Reparto

Proyecto de ciencia de datos orientado a predecir la demanda semanal de un negocio hostelero mediante series temporales, con resolucion de 30 minutos y especial atencion a la distribucion horaria de los pedidos.

## Objetivo de negocio

Ayudar a la planificacion operativa de una empresa de reparto y recogida de comida optimizando:

- la elaboracion de horarios del personal
- la asignacion de recursos por franja horaria
- la preparacion de stock en funcion de la demanda esperada

## Objetivo tecnico

Construir y comparar modelos capaces de predecir una semana completa de demanda con al menos una semana de antelacion, incorporando variables internas del negocio y senales externas como festivos, futbol, meteorologia y euribor.

## Fuentes de datos

- Informes internos de pedidos en PDF, agregados por intervalos de 15 minutos.
- Festivos oficiales y locales obtenidos mediante scraping y reglas manuales para eventos especificos.
- Calendario de partidos de futbol obtenido desde la API publica/semi-publica de LaLiga.
- Euribor diario obtenido desde la API del Banco de Espana.
- Datos meteorologicos horarios obtenidos desde la API SIAR.

Cobertura temporal principal: `2024-01-01` a `2025-05-25`.

## Estructura del repositorio

```text
.
|- configs/
|  `- config.yaml
|- data/
|  |- archive/
|  |  |- processed_backup/
|  |  `- raw_backup/
|  |- external/
|  |  `- orders_reports/
|  |- interim/
|  |  `- weather_parts/
|  |- processed/
|  `- raw/
|- docs/
|- models/
|- notebooks/
|- reports/
|  |- figures/
|  `- html/
|- src/
|  `- utils.py
|- .gitignore
|- requirements.txt
`- README.md
```

## Flujo de trabajo

### 1. ETL de fuentes

Los notebooks ETL generan los CSV base en `data/raw/`:

- `ETL-Orders.ipynb`: extrae pedidos desde PDFs fuente.
- `ETL-Holidays.ipynb`: construye el calendario de festivos.
- `ETL-Football.ipynb`: descarga y normaliza partidos relevantes.
- `ETL-Euribor.ipynb`: obtiene la serie diaria del euribor.
- `ETL-Climate.ipynb`: consolida los datos horarios de clima.

### 2. EDA e integracion

`TFM-EDA.ipynb` integra las fuentes de `data/raw/`, realiza el analisis exploratorio y genera los datasets post-EDA en `data/processed/`.

Principales salidas:

- `df_combined.csv`
- `df_weather.csv`
- `df_holidays.csv`
- `df_football.csv`
- `df_major_matches.csv`

### 3. Preprocesamiento, modelado y evaluacion

`TFM-Preprocess-Model-Evaluate.ipynb` consume `data/processed/` y compara modelos de:

- gradient boosting y random forests
- redes neuronales recurrentes
- modelos clasicos de series temporales
- baselines naive
- un modelo hibrido `Naive + LightGBM`

## Resultados clave

Segun las conclusiones recogidas en los notebooks:

- El enfoque hibrido `Naive + LightGBM` ofrece el mejor equilibrio entre precision y consistencia.
- Las senales meteorologicas y macroeconomicas aportan valor predictivo limitado frente a las variables internas del negocio, festivos y futbol.
- La validacion temporal con ventanas crecientes mejora la robustez de la comparacion entre modelos.

## Como navegar o ejecutar el proyecto

1. Revisa `notebooks/README.md` para el orden de ejecucion recomendado.
2. Ejecuta los notebooks ETL si necesitas regenerar los CSV de `data/raw/`.
3. Ejecuta `notebooks/TFM-EDA.ipynb` para reconstruir `data/processed/`.
4. Ejecuta `notebooks/TFM-Preprocess-Model-Evaluate.ipynb` para el entrenamiento y evaluacion final.

Notas practicas:

- Los notebooks son la fuente de verdad del flujo analitico; no se han convertido a scripts de forma agresiva.
- Los HTML en `reports/html/` sirven como documentacion visual, no como artefactos ejecutables.
- `data/archive/` conserva snapshots de seguridad de los CSV originales del proyecto.
- Algunos ETL dependen de APIs externas y pueden requerir conectividad o credenciales validas.

## Dependencias

Consulta `requirements.txt` para un listado base de librerias utilizadas en el proyecto.
