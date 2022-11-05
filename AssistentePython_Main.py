#deve-se baixar estas biblioetas antes da sua utilizaçao 
import speech_recognition as sr #biblioteca do reconheimento de fala
from playsound import playsound

from ouvir_microfone import ouvir_microfone
from executor_Apps import executor_Apps
from funcionalidades_Sistema import funcionalidades_Sistema
from procure_wikipedia import procure_wikipedia
from videos_YT import videos_YT

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
            
            executado = funcionalidades_Sistema(audio)
            
            executado = procure_wikipedia(audio)
            
            executado = videos_YT(audio)
                  
        elif "desativar" in audio:  #desativar a escuta     
            repete = False 
        elif(executado == False):
                print('\t[ comando invalido! ]')         
    except sr.UnknownValueError:#caso n seja reconhecido nenhum padrao de fala gera a exceçao         
        print('vc disse algo? fale python para interagir comigo')
print('\n\tEND...')