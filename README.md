# Web Scraping + Bot Telegram

Objective of learn more about Python (first project with the language), web scraping tools, and integration with telegram bot.

<h4>Objective:</h4> 
Get data of corners kicks, shots, dangerous attacks of both teams (home and away) of ANY MATCH. If the match has more or equal than 80 dangerous attacks for a team or the sum of corners kicks and shots are equal or more than 15, the telegram bot will send the link of the game and the data.

<h4>Libraries:</h4> 

* requests (download the html from web page).
* BeautifulSoup (html parser).
* telepot (for using telegram bot).
* time (use to control refresh time of program).
* datetime (use to compare the actuall time with input match time).
* re (remove the unwanted parts of html code).

<h4>Web site choosed for web screping:</h4>

* www.livescore18.com (any live or finished game).
- Example: https://www.livescore18.com/football-match/inter-milan-vs-ac-milan/summary-1763623/

<h4>How should be the input:</h4>

* First line: numberOfMatches.
* nLines 1: url of page.
* nLines 2: hour of beginning of match. (always +1 hour of the actual hour of the start of event).
* Example: [Input Example].

<h4>Bugs</h4>

- When there is a red card in the match, a new div is created in 'barData' class, as I am using only the next_sibling(from BeautifulSoup), the captured data become displaced. So, instead of div 'shots', I get the data from 'red cards' and instead of 'dangerous attacks', I get only the data from 'attacks' div. 
- I tried to read txt files, where would be urls and the time of beginning of the matches, but, for a reason that I don't now, BeautifulSoup gives an error when tried to read the string.
- (FIXED) When the match isn't started yet, the 'barData' class does not exists, which gives an error and stop the program.
FIX: add the time of beginning of the match at the input (always +1 hour of the actual hour of the start of event), comparing this with the actual time (datetime library). (It was not possible to get the hour of the event from the site).

<h4>Data that I wanted to grab:</h4>
<img src="https://github.com/lucabenetti/webscraping-bottelegram/blob/master/datacatch.png" data-canonical-src="https://github.com/lucabenetti/webscraping-bottelegram/blob/master/datacatch.png" width="593" height="196" />

<h4>Print in Telegram of bot working:</h4> 

<img src="https://github.com/lucabenetti/webscraping-bottelegram/blob/master/printOfTelegram.png" data-canonical-src="https://github.com/lucabenetti/webscraping-bottelegram/blob/master/printOfTelegram.png" width="240" height="426" />

PT-BR
-------
Projeto com o objetivo de aprender um pouco mais de Python (primeiro contato com a linguagem), ferramentas de Web Scraping e integração com a criação de um Bot para Telegram.

<h4>Objetivo:</h4> 
Recolher os dados de escanteios, chutes e ataques perigoso dos times de casa e fora de QUALQUER JOGO. Se houver 80 ataques perigosos ou mais para um time, ou a soma de escanteios e chutes for igual ou superior a 15, o bot enviará o link do jogo e os dados acima por Telegram.

<h4>Bibliotecas utilizadas:</h4> 

* requests (baixar o HTML da página web).
* BeautifulSoup (html parser).
* telepot (integração com telegram).
* time (usada para controlar o tempo de atualização do programa).
* datetime (usada para comparar o horário atual com o horário de input).
* re (retirar as partes indesejadas do código html).

<h4>Site utilizado para web scraping:</h4>

* www.livescore18.com (qualquer jogo ao vivo ou que ja foi finalizado).
- Exemplo: https://www.livescore18.com/football-match/inter-milan-vs-ac-milan/summary-1763623/

<h4>Como deve ser o input:</h4>

* Primeira linha: numeroDeJogos.
* nLinhas 1: link do site.
* nLinhas 2: horário de inicio do jogo. (deve ser sempre adicionado +1 a hora real de inicio do evento).
* Exemplo: [Input Example].

<h4>Bugs encontrados:</h4>

- Quando há um cartão vermelho no jogo, é criada uma nova div no class 'barData', como estou usando apenas o next_sibling, os dados capturados são deslocados. Assim, no lugar da div chutes, recebo os dados de cartões vermelhos e no lugar de ataques perigoosos, recebo apenas ataques.
- (FIXED) Quando o jogo não é iniciado, a class barData ainda não existe, resultando em um erro e fim do porgrama.
FIX: acrescentar o dado horário no input (que deve ser sempre adicionado +1 a hora real de inicio do evento), comparando ele com a hora real. (não foi possível pegar o horário do próprio site por meio de webscraping).
- Tentei ler arquivos txt, onde estariam os links e horários dos jogos, mas por alguma razão o BeautifulSoup dava erro ao ler a string.

[Input Example]: https://github.com/lucabenetti/webscraping-bottelegram/blob/master/input%20example.txt
