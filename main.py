# telegramBot2

# Wikipedia-бот. Gо введенному слову выдает статью на Википедии.

import telebot, wikipedia, re
from config import token

# создаем экземпляр бота
bot = telebot.TeleBot(token)

# Устанавливаем русский язык в википедии
wikipedia.set_lang("ru")


# Чистим текст статьи в википедии и ограничиваем его длину 1000 символов
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        # Получаем первую 1000 символов
        wikitext = ny.content[:1000]
        # Разделяем по точкам
        wikimas = wikitext.split('.')
        # отбрасываем все после последней точки
        wikimas = wikimas[:-1]
        # создаем пустую переменную для текста
        wikitext2 = ''
        # проходимся по строкам, где нет знаков "равно" (т.е всем, кроме заголовков)
        for x in wikimas:
            if not ('==' in x):
                # если в строке осталось более трех символов,
                # добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if (len((x.strip())) > 3):  # Не знаю зачем столько скобок, но без них не работает!
                    wikitext2 = wikitext2 + x + '.'
            else:
                break
        # теперь при помощи регулярных выражений убираем разметку
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
        # возвращаем текстовую строку
        return wikitext2
    # отрабатываем исключения, которые мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return "В энциклопедии нет информации об этом"


# Функция, отрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Отправьте мне любое слово и я найду его значение в Wikipedia')


# получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))


# запускаем бота
bot.polling(none_stop=True, interval=0)
