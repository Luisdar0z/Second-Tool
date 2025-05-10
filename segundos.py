def convertir_a_hh_mm_ss(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    return f"{horas:02}:{minutos:02}:{segundos_restantes:02}"

# Ejemplo de uso
segundos = int(input("Ingrese los segundos: "))
resultado = convertir_a_hh_mm_ss(segundos)
print("Tiempo:", resultado)
