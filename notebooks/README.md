# Notebooks

Los notebooks siguen siendo el artefacto principal del proyecto. La secuencia recomendada es:

1. `ETL-Orders.ipynb`
2. `ETL-Holidays.ipynb`
3. `ETL-Football.ipynb`
4. `ETL-Euribor.ipynb`
5. `ETL-Climate.ipynb`
6. `TFM-EDA.ipynb`
7. `TFM-Preprocess-Model-Evaluate.ipynb`

Notas importantes:

- Los archivos HTML equivalentes viven en `reports/html/` y son solo de referencia visual.
- Los datos crudos generados por los ETL se guardan en `data/raw/`.
- Los datasets post-EDA se guardan en `data/processed/`.
- Los PDFs de pedidos fuente estan en `data/external/orders_reports/`.
- Las particiones climatologicas intermedias estan en `data/interim/weather_parts/`.
- `data/archive/` conserva copias de seguridad de los CSV originales del proyecto.
