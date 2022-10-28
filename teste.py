#deve-se baixar estas biblioetas antes da sua utilizaçao 
from time import sleep
import speech_recognition as sr #biblioteca do reconheimento de fala
import os #bibliotea de acesso ao sistema operaional
import gtts
from playsound import playsound

repete = True #variavel de controle
controle_Save = False#variavel que verifica se o arquivo ja foi salvo na pasta ou não
def ouvir_mirofone(): #funçao que ouve e reconhee a fala   
    microfone = sr.Recognizer() #habilita o microfone  
    with sr.Microphone() as source:#com o objeto (sr) utilizamos a funçao (microphone) e atribuimos a variavel (source)  
        print('[ Diga PYTHON para interagir comigo ]')     
        microfone.adjust_for_ambient_noise(source)#chama o algoritmo de reduçao de ruidos              
        audio = microfone.listen(source)#funçao q ouve oq foi dito e armazena na variavel    
    try: #tratamento de exceçoes            
        iniciador = microfone.recognize_google(audio,language='pt-BR')#funçao de reconhecimento da fala/de padroes, base de dados do deep learning
        #print(iniciador)      
        if("Python" in iniciador):
            print('LISTEN: ...') 
            playsound('escuto_Intro.mp3')
            with sr.Microphone() as source:
                audio2 = microfone.listen(source)                 
                executar = microfone.recognize_google(audio2,language='pt-BR')
            #print(executar)
            if "navegador" in executar:
                global controle_Save
                with open('navegador.txt', 'r') as arquivo:#abrindo o arquivo de texto, [arquivo] e o objeto,  'r' é read/leitura.
                    for linha in arquivo:#laço for q cria a variavel linha q recebe os dados do arquivo 
                        executarN = gtts.gTTS(linha,lang='pt-br')#variavel executar recebe a transcriçao do arquivo txt, lang='portugues'
                        if(controle_Save != True):#condiçao se o arquivo.mp3 ja existe no diretorio
                            executarN.save('arquivo.mp3') #objeto executar usa o metodo save e define o nome do arquivo mp3
                        playsound('arquivo.mp3')#tocando o arquivo                      
                os.system("start Opera.exe")#passa o arquivo que deve ser aberto apos encontrar a palavra determinada no (if)
                controle_Save=True 
            elif "Spotify" in executar:
                with open('musica.txt', 'r') as arquivo:#abrindo o arquivo de texto, [arquivo] e o objeto - 'r' é read/leitura.
                    for linha in arquivo:#laço for q cria a variavel linha q recebe os dados do arquivo 
                        executarS = gtts.gTTS(linha,lang='pt-br')#variavel executar recebe a transriçao do arquivo txt, lang='portugues'
                        if(controle_Save != True):#condiçao se o arquivo.mp3 ja existe no diretorio
                            executarS.save('musica.mp3') #objeto executar usa o metodo save e define o nome do arquivo mp3
                        playsound('musica.mp3')#tocando o arquivo
                os.system("start Spotify.exe")
                controle_Save=True
            else: 
                print('\tcomando invalido!')   
                     
        elif "desativar" in iniciador:  #desativar a escuta
            global repete 
            repete = False            
    except sr.UnknownValueError:#caso n seja reconhecido nenhum padrao de fala gera a exceçao         
            print('vc disse algo? fale python para interagir comigo')      
while repete != False:    
    ouvir_mirofone()#chama a funçao para q o codigo seja exeutado
print('\n\tEND...')