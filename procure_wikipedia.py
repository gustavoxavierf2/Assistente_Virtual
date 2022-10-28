#deve-se baixar estas biblioetas antes da sua utilizaçao 
import pyttsx3 #vozPython.setProperty('volume', 0.7)
import wikipedia


def procure_wikipedia(executar):
    executado = False 
    vozPython = pyttsx3.init()
    if "procure" in executar:
        procura = executar.replace("procure", "")
        wikipedia.set_lang('pt')
        result_procura = wikipedia.summary(procura, 2)
        print(result_procura)
        vozPython.say(result_procura)
        vozPython.runAndWait()
        executado = True
    return executado
        