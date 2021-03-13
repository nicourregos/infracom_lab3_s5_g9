import socket
from threading import Thread
import _thread
import logging
import hashlib
import lib
import datetime


def main():
    print("Start")
    fecha = datetime.datetime.today().strftime('%Y-%m-%d_%H-%M-%S')
    nombreLog: str = "./archivosS/log_" + fecha + ".log"
    logging.basicConfig(filename=nombreLog, level=logging.INFO , datefmt='%Y-%m-%d %H:%M:%S',
                        format='%(asctime)s %(levelname)-8s %(message)s')
    global archivo

    host = socket.gethostname()
    puerto = 55555
    logging.info('Conectado a %s en el puerto %s', host, puerto)

    socketS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketS.bind((host, puerto))
    print('Puerto: ', puerto)

    socketS.listen(5)
    print("Escuchando...")
    elegirArchivo = int(input("¿Qué archivo desea enviar? 1. 100 MB \t 2. 250 MB \n"))
    if elegirArchivo == 1:
        archivo = "./data/100MB.zip"
    else:
        archivo = "./data/250MB.zip"

    print("Se ha seleccionado el archivo ", archivo)

    threads = []
    # while True:
    #     lanzar threads
    socketS.close()

main()