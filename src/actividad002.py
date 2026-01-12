import pandas as andy
import numpy as np
import matplotlib.pyplot as plt


class Sales:
    """Clase para analizar ventas"""

    def __init__(self, sales_file_name):
       self.sales_file_name = sales_file_name
       self.sales_report_info = andy.DataFrame()

    def load_csv_file(self):
        print("===============================================")
        print("Leyendo archivo: ", self.sales_file_name)
        self.sales_report_info = andy.read_csv("files/"+self.sales_file_name)

    def average(self):
       mean_by_period=self.sales_report_info.mean(axis='index',numeric_only=True)
       total_mean = mean_by_period.to_list()[2]
                     
       print("===============================================")
       print("Monto promedio de ventas del perido: ")
       print("-----------------------------------------------")
      
       print('${:,.2f}'.format(total_mean))
    
    def max_sales(self):
       print("===============================================")
       print("Venta más grande del periodo:")
       print("-----------------------------------------------")
       print(f"{self.sales_report_info.max(axis='index',numeric_only=True)}")

    def min_sales(self):
       print("===============================================")
       print("Venta más pequeña del periodo:")
       print("-----------------------------------------------")
       print(f" {self.sales_report_info.min(axis='index',numeric_only=True)}")

    def group_data(self):
       new_data_with_month = self.sales_report_info
       new_data_with_month['Sale_Date'] = andy.to_datetime(
                                           new_data_with_month['Sale_Date'],
                                           errors='coerce'   # Maneja fechas inválidas
                                          )
       new_data_with_month['Month']=new_data_with_month['Sale_Date'].dt.to_period('M')
       grouped_data =  (new_data_with_month
                        .groupby(['Month','Geography'], as_index=False)
                        .agg(
                            Avg_Sale_Amount=('Sale_Amount', 'mean'),
                            Max_Sale_Amount=('Sale_Amount', 'max'),
                            Min_Sale_Amount=('Sale_Amount', 'min')
                        ))
                     
       
       print("===============================================")
       print("Agrupación de Información:")
       print("-----------------------------------------------")
       print(grouped_data)     
       grouped_data.to_csv("outputs/sales_metrics_by_region.csv")                       


sales = Sales("sales_data_2023.csv")
sales.load_csv_file()

sales.average()
sales.max_sales()
sales.min_sales()
sales.group_data()