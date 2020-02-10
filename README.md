# Web Scraping + Bot Telegram

PT-BR
-------
Projeto com o objetivo de aprender um pouco mais de Python (primeiro contato com a linguagem), ferramentas de Web Scraping e integração com a criação de um Bot para Telegram.

<h4>Objetivo:</h4> 
Recolher os dados de escanteios, chutes e ataques perigoso dos times de casa e fora. Se houver 80 ataques perigosos ou mais para um time, ou a soma de escanteios e chutes for igual ou superior a 15, o bot enviará o link do jogo e os dados acima por Telegram.

<h4>Bibliotecas utilizadas:</h4> 

* requests (baixar o HTML da página web)
* BeautifulSoup (html parser)
* telepot (integração com telegram)
* time (usada para controlar o tempo de atualização do programa)
* datetime (usada para comparar o horário atual com o horário de input)
* re (retirar as partes indesejadas do código html)
