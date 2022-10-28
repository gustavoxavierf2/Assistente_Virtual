#deve-se baixar estas biblioetas antes da sua utilizaçao 
import pywhatkit

def videos_YT(executar):
    executado = False
    if "toque" in executar:
        p = executar.replace("toque", "")
        procure = pywhatkit.playonyt(p)
        executado = True
    return executado