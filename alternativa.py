import threading
import queue
import time

# Creamos una cola compartida
shared_queue = queue.Queue()

# Creamos una función productor que agrega datos a la cola compartida
def productor():
    for i in range(10):
        shared_queue.put(i)
        time.sleep(0.5)

# Creamos una función consumidor que lee datos de la cola compartida
def consumidor():
    while True:
        if shared_queue.empty():
            break
        data = shared_queue.get()
        print("Dato obtenido:", data)
        time.sleep(1)

# Creamos los hilos para el productor y el consumidor
thread_productor = threading.Thread(target=productor)
thread_consumidor = threading.Thread(target=consumidor)