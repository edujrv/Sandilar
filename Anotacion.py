from datetime import date
from datetime import datetime


class Anotacion:

    anotacion = ["?", "?", "?", "?", "?", "?", "?", "?"]

    #                año-mes-dia-hora-min-mat-desc-id

    def __init__(self, nueva_anotacion):
        print("Nueva anotacion")

        for i in range(7):
            self.anotacion[i] = nueva_anotacion[i]

        print("ESTOY EN LA CLASE")
        print(self.anotacion)

    def agregar_anotacion(frase):
        return

    def set_fecha():
        return

    def set_hora():
        return

    def set_materia():
        return

    def set_descripcion():
        return

    def set_id():
        return

    def get_fecha():
        return

    def get_hora():
        return

    def get_materia():
        return

    def get_descripcion():
        return

    def get_id():
        return

    def ver_anotaciones():
        return

    def ver_recientes():
        return

    def eliminar_anotacion(id):
        return

    def cambiar_fecha_hora(id, fecha, hora):
        return
