from nltk.chat.util import Chat, reflections # Se debe instalar la librearía NTKL a través del pip en el cmd en Winfows o terminal en Linux
pares = [# En esta parte del codigo, se le colocan los atributos para que el chatbot responda a las pregunta que uno ser humano le plantea.
    [
        r"mi nombre es (.*)",
        ["Hola %1, como estas ?",]
    ],
     [
        r"cual es tu nombre ?",
        ["Mi nombre es Chatbot ?",]
    ],
    [
        r"como estas ?",
        ["Bien, y tu?",]
    ],
    [
        r"disculpa (.*)",
        ["No pasa nada",]
    ],
    [
        r"hola|hey|buenas",
        ["Hola", "Que tal",]
    ],
    [
        r"que (.*) quieres ?",
        ["Nada gracias",]
        
    ],
    [
        r"(.*) creado ?",
        ["Fui creado hoy",]
    ],
    [
        r"finalizar",
        ["Chao","Fue bueno hablar contigo"]
],
]
def chatear():
    print("Hola soy un bot, escribe algo para comenzar") #mensaje por defecto
    chat = Chat(pares)
    chat.converse()
if __name__ == "__main__":
    chatear()