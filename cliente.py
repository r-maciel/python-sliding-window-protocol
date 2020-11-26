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
    server_address = ('localhost', 5040)
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
        with open(textfile) as f:

            for line in f:
                data = {
                    'message': line,
                    'trans_status': True
                }
                data = json.dumps(data)
                sock.sendall(data.encode('utf-8'))

                print('-----------------------------------------------------------------------------') 
                print(line)

                data = sock.recv(1024).decode('utf-8')
                data = json.loads(data)

                print(f'Capacidad del buffer {data["buffer_status"]} de {init_config["window"]}')
                bf_status = data["buffer_status"]

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
        print('-----------------------------------------------------------------------------') 
        print('\n') 
        print('\n') 
        print('Archivo enviado al 100%')

        data = {
            'trans_status': False
        }

        # Transformando dict a JSON
        data = json.dumps(data)
        # Enviando datos
        sock.sendall(data.encode('utf-8'))
        
        data = sock.recv(1024).decode('utf-8')
        data = json.loads(data) 
        print(data['message'])

        print('\n') 
        print('\n')
        while bf_status > 0:
            print('-----------------------------------------------------------------------------') 
            data = {
                'message': 'Usando datos en memoria'
            }
            data = json.dumps(data)
            sock.sendall(data.encode('utf-8'))

            data = sock.recv(1024).decode('utf-8')
            data = json.loads(data) 
            print(f'ACK{data["ack"]}')
            print(f'Capacidad del buffer {data["buffer_status"]} de {init_config["window"]}')

            bf_status = data["buffer_status"]
        
        break

except Exception as e:
    print('Error en conexión')
    print(e)

finally:
    # Cerramos la conexión
    print('Cerrando conexión...')
    sock.close()