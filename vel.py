import math

def calcular_velocidad_rotacion(latitud, longitud):

    latitud_rad = math.radians(latitud)
    longitud_rad = math.radians(longitud)

 
    radio_tierra_km = 6371  
    periodo_rotacion_horas = 24 

    # Calcular velocidad de rotación
    velocidad_rotacion = (2 * math.pi * radio_tierra_km * math.cos(latitud_rad)) / periodo_rotacion_horas

    return velocidad_rotacion


latitud = -38.373825292521154  # Latitud 
longitud = -69.67405073588125  # Longitud 

velocidad_resultante = calcular_velocidad_rotacion(latitud, longitud)

print(f"La velocidad de rotación en la ubicación ({latitud}, {longitud}) es aproximadamente {velocidad_resultante:.6f} km/h.")
