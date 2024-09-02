import pandas as pd
import matplotlib.pyplot as plt
import glob

# Cargar el archivo general con los datos de todos los sistemas
general_data = pd.read_csv('descarga.csv')

# Función para cargar y procesar los datos de O-C
def process_oc_file(filename):
    with open(filename, 'r') as file:
        # Leer la primera línea que contiene los nombres de las columnas
        first_line = file.readline().strip()
        # Eliminar el # inicial si existe
        if first_line.startswith('#'):
            first_line = first_line[1:].strip()
        # Usar 'split' para separar los nombres de las columnas correctamente, preservando nombres como "O-C (days)"
        column_names = first_line.split('\t')

    # Cargar el resto del archivo utilizando los nombres de las columnas
    oc_data = pd.read_csv(filename, delim_whitespace=True, comment='#', names=column_names, skiprows=1)
    
    # Filtrar los eclipses primarios y secundarios
    primary_eclipse = oc_data[oc_data['Eclipse'] == 1]
    secondary_eclipse = oc_data[oc_data['Eclipse'] == 2]
    
    return primary_eclipse, secondary_eclipse

# Iterar sobre todos los sistemas binarios en el archivo general
for index, system in general_data.iterrows():
    kic = str(system['KIC'])

    # Construir el nombre del archivo individual, considerando el prefijo "0" si es necesario
    possible_files = [f'{kic.zfill(8)}.00.lc.etv.csv', f'{kic}.00.lc.etv.csv']  # Archivos potenciales
    
    oc_file = None
    for file in possible_files:
        if glob.glob(file):
            oc_file = file
            break

    if not oc_file:
        print(f'Archivo no encontrado para KIC {kic}')
        continue  # Saltar a la siguiente iteración si el archivo no existe
    
    # Procesar el archivo de O-C
    primary_eclipse, secondary_eclipse = process_oc_file(oc_file)

    # Crear la gráfica de la curva O-C para los eclipses primario y secundario
    plt.figure(figsize=(10, 6))
    plt.errorbar(primary_eclipse['BJD'], primary_eclipse['O-C (days)'], 
                 yerr=primary_eclipse['Error (days)'], fmt='o', label='Eclipse Primario')
    plt.errorbar(secondary_eclipse['BJD'], secondary_eclipse['O-C (days)'], 
                 yerr=secondary_eclipse['Error (days)'], fmt='o', label='Eclipse Secundario', color='r')
    
    # Configurar la gráfica
    plt.xlabel('BJD')
    plt.ylabel('O-C (días)')
    plt.title(f'Curvas O-C para Eclipses Primario y Secundario - KIC {kic}')
    plt.legend()
    plt.grid(True)
    
    # Guardar la figura en lugar de mostrarla
    plt.savefig(f'ETV_vs_BJD_KIC_{kic}.png')
    plt.close()  # Cerrar la figura para liberar memoria

print("Generación de gráficos completada.")
