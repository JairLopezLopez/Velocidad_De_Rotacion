import math

def calcular_velocidad_rotacion(latitud, longitud):

    latitud_rad = math.radians(latitud)
    longitud_rad = math.radians(longitud)

 
    radio_tierra_km = 6371  
    periodo_rotacion_horas = 24 

    # Calcular velocidad de rotación
    velocidad_rotacion = (2 * math.pi * radio_tierra_km * math.cos(latitud_rad)) / periodo_rotacion_horas

    return velocidad_rotacion


latitud = 18.60646 # Latitud 
longitud = -90.73780  # Longitud 

latitud2 = 38.373825292521154 #Segunda latitud
longitud2 = -69.67405073588125 #Segunda longitud


velocidad_resultante = calcular_velocidad_rotacion(latitud, longitud)
velocidad_resultante2 = calcular_velocidad_rotacion(latitud2, longitud2)

print(f"La velocidad de rotación en la ubicación ({latitud}, {longitud}) es aproximadamente {velocidad_resultante:.8f} km/h.")
print(f"La velocidad de rotación en la ubicación ({latitud2}, {longitud2}) es aproximadamente {velocidad_resultante2:.6f} km/h.")
