import pandas as pd 

#ruta donde guardamos el libro de excel 
ruta_excel = 'C:\\Users\\52993\\OneDrive\\Desktop\\python_ia\\Libro1.xlsx'
df = pd.read_excel(ruta_excel)
##imprimir el contenido del archivo de excel

print("contenido del archivo")
print(df)
##imprimimso el contenido de la columna 'Nombre'
print("Resumen de los datos")
print(df.describe())

compras_mayores_5000=df[df['total '] > 5000]
print("Compras mayores a 5000:")
print(compras_mayores_5000)

compras_mayores_5000.to_excel("compras_filtradas.xlsx", index=False)
