#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *


class Ventana:
    def __init__(self, tamano):
        self.tamano = tamano
        self.ventana = Tk()
        self.ventana.title('Vehiculos')
        # self.ventana.geometry("1000x500")
        self.ventana.geometry(str(tamano['ancho']) + "x" + str(tamano['alto']))
        # self.ventana.geometry(tamano['ancho'], tamano['alto'])
        self.canvas = Canvas(width=tamano['ancho'], height=tamano['alto'], bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        self.dibujarVias()

    def dibujarVias(self):
        anchoVia = 100
        # Se dibuja en la mitad
        limiteSuperior = (self.tamano['alto'] / 2) - (anchoVia / 2)
        limiteInferior = (self.tamano['alto'] / 2) + (anchoVia / 2)
        lineaDivisionCarril = limiteSuperior + ((limiteInferior - limiteSuperior) / 2)
        self.via = {'ancho': anchoVia, 'limiteSuperior': limiteSuperior, 'limiteInferior': limiteInferior, 'divisionCarriles': lineaDivisionCarril}

        # Dibuja via
        self.canvas.create_line(0, limiteSuperior, self.tamano['ancho'], limiteSuperior, width=2)
        self.canvas.create_line(0, limiteInferior, self.tamano['ancho'], limiteInferior, width=2)

        self.canvas.create_line(0, lineaDivisionCarril, self.tamano['ancho'], lineaDivisionCarril, width=1, fill='gray')

    def dibujarOvalos(self, particulas):
        for particula in particulas:
            x = particula.posicion[0]
            y = particula.posicion[1]

            self.canvas.delete(particula.dibujo)  # Borra el dibujo anterior

            # Dibuja el circulo
            dibujo = self.canvas.create_rectangle(x, y, x + particula.ancho, y + particula.alto, fill=particula.color)
            particula.setDibujo(dibujo)

    def mostrar(self):
        self.ventana.mainloop()