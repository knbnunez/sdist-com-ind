import pika
import time
import random
from lorem_text import lorem

from common import *

pub_number = 1

def run():
    # Apertura de la conexión desde el publisher hasta el broker:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=BROKER_IP, port=BROKER_PORT))

    # Creación de un canal dentro de la conexión:
    channel = connection.channel()

    # Mismo caso, no estoy haciendo la declaración de las colas, necesito que los consumers sí o sí creen sus colas antes.
    channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='topic')

    routing_key = 'deporte.gazzetta.italy'

    # print(' [*] To exit press CTRL+C\n') # Si ejecutamos desde el main, no sirve
    while True:
        send_message(channel, routing_key)

    # connection.close()

def send_message(channel, routing_key):
    message = f' > Asunto: {routing_key}; Body: {lorem.paragraph()};'
    if random.random() < 0.8:  # 80% de probabilidad de entrega exitosa
        channel.basic_publish(
            exchange=EXCHANGE_NAME, 
            routing_key=routing_key, 
            body=message
        ); print(f"[P{pub_number}] ENVIADO: {message}"); time.sleep(5)
    else:
        print(f' [P{pub_number}] ERROR EN ENVÍO... Reintento en unos segundos...')
        time.sleep(random.randint(1, 5))  # Retraso aleatorio entre 1 y 5 segundos para el reintento
        send_message(channel, routing_key)  # Reintentar el envío