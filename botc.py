import telebot # importamos la libreria de telebot
bot = telebot.TeleBot('1931770782:AAEdUhKwUw4o1dB_7wokf82xSejeFeMjPcg') #anadimos el token
updates = bot.get_updates()
message = updates[0].message
from_user = message.from_user
id = from_user.id
get_me = bot.get_me()
@bot.message_handler(commands=['hola']) 
def hola(mensaje):
    bot.reply_to(mensaje, "Hola")
    print("Mandaron hola")
@bot.message_handler(commands=['celsius']) 
def hola(mensaje):
    bot.reply_to(mensaje, " ºF = (ºC · 1,8) + 32")
    
@bot.message_handler(commands=['farenheit']) 
def hola(mensaje):
    bot.reply_to(mensaje, " ºC = (ºF -32) / 1,8")
 
bot.polling()