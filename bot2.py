# -*- coding: utf8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Aula')

lista = ['oii', 'olá, bem vindo',
        'posso te ajudar?', 'sim, qual seu nome?', 
        'Meu nome é ChatBot', 'Esse é meu nome']


bot.set_trainer(ListTrainer)

bot.train(lista)

while True:
    
    request = input('Usuário: ')

    response = bot.get_response(request)

    if float(response.confidence) > 0.5:

        print('ChatBot: ', response)

    else:

        print('ChatBot: Não tenho certeza da resposta')
