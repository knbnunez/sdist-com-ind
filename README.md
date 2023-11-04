#### Los ejercicios están pensados para ser una demo de cómo funcionaría el broker en diferentes hosts, con publicadores y suscriptores.


#### Dada la orientación, la funcionalidad está resuelta para que el usuario solamente tenga que ejecutar un "py main.py" por consola. Esto activa automáticamente la ejecución de los hilos de ejecución simulando cada uno de los procesos (publicadores y suscriptores).


#### Lamentablemente, debido a cómo se implementó, la única manera de finalizar la ejecución una vez ejecutado el "main.py", es matando la terminal. No es posible cortarla con Ctrl+C.


# Requerimientos ejecución:
***
* [Instalar]: python3 # El test se hizo sobre la versión 3.10
* [Instalar]: requirements.txt # Conveniente usar un entorno virtual 'pip install -r requirements.txt'
* [Ejecución]: py main.py
***