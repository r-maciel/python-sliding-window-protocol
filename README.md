# Protocolo de Ventana Deslizante (Simulador)
Simulador para la transferencia de un archivo de texto de un servidor a un cliente por medio del Protocolo de Ventana Deslizante.

## Requisitos
- Python v3.x (Desarrollado con v3.8.2)

## Instalación
Clone el repositorio desde la terminal
```
git clone https://github.com/r-maciel/python-sliding-window-protocol.git
```
O descárguelo como zip

## Uso
Abra una terminal, posicionese dentro del directorio donde se encuentran los archivos e inicie el servidor
Ejemplo.
```
python3 servidor.py
```

Abra una nueva terminal, posicionese dentro del directorio donde se encuentran los archivos e inicie el cliente
Ejemplo.
```
python3 cliente.py
```
La conexión se debe de haber establecido y ya puede empezar a transmitir su archivo

## Notas
Por defecto se incluye un archivo test.txt para transmitir como prueba, a la hora de ingresar el nombre del archivo se debe de incluir la extensión de este.
Ejemplo.
```
Ingresar nombre del archivo: test.txt
```
Puedes transmitir cualquier otro archivo de texto, pero debes de colocarlo al mismo nivel que los otros arhivos del proyecto, o en su defecto proporcionar el PATH completo del archivo