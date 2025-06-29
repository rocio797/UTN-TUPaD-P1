import random
import time
from statistics import mean

def busqueda_lineal(lista, objetivo):
    """Implementación canónica de búsqueda lineal"""
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice
    return -1

def busqueda_binaria(lista, objetivo):
    """Implementación eficiente de búsqueda binaria"""
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

def generar_datos(tamaño):
    """Genera lista ordenada con valores únicos"""
    lista = random.sample(range(1, tamaño * 10), tamaño)
    lista.sort()
    return lista

def ejecutar_experimento(repeticiones=5):
    """Ejecuta el experimento comparativo completo"""
    tamaños = [100, 1000, 10000, 100000]
    objetivo = 42
    
    print("ANÁLISIS COMPARATIVO DE ALGORITMOS DE BÚSQUEDA")
    print("=" * 50 + "\n")
    
    for tamaño in tamaños:
        tiempos_lineal = []
        tiempos_binaria = []
        
        for _ in range(repeticiones):
            datos = generar_datos(tamaño)
            
            # Controlamos la presencia del objetivo
            if random.random() > 0.5:
                pos = random.randint(0, len(datos)-1)
                datos[pos] = objetivo
            
            # Medición búsqueda lineal
            inicio = time.perf_counter()
            resultado_lineal = busqueda_lineal(datos, objetivo)
            tiempos_lineal.append(time.perf_counter() - inicio)
            
            # Medición búsqueda binaria
            inicio = time.perf_counter()
            resultado_binario = busqueda_binaria(datos, objetivo)
            tiempos_binaria.append(time.perf_counter() - inicio)
        
        # Cálculo de promedios
        avg_lineal = mean(tiempos_lineal)
        avg_binaria = mean(tiempos_binaria)
        
        # Presentación de resultados
        print(f"TAMAÑO DE LISTA: {tamaño:>7} elementos")
        print("-" * 40)
        print(f"Búsqueda lineal (promedio): {avg_lineal:.8f} segundos")
        print(f"Búsqueda binaria (promedio): {avg_binaria:.8f} segundos")
        
        if avg_binaria > 0:
            mejora = avg_lineal / avg_binaria
            print(f"Factor de mejora: {mejora:.1f}x más rápida")
        else:
            print("La búsqueda binaria fue instantánea")
        
        print("\n" + "=" * 50 + "\n")

if __name__ == "__main__":
    ejecutar_experimento()