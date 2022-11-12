from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatBot = ChatBot("Chatbot")
trainer = ChatterBotCorpusTrainer(chatBot)


trainer.train("chatterbot.corpus.english")
print("Hello__ I Am A Assistant Of You ")

while True:
    Query = input(">>>")
    print(chatBot.get_response(text=Query,search_text=Query))
