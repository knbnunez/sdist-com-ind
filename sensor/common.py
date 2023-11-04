# Me traje algunas variables compartidas acá para no repetir código.

#
BROKER_IP='localhost'
BROKER_PORT=5672
#
EXCHANGE_NAME='sensor'
#
ROUTING_KEYS=[
    'comedor',
    'cocina',
    'habitacion_ninios',
    'habitacion_padres'
]; N = len(ROUTING_KEYS)-1
#
