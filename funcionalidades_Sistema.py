#deve-se baixar estas biblioetas antes da sua utilizaçao 
import datetime

import pyttsx3  # vozPython.setProperty('volume', 0.7)
import pywhatkit
import wikipedia
import webbrowser


class funcionalidades_Sistema:
    try:
        def pesquisa(executar):
            executado = False
            if "abra" and "google" in executar:
                procura = executar.replace("pesquise", "")
                procura = executar.replace("google", "")
                webbrowser.get('windows-default').open_new(f'www.google.com.br/search?q={procura}')
                executado = True   
            return  executado
             
        def horario(executar):
            executado = False
            vozPython = pyttsx3.init()
            if "horário" in executar:
                horario = datetime.datetime.now().strftime("%H: %M") #pega o horario atual, strftime formataçao de hora - minuto
                fala = "agora são "+ horario
                vozPython.say(fala) #interpretaçao do texto
                vozPython.runAndWait()#execuçao da linha acima 
                executado = True   
            return  executado 
        
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

        def videos_YT(executar):
            executado = False
            if "toque" and 'youtube' in executar:
                p = executar.replace("toque", "")
                pywhatkit.playonyt(p)
                executado = True
            else:
                print('\t[ comando invalido! ]')    
            return executado
        
    except Exception as erro:       
        print('Ocorreu um erro inexperado na API`s solicitada, [tente novemente mais tarde]\n\t= codigo de erro [003]')     