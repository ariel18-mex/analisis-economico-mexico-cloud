# Análisis económico, demográfico y empresarial de México mediante herramientas en la nube

## Descripción del proyecto

Este proyecto desarrolla un pipeline de análisis de datos para comparar las 32 entidades federativas de México utilizando información pública de fuentes oficiales.

Se integran indicadores demográficos, económicos y empresariales para explorar diferencias entre estados, identificar patrones y presentar los resultados mediante un dashboard interactivo.

El proyecto fue desarrollado para la materia **Análisis de Datos en la Nube (LIAD7002)**.

## Objetivos

- Integrar información pública de México mediante APIs y archivos oficiales.
- Procesar, limpiar y transformar los datos utilizando Python.
- Almacenar y consultar información en Google BigQuery.
- Analizar indicadores estatales mediante técnicas estadísticas y aprendizaje no supervisado.
- Visualizar los resultados en una aplicación pública desarrollada con Streamlit.

## Tecnologías utilizadas

| Tecnología | Aplicación |
|---|---|
| Python | Extracción, limpieza y análisis de datos |
| Pandas | Transformación e integración de datasets |
| Google Colab | Ejecución del pipeline |
| Google BigQuery | Almacenamiento y consultas SQL en la nube |
| Scikit-learn | Escalamiento de variables y clustering K-Means |
| Streamlit | Dashboard interactivo |
| Plotly | Visualizaciones interactivas |
| GitHub | Publicación del código y documentación |

## Fuentes de datos

Los indicadores provienen de fuentes oficiales del INEGI:

- **Población por entidad federativa:** información correspondiente a 2025.
- **Producto Interno Bruto Estatal:** PIB de 2024, expresado en millones de pesos corrientes.
- **Directorio Estadístico Nacional de Unidades Económicas (DENUE):** número de establecimientos económicos por entidad federativa.

**Nota:** Los indicadores corresponden a diferentes periodos de referencia. Por ello, las comparaciones deben interpretarse considerando estas diferencias temporales.

## Arquitectura del proyecto

El flujo general de procesamiento es:

1. Extracción de información mediante APIs y archivos oficiales del INEGI.
2. Limpieza, transformación e integración de datos con Python en Google Colab.
3. Almacenamiento de la tabla integrada en Google BigQuery.
4. Consultas SQL y análisis exploratorio.
5. Estandarización de variables y aplicación de K-Means.
6. Exportación del dataset procesado con las etiquetas de clúster.
7. Visualización interactiva mediante Streamlit Community Cloud.

El dashboard publicado utiliza un archivo CSV procesado generado por el pipeline. No realiza consultas directas a BigQuery durante su ejecución.

## Análisis mediante K-Means

Se implementó el algoritmo K-Means utilizando tres variables:

- Población total.
- Número de establecimientos económicos.
- PIB estatal.

Las variables fueron estandarizadas mediante `StandardScaler` antes de entrenar el modelo.

Se seleccionaron tres clústeres, obteniendo la siguiente distribución:

| Clúster | Entidades | Características generales |
|---|---:|---|
| 0 | 24 | Menor magnitud relativa en las variables analizadas |
| 1 | 2 | Mayor magnitud económica y demográfica |
| 2 | 6 | Magnitud intermedia |

Los grupos representan similitudes en el tamaño económico y demográfico de las entidades. **No constituyen una clasificación de bienestar, calidad de vida ni desarrollo humano.**

## Dashboard interactivo

La aplicación permite:

- Consultar indicadores de cada entidad federativa.
- Comparar las entidades con mayor PIB.
- Visualizar la cantidad de estados por clúster.
- Explorar los estados pertenecientes a cada grupo.
- Analizar la relación entre PIB, establecimientos y población mediante una gráfica interactiva.

**Aplicación pública:** https://liadeconomiamexico.streamlit.app/

## Ejecución local

Para ejecutar el dashboard:

1. Descargar o clonar el repositorio.
2. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecutar la aplicación:

```bash
python -m streamlit run app.py
```

## Limitaciones

- Los indicadores no corresponden todos al mismo año.
- El clustering utiliza variables absolutas, por lo que está influido por el tamaño de las entidades.
- La segmentación no permite establecer relaciones causales.
- La aplicación utiliza una copia procesada de los datos, por lo que no se actualiza automáticamente cuando cambia la información oficial.

## Seguridad y ética

El proyecto utiliza información pública y agregada a nivel estatal. No incluye datos personales individuales.

Las credenciales y los tokens utilizados para acceder a servicios externos no deben publicarse en el repositorio.

Los resultados se presentan con fines académicos y exploratorios, evitando interpretar los clústeres como rankings de bienestar o superioridad económica.

## Autor
Ariel Yaredd Sanchez Gonzalez
Proyecto académico desarrollado para la materia Análisis de Datos en la Nube (LIAD7002).
