#deve-se baixar estas biblioetas antes da sua utilizaçao 
import pyttsx3 #vozPython.setProperty('volume', 0.7)
import wikipedia

def procure_wikipedia(executar):
    vozPython = pyttsx3.init()
    comandos_Alternativos = ['procure', 'quem foi', 'quem é', 'quem são']
    
    executado = False 
    for comandos in comandos_Alternativos:  
        #print(comandos)
        if comandos in executar:
            procura = executar.replace(comandos, "")
            wikipedia.set_lang('pt')
            result_procura = wikipedia.summary(procura, 2)
            print(result_procura)
            vozPython.say(result_procura)
            vozPython.runAndWait()
            executado = True 
            break   
        
    return executado
'''if __name__ == "__main__":
    print("gg",procure_wikipedia('procure'))'''
    

