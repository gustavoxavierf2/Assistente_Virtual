#deve-se baixar estas biblioetas antes da sua utilizaçao 
import speech_recognition as sr #biblioteca do reconheimento de fala
from playsound import playsound

from ouvir_microfone import ouvir_microfone
from executor_Apps import executor_Apps
from funcionalidades_Sistema import funcionalidades_Sistema
from procure_wikipedia import procure_wikipedia
from videos_YT import videos_YT

repete = True #variavel de controle
while repete != False: 
    try:   
        audio = ouvir_microfone()
        if("Python" in audio):
            executado = False
            playsound('escuto_Intro.mp3')
            audio = audio.replace("Python", "")        
            executado = executor_Apps(audio)
            
            executado = funcionalidades_Sistema(audio)
            
            executado = procure_wikipedia(audio)
            
            executado = videos_YT(audio)
            if(executado != True):
                print('\t[ comando invalido! ]')       
        elif "desativar" in audio:  #desativar a escuta
            #global repete 
            repete = False       
    except sr.UnknownValueError:#caso n seja reconhecido nenhum padrao de fala gera a exceçao         
        print('vc disse algo? fale python para interagir comigo')
print('\n\tEND...')