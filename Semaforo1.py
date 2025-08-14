
import time


def semaforo():
    contador = 0
    def luces():
        print("Estado de los semáforos:")
        print("Semaforo 1", Semaforo1)
        print("Semaforo 2", Semaforo2)
        print("Semaforo 3", Semaforo3)
        print("Semaforo 4", Semaforo4)
        
    while contador < 2:
        print("Ciclo", contador + 1)
        contador = contador + 1
        #semaforo1
        Semaforo1 = "Luz Verde"
        Semaforo2 = "Luz Roja"
        Semaforo3 = "Luz roja"
        Semaforo4 = "Luz roja"
        luces()
        time.sleep(5)
        Semaforo1 = "Luz Amarilla"
        Semaforo2 = "Luz Roja"
        Semaforo3 = "Luz roja"
        Semaforo4 = "Luz roja"
        luces()
        time.sleep(5)
        #semaforo2
        Semaforo1 = "Luz Roja"      
        Semaforo2 = "Luz Verde"
        Semaforo3 = "Luz roja"
        Semaforo4 = "Luz roja"
        luces()
        time.sleep(5)
        Semaforo1 = "Luz Roja"
        Semaforo2 = "Luz Amarilla"
        Semaforo3 = "Luz roja"
        Semaforo4 = "Luz roja"
        luces()
        time.sleep(5)
        #semaforo3
        Semaforo1 = "Luz Roja"
        Semaforo2 = "Luz Roja"  
        Semaforo3 = "Luz Verde"
        Semaforo4 = "Luz roja"
        luces()
        time.sleep(5)   
        Semaforo1 = "Luz Roja"
        Semaforo2 = "Luz Roja"
        Semaforo3 = "Luz Amarilla"
        Semaforo4 = "Luz roja"
        luces() 
        time.sleep(5)
        #semaforo4
        Semaforo1 = "Luz Roja"
        Semaforo2 = "Luz Roja"
        Semaforo3 = "Luz Roja"
        Semaforo4 = "Luz Verde"
        luces()
        time.sleep(5)
        Semaforo1 = "Luz Roja"
        Semaforo2 = "Luz Roja"
        Semaforo3 = "Luz Roja"
        Semaforo4 = "Luz Amarilla"
        luces() 
        time.sleep(5)
    print("Fin del ciclo de semáforos")
    
semaforo()