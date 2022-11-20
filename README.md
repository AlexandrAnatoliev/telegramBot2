# telegramBot2
[Ru] Wikipedia-бот. По введенному слову выдает статью на Википедии.

## Требования:
* $ pip install -r requirements.txt
* создать файл config.py, в котором будут храниться токен для доступа к боту в виде
```python 
token = "1234567890:ASDFGHH..."
```

## Где взять token?
* https://xakep.ru/2021/11/28/python-telegram-bots/

## Подключаем модули
```python
import telebot, wikipedia, re
from config import token
```

## Примеры использования

#### Функция, отрабатывающая команду /start
```python
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Отправьте мне любое слово и я найду его значение в Wikipedia')
```

#### Запускаем бота
```python
bot.polling(none_stop=True, interval=0)
```