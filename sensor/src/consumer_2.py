import pika
from common import *

# Numero de cliente:
client_number = 2

def run():
    # Apertura de la conexión desde el cliente (consumidor) hasta el broker:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=BROKER_IP, port=BROKER_PORT))

    # Creación de un canal dentro de la conexión:
    channel = connection.channel()

    # Declaro el Exchange al que se van a enlazar las colas
    channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='direct')

    # Claves de enlace con las que voy a enlazar las colas de este cliente
    binding_keys = [
        'comedor',
        'cocina'
    ]
    # Colas que voy a consumir
    queues = [
        f'comedor_c{client_number}',
        f'cocina_c{client_number}'
    ]
    #
    def callback(ch, method, properties, body):
        print(f" [CONSUMER_c{client_number}] RECIBIDO: {body.decode('utf-8')}")
    #
    for i, queue in enumerate(queues): 
        # Declaración de la cola:
        channel.queue_declare(queue=queue)
        # Declaración del enlace entre las colas y el exchange:
        channel.queue_bind(exchange=EXCHANGE_NAME, queue=queue, routing_key=binding_keys[i])
        # Declaración de las colas a las que estará suscripto éste consumidor:
        channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)

    # print(' [*] To exit press CTRL+C\n') # Si ejecutamos desde el main, no sirve
    while True:
        channel.start_consuming() # Es bloqueante, espera hasta que llegue un mensaje. Cuando llegue se va a ejecutar la función 'callback'