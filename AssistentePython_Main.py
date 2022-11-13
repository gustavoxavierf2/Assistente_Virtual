#deve-se baixar estas biblioetas antes da sua utilizaçao 
import speech_recognition as sr #biblioteca do reconheimento de fala
from playsound import playsound

import funcionalidades_Sistema as func
from ouvir_microfone import ouvir_microfone
from executor_Apps import executor_Apps


global repete
repete = True #variavel de controle
while repete != False: 
    executado = False
    try:   
        audio = ouvir_microfone()
        if("python" in audio):   
            playsound('escuto_Intro.mp3')
            audio = audio.replace("python", "")
            executado = executor_Apps(audio) 
            
            executado = func.funcionalidades_Sistema.horario(audio)
            
            executado = func.funcionalidades_Sistema.procure_wikipedia(audio)
            
            executado = func.funcionalidades_Sistema.pesquisa(audio)
            
            executado = func.funcionalidades_Sistema.videos_YT(audio)
                  
        elif "desativar" in audio:  #desativar a escuta     
            repete = False 
        elif(executado == False):
                print('\t[ comando invalido! ]')         
    except sr.UnknownValueError:#caso n seja reconhecido nenhum padrao de fala gera a exceçao         
        print('vc disse algo? fale python para interagir comigo')
    except Exception as erro:
        print()
print('\n\tEND...')