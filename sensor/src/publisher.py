import pika
import random
import time
from common import *

def run():
    # Apertura de la conexión desde el publisher hasta el broker:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=BROKER_IP, port=BROKER_PORT))

    # Creación de un canal dentro de la conexión:
    channel = connection.channel()

    # > Decidí arriesgarme a enviar mensajes, sin haber declarado en el publisher las colas, podría incluso ni siquiera haber declarado el Exchange en base a la misma lógica.
    # > Entonces OJO: si el publisher ejecuta el código antes de que los clientes puedan declarar sus colas, ocurrirá un error.
    # > Esto es porque elegí resolverlo con un exchange de tipo 'direct'.
    channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='direct')

    i = 0
    # print(' [*] To exit press CTRL+C\n') # Si ejecutamos desde el main, no sirve
    while True:
        i = 0 if (i == N) else i+1 # Control del índice
        message = f' [°] {ROUTING_KEYS[i]} temperatura -> {round(random.uniform(-10, 40), 2)}°'
        channel.basic_publish(
            exchange=EXCHANGE_NAME, 
            routing_key=ROUTING_KEYS[i], 
            body=message
        ); print(f"\n [PUBLISHER] ENVIADO: {message}"); time.sleep(5)

    # connection.close()