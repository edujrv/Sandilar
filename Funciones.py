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






def urlDriveLinker(canal_actual):
    #Devolvera la url correspondiente
    linker = {"redes-i":"https://drive.google.com/drive/folders/1S_9u3_qWH9nX5JB5WYbZIcgyqFtNJsT1",
     "auditoria":"https://drive.google.com/drive/folders/1EsHvUGxkfPzXzw1xdT_ujZEQDerINIJG",
     "pds-ii":"https://drive.google.com/drive/u/0/folders/1vi8Q7yHjc1fGg95ENiWCOLVM6Hy_5lMD",
     "organizacion-de-empresas":"https://drive.google.com/drive/u/0/folders/1VwF5FGe1cWf5FJSJp9OzPBqy2UIQY9SU",
     "desarrollo-de-herramientas-de-software":"https://drive.google.com/drive/u/0/folders/1tXO6Go3e5CbsJ7OoJhVv6JCI34tg6ZpV",
     "derecho-y-etica-pro":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8qbOHYcguS9vGdg596WQJsScJiCMdR1wOG5fqjy_9VZqcZ3d_6mTh_mzgk3U8qIasjuk&usqp=CAU"
  

  #...
    }
    print("\n\n\n")
    print(canal_actual)
    print("\n\n\n")
    print(linker.get(canal_actual))
    print("\n\n\n")
    
    return linker.get(canal_actual)







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
