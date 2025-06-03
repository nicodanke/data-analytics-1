import pandas as pd

# Cargar el dataset
# Asegúrate de que la ruta 'data/phone_data.csv' sea accesible desde donde ejecutes el script
try:
    dataset = pd.read_csv('data/phone_data.csv', index_col=0)
except FileNotFoundError:
    print("Error: El archivo 'data/phone_data.csv' no fue encontrado.")
    print("Por favor, asegúrate de que el script se ejecute desde el directorio correcto o ajusta la ruta.")
    exit()

# Convertir la columna 'date' a datetime
dataset['date'] = pd.to_datetime(dataset['date'], format='%d/%m/%y %H:%M')

print("Dataset cargado y columna 'date' convertida a datetime.\n")

# Ejemplo 1: llamadas con duración mayor a 1000 segundos
print("Llamadas con duración superior a 1000 segundos:")
llamadas_largas = dataset.query('item == "call" and duration > 1000')
print(llamadas_largas.head())
print("-" * 50)

# Ejemplo 2: SMS enviados a través de la red Vodafone
print("\nSMS enviados a través de la red Vodafone:")
sms_vodafone = dataset.query('item == "sms" and network == "Vodafone"')
print(sms_vodafone.head())
print("-" * 50)

# Ejemplo 3: Uso de datos en el mes '2015-01'
print("\nUso de datos (data) en el mes de Enero 2015:")
datos_enero_2015 = dataset.query('item == "data" and month == "2015-01"')
print(datos_enero_2015.head())
print("-" * 50)

# Ejemplo 4: Llamadas que no son a 'landline' y duran menos de 60 segundos
variable_red = "landline"
duracion_corta = 60
print(f"\nLlamadas cortas (<{duracion_corta}s) que no son a red '{variable_red}':")
llamadas_cortas_no_fijo = dataset.query('item == "call" and network_type != @variable_red and duration < @duracion_corta')
print(llamadas_cortas_no_fijo.head())
print("-" * 50)

# Ejemplo de búsqueda tipo LIKE: encontrar redes que contengan "da"
# Esto sería similar a LIKE '%da%' en SQL
print("\nRedes cuyo nombre contiene 'da' (insensible a mayúsculas/minúsculas):")
# Es importante usar engine='python' para expresiones complejas o métodos de string
redes_con_da = dataset.query('network.str.contains("da", case=False, na=False)', engine='python')
print(redes_con_da.head())
print("-" * 50)

# Otro ejemplo tipo LIKE: items que comienzan con "ca" (como 'call')
print("\nItems que comienzan con 'ca':")
items_empiezan_con_ca = dataset.query('item.str.startswith("ca", na=False)', engine='python')
print(items_empiezan_con_ca.head())
print("-" * 50)

print("\nScript de ejemplos de query finalizado.") 