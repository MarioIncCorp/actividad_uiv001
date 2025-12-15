# Instalación de make

Para instalar make 

sudo apt-get update
sudo apt-get install build-essential

# Uso de make 

### Instalación y configuración

Crear ambiente virtual

create-venv

Instalación de dependencias

make install 

# Docstring para main

### a) Verificar la integridad y consistencia de los datos
 
 Esto incluye revisar que los nombres de las columnas estén correctos, 
 que los tipos de datos sean apropiados para cada columna y que no haya valores nulos o inconsistencias en los datos.

### b) Realizar las siguientes tareas para asegurar que los datos sean adecuados para el análisis:

- Cambia los tipos de datos de las columnas cuando sea necesario (por ejemplo, convertir cadenas de texto a fechas o números).
- Elimina los valores atípicos que puedan distorsionar los análisis y los registros duplicados.
- Rellena o elimina los valores faltantes en las columnas según corresponda, dependiendo de la naturaleza de los datos y los requisitos del análisis.

### c) Agrupar las ventas mensuales por región geográfica para entender las tendencias de ventas en diferentes áreas. 

Visualicen los resultados en tablas o gráficos básicos (por ejemplo, gráficos de barras o líneas) para facilitar la 
interpretación de los datos y obtener insights claros y útiles.

# Correr programa

Ubicarse en la carpeta src y correr el comando

python main.py

- Leé archivo customers
- Leé archivo sales
   |______ Revisa integridad de los datos customers y sales
   |______ Limpia datos de customers y sales
   |______ Unión (left join), entre customers y sales
   |______ Agrupa y grafica ventas mensuales por región geográfica