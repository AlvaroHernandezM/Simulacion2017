#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import numpy as np
import time
import threading
from vehiculo import Vehiculo
from ventana import Ventana


class Simulador:

    anchoVentana = 1000
    alturaVentana = 600

    def __init__(self):
        self.ventana = Ventana({'ancho': self.anchoVentana, 'alto': self.alturaVentana})

    def generar(self, cantidadParticulas=15):
        self.vehiculos = []
        for i in xrange(0, cantidadParticulas):
            self.generateColor()
            vehiculo = Vehiculo(self.ventana.via, self.vehiculos, self.anchoVentana, self.color, i)
            self.vehiculos.append(vehiculo)
            espera = np.random.poisson()
            time.sleep(espera)
            pass

    # ....Hilo.....
    def moverParticulas(self):
        while True:
            #self.ventana.dibujarVias()
            for x in xrange(0, len(self.vehiculos)):
                self.vehiculos[x].mover()
                pass
            self.ventana.dibujarOvalos(self.vehiculos)
            time.sleep(0.01)

    def mostrarVentana(self):
        self.ventana.mostrar()

    def generateColor(self):
        data = ['red','blue','black','white','green','yellow','gray','pink']
        self.color = data[random.randrange(len(data))]
        


simulador = Simulador()

hiloGenerador = threading.Thread(target=simulador.generar)
hiloGenerador.daemon = True
hiloGenerador.start()

# Hilo que mueve y dibuja
hilo = threading.Thread(target=simulador.moverParticulas)
hilo.daemon = True
hilo.start()

simulador.mostrarVentana()
