import time

    
def semaforo_con_boton():
    # Tiempos para cada estado
    tiempo_verde = 5
    tiempo_amarillo = 2
    tiempo_rojo = 5

    def mostrar_estado(semaforo, estado):
        print(f"Semáforo {semaforo}: {estado}")
        if estado == "Luz Verde":
            print("Mensaje audible: Puede cruzar.")
        elif estado == "Luz Roja":
            print("Mensaje audible: Espere, no cruce.")
        time.sleep(1)

    for ciclo in range(2):
        print(f"\nCiclo {ciclo + 1}")
        
        # Semáforo 1: Verde
        mostrar_estado(1, "Luz Verde")
        time.sleep(tiempo_verde)
        
        # Simular botón peatonal
        boton = input("¿Presionó el botón peatonal? (s/n): ").strip().lower()
        if boton == "s":
            print("Botón peatonal presionado. Cambiando a luz roja...")
            mostrar_estado(1, "Luz Roja")
            time.sleep(tiempo_rojo)
            continue  # Saltar al siguiente ciclo
        
        # Semáforo 1: Amarillo
        mostrar_estado(1, "Luz Amarilla")
        time.sleep(tiempo_amarillo)
        
        # Semáforo 1: Rojo
        mostrar_estado(1, "Luz Roja")
        time.sleep(tiempo_rojo)

    print("\nFin del ciclo de semáforos.")

# Ejecutar la simulación con botón
semaforo_con_boton()