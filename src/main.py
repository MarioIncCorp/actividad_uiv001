import pandas as andy
import numpy as np
import matplotlib.pyplot as plt

def readCSVFile(csvFileName):
    print("===============================================")
    print("Leyendo archivo: ", csvFileName)
    _reportInfo = andy.read_csv("files/"+csvFileName)
    
    return _reportInfo


def reviewDataIntegrity(data2Review):
    ### a  - Integridad de la información: 
    ###      -> Validar Nombres de columnas 
    ###      -> Cotejar nombres apropiados de las columnas 
    ###      -> Eliminar nulos o inconsistencias en los datos.
    print(data2Review.info())

def cleanDataSale(data2Clean):
    ### Cambia los tipos de datos de las columnas cuando sea necesario (por ejemplo, convertir cadenas de texto a fechas o números).
    ### Elimina los valores atípicos que puedan distorsionar los análisis y los registros duplicados.
    ### Rellena o elimina los valores faltantes en las columnas según corresponda, 
    ### dependiendo de la naturaleza de los datos y los requisitos del análisis.

    # Borra duplicados
    data2Clean = data2Clean.drop_duplicates()
    
    # Eliminar registro si una de las dos columnas es vacía (por ser llave compuesta)
    data2Clean = data2Clean.dropna(subset=['Sale_ID', 'Customer_ID'])
    
    # Convertir Fecha de Venta a tipo de dato datetime
    data2Clean['Sale_Date'] = andy.to_datetime(data2Clean['Sale_Date'], errors='coerce')

    # Convertir monto de venta a float
    #data2Clean['Sale_Amount'] = andy.to_numeric(data2Clean['Sale_Amount'], errors='coerce')

    # Rellenar información faltante
    numeric_cols_sales = data2Clean.select_dtypes(include=['float64', 'int64']).columns
    data2Clean[numeric_cols_sales] = data2Clean[numeric_cols_sales].fillna(data2Clean[numeric_cols_sales].median())

    return data2Clean

def cleanDataCustomer(data2Clean):
    ### Cambia los tipos de datos de las columnas cuando sea necesario (por ejemplo, convertir cadenas de texto a fechas o números).
    ### Elimina los valores atípicos que puedan distorsionar los análisis y los registros duplicados.
    ### Rellena o elimina los valores faltantes en las columnas según corresponda, 
    ### dependiendo de la naturaleza de los datos y los requisitos del análisis.

    # Borra duplicados
    data2Clean = data2Clean.drop_duplicates()

    # Borra registros nulos con clave primaria vacía
    data2Clean = data2Clean.dropna(subset=['Customer_ID'])

    # Convertir Fecha de Venta a tipo de dato datetime
    data2Clean['Customer_Age'] = andy.to_numeric(data2Clean['Customer_Age'], errors='coerce', downcast='integer')

    return data2Clean

def mergeData(customersData, salesData ):
    mergedFrame = salesData.merge(customersData, on='Customer_ID', how='left')
    return mergedFrame
    
def graphData(monthly_sales):
    plt.figure(figsize=(10, 6))

    for region in monthly_sales['Geography_x'].unique():
        subset = monthly_sales[monthly_sales['Geography_x'] == region]
        plt.plot(subset['Month'].astype(str),
             subset['Sale_Amount'],
             marker='o',
             label=region)

    plt.xlabel('Mes')
    plt.ylabel('Total de Ventas')
    plt.title('Ventas Mensuales por Región (Ejemplo 2023)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

def calculateSummary():
    print('\N{grinning face with smiling eyes} Analizando Documentos...')
    customers = readCSVFile("customer_data_2023.csv")
    sales = readCSVFile("sales_data_2023.csv")
    print("===============================================")
    print("--------- Encabezado Customer --------")
    print(customers.head())
    print("--------- Encabezado Sales --------")
    print(sales.head())

    ### a  - Integridad de la información: 
    print("===============================================")
    print("--------- Integridad de la Información --------")
    print("---- Customers ------")
    reviewDataIntegrity(customers)
    reviewDataIntegrity(sales)

    ### b - Limpieza de datos
    print("===========================================================")
    print("--------- Limpieza y preparación de la Información --------")
    print("---- Customers ------")
    customers = cleanDataCustomer(customers)
    print("---- Sales ------")
    sales = cleanDataSale(sales)

    ### c - Integración (merge de la información)
    print("===========================================================")
    print("--------- Integración de la Información --------")
    mergedData = mergeData(customersData=customers, salesData=sales)
    print("******* Información Integrada (sales join customers) ********")
    print(mergedData.head())

    print("===========================================================")
    print("=== Ventas mensuales por región ===")
    mergedData['Month'] = mergedData['Sale_Date'].dt.to_period('M')

    # Agrupar por mes y región
    monthly_sales = mergedData.groupby(['Month', 'Geography_x'])['Sale_Amount'].sum().reset_index()
    print(monthly_sales.head(12))

    graphData(monthly_sales)

if __name__ == '__main__':
  calculateSummary()