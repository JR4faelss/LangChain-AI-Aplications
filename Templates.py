
exemplos = [
    {"pergunta": "Quem viveu mais tempo, Muhammad Ali ou Alan Turing?", 
    "resposta": 
    """São necessárias perguntas de acompanhamento aqui: Sim. 
Pergunta de acompanhamento: Quantos anos Muhammad Ali tinha quando morreu? 
Resposta intermediária: Muhammad Ali tinha 74 anos quando morreu. 
Pergunta de acompanhamento: Quantos anos Alan Turing tinha quando morreu? 
Resposta intermediária: Alan Turing tinha 41 anos quando morreu. 
Então a resposta final é: Muhammad Ali 
""", 
    }, 
    {"pergunta": "Quando nasceu o fundador do craigslist?", 
    "resposta": 
"""São necessárias perguntas de acompanhamento aqui: Sim. 
Pergunta de acompanhamento: Quem foi o fundador do craigslist? 
Resposta intermediária: O craigslist foi fundado por Craig Newmark. 
Pergunta de acompanhamento: Quando nasceu Craig Newmark? 
Resposta intermediária: Craig Newmark nasceu em 6 de dezembro de 1952. 
Então a resposta final é: 6 de dezembro de 1952 
""", 
    }, 
    {"pergunta": "Quem foi o avô materno de George Washington?",
    "resposta": 
"""São necessárias perguntas de acompanhamento aqui: Sim. 
Pergunta de acompanhamento: Quem foi a mãe de George Washington? 
Resposta intermediária: A mãe de George Washington foi Mary Ball Washington. 
Pergunta de acompanhamento: Quem foi o pai de Mary Ball Washington? 
Resposta intermediária: O pai de Mary Ball Washington foi Joseph Ball. 
Então a resposta final é: Joseph Ball 
""", 
    },
    {"pergunta": "Os diretores de Jaws e Casino Royale são do mesmo país?", 
    "resposta": 
"""São necessárias perguntas de acompanhamento aqui: Sim. 
Pergunta de acompanhamento: Quem é o diretor de Jaws? 
Resposta Intermediária: O diretor de Jaws é Steven Spielberg. 
Pergunta de acompanhamento: De onde é Steven Spielberg? 
Resposta Intermediária: Estados Unidos. 
Pergunta de acompanhamento: Quem é o diretor de Casino Royale? 
Resposta Intermediária: O diretor de Casino Royale é Martin Campbell. 
Pergunta de acompanhamento: De onde é Martin Campbell? 
Resposta Intermediária: Nova Zelândia. 
Então a resposta final é: Não 
""",
    },
]


review_cliente = """Este soprador de folhas é bastante incrível. Ele tem 
quatro configurações: sopro de vela, brisa suave, cidade ventosa 
e tornado. Chegou em dois dias, bem a tempo para o presente de 
aniversário da minha esposa. Acho que minha esposa gostou tanto 
que ficou sem palavras. Até agora, fui o único a usá-lo, e tenho 
usado em todas as manhãs alternadas para limpar as folhas do 
nosso gramado. É um pouco mais caro do que os outros sopradores 
de folhas disponíveis no mercado, mas acho que vale a pena pelas 
características extras."""


texto_usuário = {'texto': """
                 This has been Oklahoma City's formula all season: Lose one game, respond in the next.

That's exactly what the Thunder did in Game 2 of the NBA Finals.

Shai Gilgeous-Alexander scored 34 points, Alex Caruso added 20 off the bench and the Thunder beat the Indiana Pacers 123-107 on Sunday night to tie these finals at one game apiece.

Jalen Williams scored 19, Aaron Wiggins had 18 and Chet Holmgren finished with 15 for the Thunder. It was the franchise’s first finals game win since the opener of the 2012 series against Miami.

“We did some things good tonight. We did some things bad,” Gilgeous-Alexander said. “We’ve got to be able to get better and be ready for Game 3.”

Tyrese Haliburton scored 17 for Indiana, which erased a 15-point, fourth-quarter deficit in Game 1 but never made a push on Sunday. Myles Turner scored 16 and Pascal Siakam added 15 for the Pacers, the first team since Miami in 2013 to not have a 20-point scorer in the first two games of the finals.

Game 3 is Wednesday at Indianapolis, in what will be the first finals game in that city in 25 years.

“A bad first half, obviously, was a big problem," Pacers coach Rick Carlisle said. “And we just played poorly. A little better in the second half. But you can’t be a team that’s reactive and expect to be successful or have consistency.”

Gilgeous-Alexander's first basket of the night was a history-maker: It gave him 3,000 points on the season, including the regular season and playoffs. And later in Game 2, he passed New York's Jalen Brunson (514) as the leading overall scorer in these playoffs.

But the real milestone for the MVP came a couple hours later, when he and most everybody else on the Thunder got a finals win for the first time.

A 19-2 run in the second quarter turned what was a six-point game into a 23-point Thunder lead. It might have seemed wobbly a couple of times - an immediate 10-0 rebuttal by the Pacers made it 52-39, and Indiana was within 13 again after Andrew Nembhard's layup with 7:09 left in the third - but the Thunder lead was never in serious doubt.

“They did a good job being disruptive,” Siakam said. “They got out in transition. ... They were super aggressive, which is what they do."

With the noise level in the building often topping 100 decibels - a chain saw is 110 dB, for comparison purposes - the Thunder did what they’ve done pretty much all season. They came off a loss, this time a 111-110 defeat in Game 1, and blew somebody out as their response.

Including the NBA Cup title game, which doesn't count in any standings, the Thunder are now 18-2 this season when coming off a loss. Of those 18 wins, 12 have been by double digits.

“That's a long 48 hours when you lose Game 1 like that, coming into Game 2,” Thunder coach Mark Daigneault said. “The guys did a great job of just focusing on what we needed to do to stack to a win tonight. That's how we got it.”
                 """}


wiki_speed = """
Darren Watkins Jr. nasceu em 21 de janeiro de 2005, em Cincinnati, Ohio. 
Em 2016, começou a criar seu canal no Youtube, onde publicava vídeos de jogos ocasionalmente.
Por volta de dezembro de 2017, Watkins começou a produzir livestreams de jogos, tal como Fortnite e NBA 2K, mas só conseguiu uma média de dois espectadores.
Eventualmente, sua contagem de assinantes aumentou em alguns meses, atingindo 100 mil assinantes em abril de 2021,
1 milhão em junho de 2021 e 10 milhões em julho de 2022.
Ele foi diagnosticado com cefaleia em salvas quando viajava pelo Japão entre o final de julho e o início de agosto de 2023.

Watkins começou a realizar transmissões ao vivo em 2019.
Ele se tornou proeminente em 2021 depois que sua base de fãs começou a postar clipes no TikTok de seu comportamento frequentemente violento durante transmissões ao vivo em relação a jogos,jogadores e sua câmera - que ganhou popularidade e se tornou viral. 
Suas "explosões de raiva" resultaram em banimentos da plataforma de streaming Twitch e do jogo Valorant.
Ele foi descrito pelo Kotaku como "um dos maiores e mais virais streamers" no YouTube.
Um jogo que contribuiu muito para o crescimento de sua popularidade é o Talking Ben.
Vídeos de Watkins sobre o jogo Talking Ben foram creditados por trazer a popularidade recém-descoberta do aplicativo móvel, tornando-o o jogo mais vendido na App Store mais de uma década após seu lançamento inicial.
"""