#deve-se baixar estas biblioetas antes da sua utilizaçao 
import speech_recognition as sr #biblioteca do reconheimento de fala

def ouvir_microfone(): #funçao que ouve e reconhee a fala   
    microfone = sr.Recognizer() #habilita o microfone  
    with sr.Microphone() as source:#com o objeto (sr) utilizamos a funçao (microphone) e atribuimos a variavel (source)  
        print('[ Diga PYTHON para interagir comigo ]')     
        microfone.adjust_for_ambient_noise(source)#chama o algoritmo de reduçao de ruidos              
        audio = microfone.listen(source)#funçao q ouve oq foi dito e armazena na variavel                
        iniciador = microfone.recognize_google(audio,language='pt-BR')#funçao de reconhecimento da fala/de padroes, base de dados do deep learning
        #print(iniciador) 
    return iniciador      
