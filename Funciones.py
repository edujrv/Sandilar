import datetime
import random
import discord

def recordatorio_constructor(frase):
    frase = frase.replace("$na ", "").split(";")
    #    frase = frase.split(";")
    frase_final = ["?", "?", "?", "?", "?", "?", "?"]

    fecha = frase[0].split("/")
    desc = frase[-1]
    hora = ["?", "?"]
    materia = "?"

    if (len(fecha) == 1):
        fecha.append(str(datetime.now().month))
        fecha.append(str(datetime.now().year))
    elif (len(fecha) == 2):
        fecha.append(str(datetime.now().year))

    if (len(frase) == 3):  #Puede ser hora o materia
        frase_aux = frase[1].split(":")
        if (frase_aux[0].isnumeric()):  #Se trata de una hora
            hora[0] = frase_aux[0]
            if (len(frase_aux) == 1):  #Solo hora
                hora[1] = "00"
            else:  #hora y minuto
                hora[1] = frase_aux[1]
        else:  #Es la materia
            materia = frase[1]

    if (len(frase) == 4):
        frase_aux = frase[1].split(":")
        hora[0] = frase_aux[0]
        if (len(frase_aux) == 1):  #Solo hora
            hora[1] = "00"
        else:  #hora y minuto
            hora[1] = frase_aux[1]
        materia = frase[2]

    frase_final[0] = fecha[0]
    frase_final[1] = fecha[1]
    frase_final[2] = fecha[2]

    frase_final[3] = hora[0]
    frase_final[4] = hora[1]

    frase_final[5] = materia.lower()

    frase_final[6] = desc.lower()

    print(frase_final)
  
    return frase_final


def bardeo():
    file = open("insultos.txt")

    contenido = file.readlines()

    palabras = []

    for line in contenido:
        palabras.append(line.replace('\n', ''))

    return palabras[random.randint(0, len(palabras) - 1)]


def get_agendado(frase):
    dia = frase[0]
    mes = frase[1]
    ano = frase[2]
    hora = frase[3]
    minuto = frase[4]
    materia = frase[5]
    descripcion = frase[6]

    print("\n\n\n")
#        print(frase)

    agendado = dia + "/" + mes + "/" + ano + " - "
    if (not hora == '?'):
        agendado += hora
    if (not minuto == '?'):
        agendado += ":" + minuto + " - "
    if (not materia == '?'):
        agendado += materia + " - "
    agendado += descripcion

    return agendado
