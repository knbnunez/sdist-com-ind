from src import consumer_1
from src import consumer_2
from src import consumer_3
from src import publisher
import threading # Para poder hacer las ejecuciones en paralelo

def main():
    thread_c1 = threading.Thread(target=consumer_1.run)
    thread_c2 = threading.Thread(target=consumer_2.run)
    thread_c3 = threading.Thread(target=consumer_3.run)
    thread_p  = threading.Thread(target=publisher.run)

    # Inicia los hilos
    thread_c1.start()
    thread_c2.start()
    thread_c3.start()
    thread_p.start()

    # OJO QUE LA ÚNICA MANERA QUE HAY DE CORTAR LA EJECUCIÓN AHORA, ES MATAR LA TERMINAL

if __name__ == '__main__': main()