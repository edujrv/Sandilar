import Funciones 

def evento(client):
   
    @client.event
    async def on_message(message):

        if message.author == client.user:
            return

        def mandar_mensaje(texto):
            return message.channel.send(texto)
           
        mensaje = message.content.split(" ")
        if (mensaje[0] == "$tony"):
            await mandar_mensaje('tony es un bot y pancho barbaro')
            await mandar_mensaje('https://media.discordapp.net/attachments/698233666601484379/880130562956853258/unknown.png')
    

        elif (mensaje[0] == "$hater"):
            if(len(message.mentions) == 0):
                await mandar_mensaje('Para hatear , tenes que tener odio por alguien, mencionalo y lo destrozo perri')
            else:
                await mandar_mensaje(
                    'Segun paginas oficiales como Wikipedia y resultados analiticos de laboratorios de investigacion a nivel mundial, esta comprobado que ' + message.mentions[0].mention + ' es el mas hater')
              
                
        elif (mensaje[0] == "$klan"):
            await mandar_mensaje('El mas kaka kaka del universo')
            await mandar_mensaje(
                'https://media.discordapp.net/attachments/881890595747024937/881890655868178482/Klan_dios.png')

        elif (mensaje[0] == "$ricto"):
            await mandar_mensaje('Lo siento homie')

        elif (mensaje[0] == "$autobardear"):
            await mandar_mensaje(message.author.mention + ' es un un uachin')

        elif (mensaje[0] == "$horario"):
            await mandar_mensaje(
                'https://media.discordapp.net/attachments/821355545838485535/877535911309635624/unknown.png'
            )

        elif (mensaje[0] == "$sandi"):
            await mandar_mensaje('Este soy yo, bonito no?')
            await mandar_mensaje(
                'https://cdn5.dibujos.net/dibujos/pintados/201627/trozo-de-sandia-comida-frutas-10712724.jpg'
            )

        elif (mensaje[0] == "$help"):
            await mandar_mensaje(
                'Te voy a dar una ayudita, puedes usarme con: \n```▁ ▂ ▄ ▅ ▆ ▇ █ 𝕃𝕀𝕊𝕋𝔸 𝔻𝔼 ℂ𝕆𝕄𝔸ℕ𝔻𝕆𝕊 █ ▇ ▆ ▅ ▄ ▂ ▁\n$tony\n$hater\n$klan ♥\n$ricto\n$autobardear\n$horario\n$sandi\n$celebrar\n$bardear\n$na\n$na\n$go```'
            )

        elif (mensaje[0] == "$celebrar"):
            await mandar_mensaje('¡¡A CELEBRAR!!')
            await mandar_mensaje('https://i.pinimg.com/originals/c9/ae/85/c9ae85b4431228f0d59e2ab9e4515378.gif')

        elif (mensaje[0] == "$bardear"):
            await mandar_mensaje(message.mentions[0].mention + " sos un " + Funciones.bardeo())

        elif (mensaje[0] == "$na"):
            frase = Funciones.recordatorio_constructor(message.content)
        
            agendado = Funciones.get_agendado(frase)
           # anot = Funciones.Anotacion(frase)
            
            print("\n\n------- AGENDADO --------\n")
            print(agendado)

            await mandar_mensaje(agendado)

            cond_descripcion = False
            descripcion = ""
            for i in mensaje:
                if i == ' " ' and cond_descripcion == False:
                    cond_descripcion = True
                    continue
                if i == ' " ' and cond_descripcion == True:
                    cond_descripcion = True
                    break
                if cond_descripcion:
                    descripcion += i
            print(descripcion)

        elif (mensaje[0] == "$go"):
            #Ir a la carpeta Drive de la materia
            canal_actual = message.channel
            
            url = Funciones.urlDriveLinker(str(canal_actual))

            await mandar_mensaje(url)