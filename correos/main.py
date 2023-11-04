from src import consumer_1
from src import consumer_2
from src import consumer_3
from src import publisher_1
from src import publisher_2
import threading # Para poder hacer las ejecuciones en paralelo

def main():
    thread_c1 = threading.Thread(target=consumer_1.run)
    thread_c2 = threading.Thread(target=consumer_2.run)
    thread_c3 = threading.Thread(target=consumer_3.run)
    thread_p1  = threading.Thread(target=publisher_1.run)
    thread_p2  = threading.Thread(target=publisher_2.run)

    # Inicia los hilos
    thread_c1.start()
    thread_c2.start()
    thread_c3.start()
    thread_p1.start()
    thread_p2.start()

    # OJO QUE LA ÚNICA MANERA QUE HAY DE CORTAR LA EJECUCIÓN AHORA, ES MATAR LA TERMINAL

if __name__ == '__main__': main()