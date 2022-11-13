#deve-se baixar estas biblioetas antes da sua utilizaçao 
import os #bibliotea de acesso ao sistema operaional
import gtts
from playsound import playsound

controle_Save = False#variavel que verifica se o arquivo ja foi salvo na pasta ou não
def executor_Apps(executar):
    try:
        executado = False
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
            executado = True
                
        elif "spotify" in executar:
            with open('musica.txt', 'r') as arquivo:#abrindo o arquivo de texto, [arquivo] e o objeto - 'r' é read/leitura.
                for linha in arquivo:#laço for q cria a variavel linha q recebe os dados do arquivo 
                    executarS = gtts.gTTS(linha,lang='pt-br')#variavel executar recebe a transriçao do arquivo txt, lang='portugues'
                    if(controle_Save != True):#condiçao se o arquivo.mp3 ja existe no diretorio
                        executarS.save('musica.mp3') #objeto executar usa o metodo save e define o nome do arquivo mp3
                    playsound('musica.mp3')#tocando o arquivo
            os.system("start Spotify.exe")
            controle_Save=True
            executado = True
        return executado
    except Exception as erro:
        print('houve um erro inexperado, [tente novemente mais tarde]\n\t=  codigo de erro [002]')

                