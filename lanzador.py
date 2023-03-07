from ejercicio import *

def lanzar():

    t1 = Thread(target=producer,args=("Juan",))

    t2 = Thread(target=customer,args=("Pepe",))

    t1.start()

    t2.start()