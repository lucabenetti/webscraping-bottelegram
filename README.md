# Web Scraping + Bot Telegram

PT-BR
-------
Projeto com o objetivo de aprender um pouco mais de Python (primeiro contato com a linguagem), ferramentas de Web Scraping e integração com a criação de um Bot para Telegram.

Objetivo: 
Recolher os dados de escanteios, chutes e ataques perigoso dos times de casa e fora. Se houver 80 ataques perigosos ou mais para um time, ou a soma de escanteios e chutes for igual ou superior a 15, o bot enviará o link do jogo e os dados acima por Telegram.

Bibliotecas utilizadas:
requests (baixar o HTML da página web)
time (usada para controlar o tempo de atualização do programa)
datetime (usada para comparar o horário atual com o horário de input)
re (retirar as partes indesejadas do código html)
telepot (integração com telegram)
BeautifulSoup (html parser)

Site utilizado para web scraping: www.livescore18.com (qualquer jogo ao vivo ou que ja foi finalizado).
Exemplo: https://www.livescore18.com/football-match/inter-milan-vs-ac-milan/summary-1763623/

Como deve ser o input:
- Primeira linha: numerodeJogos.
- Nlinhas 1: link do site
- Nlinhas 2: horário de inicio do jogo.

Bugs encontrados:
- Quando há um cartão vermelho no jogo, é criada uma nova div no class 'barData', como estou usando apenas o next_sibling, os dados capturados são deslocados. Assim, no lugar da div chutes, recebo os dados de cartões vermelhos e no lugar de ataques perigoosos, recebo apenas ataques.

- (FIXED) Quando o jogo não é iniciado, a class barData ainda não existe, resultando em um erro e fim do porgrama.
	*'FIX': acrescentar o dado horário no input (que deve ser sempre adicionado +1 a hora real de inicio do evento), comparando ele com a hora real. (não foi possível pegar o horário do próprio site por meio de webscraping).

- Tentei ler arquivos txt, onde estariam os links e horários dos jogos, mas por alguma razão o BeautifulSoup dava erro ao ler a string.
	
