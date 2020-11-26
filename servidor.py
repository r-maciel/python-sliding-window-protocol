""" 
Alumno: Maciel Amador Luis Roberto
UA: Transmisión de Datos
"""

import socket
import json

# Creamos el socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definimos los datos de nuestro server
server_address = ('localhost', 5027)
print('Inicializando en {} puerto {}'.format(*server_address))
sock.bind(server_address)

# Escuchamos las posibles conexiones al server
sock.listen(1)

while True:
    # Esperamos por alguna conexión y la aceptamos
    print('Esperando por conexión...')
    connection, client_address = sock.accept()
    
    print('Conectado desde', client_address)

    try:
        # Valores que mandaremos al inicio de la conexión
        init_config = {
            'welcome': 'Bienvenido al servidor',
            'window': 5
        }

        # Transformando dict a JSON
        data = json.dumps(init_config)
        # Enviando datos
        connection.sendall(data.encode('utf-8'))

        # Init buffer
        buffer = []
        buffer_status = len(buffer)
        ack = 0

        transfering = True

        while transfering:
            while buffer_status < init_config['window'] :
                # Recibimos y decodificamos los datos que el cliente envía
                data = connection.recv(1024).decode('utf-8')
                data = json.loads(data)
                if data['message']:
                    transfering = False
                    break

                buffer.append(data['message'])

                buffer_status += 1
                
                data = {
                    'buffer_status': buffer_status
                }
                data = json.dumps(data)
                connection.sendall(data.encode('utf-8'))

            if transfering :

                print(buffer)

                # Mensaje del status del cliente
                data = connection.recv(1024).decode('utf-8')
                data = json.loads(data)
                print(data['message'])

                # Remove first element from buffer
                print(buffer.pop(0))
                buffer_status -= 1

                ack += 1
                data = {
                    'ack': ack
                }
                data = json.dumps(data)
                connection.sendall(data.encode('utf-8'))

    finally:
        # Cerramos la conexión con el cliente
        connection.close()