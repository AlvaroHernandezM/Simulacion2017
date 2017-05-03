#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import numpy as np

class Vehiculo:

    ancho = 60
    alto = 20
    dibujo = None  # Es la referencia del dibujo que pertenece a esta particula en el canvas
    distanciaPrudente= 5

    def __init__(self, via, vehiculos, limiteVentana, color, id):
        self.limiteVentana = limiteVentana
        self.carril = random.randrange(1, 3)  # La vía tiene dos carriles
        self.via = via
        self.vehiculos = vehiculos
        self.setPosicion()
        self.velocidad = np.array([random.randrange(1, 4), 0])  # Velocidad en Y = 0
        self.velocidadMaxima = self.velocidad[0]
        self.color = color
        self.id = id
        # print self.coordenadas

    def setPosicion(self):
        if self.carril == 1:  # Carril superior
            y = self.via['limiteSuperior'] + ((self.via['divisionCarriles'] - self.via['limiteSuperior']) / 2)
        else:
            y = self.via['divisionCarriles'] + ((self.via['limiteInferior'] - self.via['divisionCarriles']) / 2)
        self.posicion = np.array([0, y])

    def mover(self):
        if self.posicion[0] < self.limiteVentana:
            if self.verificarAdelante() is False:  # hay un veliculo adelante
                if self.verificarLateral() is False:  # hay un vehiculo en el otro carril               
                    self.frenar()
                else:
                    self.cambiarCarril()
        # print str(self.velocidad[0])+'-'+str(self.velocidadOriginal[0])
            if self.velocidad[0] < self.velocidadMaxima:
                self.velocidad[0] += 1
            self.posicion = self.posicion + self.velocidad
        # self.velocidad = self.velocidad + 1  if self.velocidad < self.velocidadOriginal else self.velocidadOriginal


    def frenar(self):
        self.velocidad[0] = 0


    def cambiarCarril(self):
        if self.carril == 2:  # Esta en el inferior hay que cambiar
            y = self.via['limiteSuperior'] + ((self.via['divisionCarriles'] - self.via['limiteSuperior']) / 2)
            self.carril = 1
        else:  # Esta en el superior hay que cambiar
            y = self.via['divisionCarriles'] + ((self.via['limiteInferior'] - self.via['divisionCarriles']) / 2)
            self.carril = 2
        self.posicion = np.array([self.posicion[0], y])

    def verificarAdelante(self):
        for vehiculo in self.vehiculos:
            if self.carril == vehiculo.carril:
                if self.posicion[0] == vehiculo.posicion[0] is False:
                    if vehiculo.posicion[0] > self.posicion[0] + self.ancho:
                        distancia = (vehiculo.posicion[0] - (self.posicion[0] + self.ancho))
                        if distancia <= self.distanciaPrudente and distancia > 0:
                            return False
                    else:
                        distancia = (vehiculo.posicion[0] - (self.posicion[0] + self.ancho))
                        if distancia >= 0:
                            return False
                else:
                    return False
        return True

    def verificarLateral(self):
        for vehiculo in self.vehiculos:
            if self.carril != vehiculo.carril:
                if self.posicion[0] >= vehiculo.posicion[0]:
                    distancia = (self.posicion[0] - (vehiculo.posicion[0] + self.ancho))
                    #print 'veh pos 0 '+str(vehiculo.posicion[0] + self.ancho)+' veh yo '+str(self.posicion[0])+' dist: '+str(distancia)
                    if distancia <= self.distanciaPrudente:
                        return False
                else:
                     distancia = (vehiculo.posicion[0] - (self.posicion[0]  + self.ancho) )
                     if distancia <= self.distanciaPrudente:
                        return False

        return True

    # Para referenciar el dibujo en la pantalla
    def setDibujo(self, dibujo):
        self.dibujo = dibujo
