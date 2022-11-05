#deve-se baixar estas biblioetas antes da sua utilizaçao 
import pyttsx3 #vozPython.setProperty('volume', 0.7)
import datetime

def funcionalidades_Sistema(executar):
    executado = False
    vozPython = pyttsx3.init()
    if "horário" in executar:
        horario = datetime.datetime.now().strftime("%H: %M") #pega o horario atual, strftime formataçao de hora - minuto
        fala = "agora são "+ horario
        vozPython.say(fala) #interpretaçao do texto
        vozPython.runAndWait()#execuçao da linha acima 
        executado = True
        
    return  executado               