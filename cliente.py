""" 
Alumno: Maciel Amador Luis Roberto
UA: Transmisión de Datos
"""


import socket
import json

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
try:
    server_address = ('localhost', 5027)
    print('Conectando a {} puerto {}...'.format(*server_address))
    sock.connect(server_address)
    # Recibimos la información del server y la decodificamos en utf-8
    data = sock.recv(1024)
    data_json = data.decode('utf-8')

    # Como recibimos un JSON debemos transformarlo a un diccionario
    init_config = json.loads(data_json) 

    print(init_config['welcome'])
    print(f'Tamaño de la ventana: {init_config["window"]}')

    while True:
        textfile = input('Ingresar nombre del archivo: ')
        print('Iniciando transferencia')

        # Leer archivo
        with open(textfile, encoding = 'utf-8') as f:
            for line in f:
                init_config = {
                    'message': 'Bienvenido al servidor'
                }

                # Transformando dict a JSON
                data = json.dumps(init_config)
                # Enviando datos
                sock.sendall(data.encode('utf-8'))

                
                data = sock.recv(1024).decode('utf-8')
                data = json.loads(data) 

                print(f'Capacidad del buffer {data["buffer_status"]} de {init_config["window"]}')
                bf_status = int(data["buffer_status"])

                if bf_status == int(init_config['window']) :
                    message = 'Cliente en espera, buffer en capacidad máxima'
                    data = {
                        'message': message
                    }
                    data = json.dumps(data)

                    sock.sendall(data.encode('utf-8'))
                    print(message)
                    
                    data = sock.recv(1024).decode('utf-8')
                    data = json.loads(data) 
                    print(f'ACK{data["ack"]}')


except:
    print('Error en conexión')

finally:
    # Cerramos la conexión
    print('Cerrando conexión...')
    sock.close()