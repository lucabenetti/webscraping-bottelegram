import requests
import time
import re
import telepot
import datetime
from bs4 import BeautifulSoup

bot = telepot.Bot("----ID BOT----") #id token from telegram bot

linkJogos = [] #store n links of the matches
horaJogos = [] #store n hour of start of the matches
flagJogos = [] #flag to not send again, if a message has already sent by the bot
abriuJogos = []#flag if the game has already started or not

print('Quantidade de jogos:') #'number of matches'
n = input() #input the number of matches
n = int(n)

for i in range(n):
        print('Link do jogo ' + str(i+1) + ':') #'link of match'
        entrada = input() #input the link of match i
        linkJogos.append(entrada) #insert link into linkJogos
        print('Horario do jogo ' + str(i+1) + ':') #'hour of beginning of match'
        entrada = input() #input of hour of beginning of match i
        entrada = int(entrada)
        horaJogos.append(entrada) #insert hour of beginning of match into horaJogos
        flagJogos.append(1) #set flagJogos[i] = 1 (game has not sent by bot yet)
        abriuJogos.append(0) #set abriuJogos[i] = 0 (game has not started yet)

while(1): #it does not stop

    for i in range(n): #loop between all games
        now= datetime.datetime.now() #now receives actual time
        print(now.hour) #print hour
        print(now.minute) #print minute

        print(linkJogos[i]) #print the link of the match

        if (now.hour >= horaJogos[i]) or abriuJogos[i]: #if the actual hour is >= time of beginning of match i (now.hour >= horaJogos[i]) or match has already started (abriuJogos[i]) it continues
            abriuJogos[i] = 1 #match i already started

            page = requests.get(linkJogos[i]) #request page
            if page.status_code == 200: #confirm if the request was successful
                print('Requisição bem sucedida!') #'request was succesful'
 
            soup = BeautifulSoup(page.text, 'html.parser') #create the tree of html elements

            br = soup.find(class_= 'barData') #find where class are the information that I in interested in

            CornerKicksHome = br.div.div.text #Corner Kicks Home receive is the first element in the class, receiving the text
            CornerKicksAway = br.div.find('div', class_='guest')#Corner Kicks Away is forward, and with class guest
            CornerKicksAway = CornerKicksAway.text #receiveing just the text part of the div

            cornerhome = re.sub(r'\D', '', CornerKicksHome) #remove spaces and break lines from the string
            cornerhome = int (cornerhome) #str to int
            corneraway = re.sub(r'\D', '', CornerKicksAway) #remove spaces and break lines from the string
            corneraway = int (corneraway) #str to int

            print('Escanteios') #'corners'
            print(cornerhome)
            print(corneraway)

            #next part of web scraping is done just with next_sibling, because all the information needed is in the same class
            #i am interested just in corners kicks, shots and dangerous atacks, so i jumped some div (like yellow cards)

            ShotsHome = (br.div.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.div.text) #get text from next div - shots home
            ShotsAway = (br.div.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.find('div', class_='guest')) #get text from class guest - shots away
            ShotsAway = ShotsAway.text #receive just the text

            shothome= re.sub(r'\D', '', ShotsHome) #remove spaces and break lines from the string
            shothome= int(shothome) #str to int
            shotaway= re.sub(r'\D', '', ShotsAway) #remove spaces and break lines from the string
            shotaway= int(shotaway) #str to int
            print('Chutes') #'shots'
            print(shothome) 
            print(shotaway)

            DangerousHome = br.div.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.div.text #get text from next div - dangerous attacks home
            DangerousAway = br.div.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.find('div', class_='guest') #get text from class guest - dangerous attacks away
            DangerousAway = DangerousAway.text #receive just the text

            dangerousathome = re.sub(r'\D', '', DangerousHome) #remove spaces and break lines from the string
            dangerousathome = int(dangerousathome) #str to int
            dangerousataway = re.sub(r'\D', '', DangerousAway) #remove spaces and break lines from the string
            dangerousataway = int(dangerousataway) #str to int
            print('Ataques Perigosos') #'dangerous attacks'
            print(dangerousathome)
            print(dangerousataway)

            #PART OF TELEGRAM BOT

            if(flagJogos[i] and (dangerousathome >=80 or dangerousataway >=80 or (shothome+cornerhome) >= 15 or (shotaway+corneraway) >= 15)): #if the message about the game has already sent (flagJogos[i]) it does not send again; the send of message will happen if a team have more or equal than 80 dangerous attacks or the sum of shots and corners is equal or more than 15
                dangerousathome = str(dangerousathome) #int to str
                dangerousataway = str(dangerousataway) #int to str
                shothome = str(shothome) #int to str
                shotaway = str(shotaway) #int to str
                cornerhome = str(cornerhome) #int to str
                corneraway = str(corneraway) #int to str
                mensagem = linkJogos[i] + '\n\n*Ataques Perigosos*\nCasa: ' + dangerousathome + ' Fora: ' + dangerousataway + '\n\n*Chutes*\nCasa: ' + shothome + ' Fora: ' + shotaway + '\n\n*Escanteios*\nCasa: ' + cornerhome + ' Fora: ' + corneraway + '\n\n' #string 'mensagem' will be sent by telegram bot 
                bot.sendMessage(-----CHAT ID-----, mensagem, parse_mode = 'Markdown') #bot send message using markdown
                flagJogos[i] = 0 #that game i receives 0, so it will not sent messages anymore
        else:
            print('Partida não começou!') #if actual hour is less (before) of the beginning of the match i, print 'match isn't started yet'          
    time.sleep(300) #wait 5 minutes to reload and scan all the matches
