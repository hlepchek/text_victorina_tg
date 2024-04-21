import telebot
import random
from telebot import types
token="replace with your bot token"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
 bot.send_message(message.chat.id,"Привет сейчас мы с тобой поиграем в викторину по теме видиоигры.Напиши слово голубь чтобы начать игру.",reply_markup=types.ReplyKeyboardRemove())
@bot.message_handler(commands=['голубь'])
def vopros1(message):
  global msg
  msg = message.chat.id
  global klaviature
  klaviature = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
  btn = types.KeyboardButton("Майнкрафт")
  btn1 = types.KeyboardButton("Fortnite")
  btn2 = types.KeyboardButton("GTA V")
  btn3 = types.KeyboardButton("Марио")
  klaviature.add(btn, btn1, btn2, btn3)
  a=bot.send_message(msg, "Самая популярная игра в мире:", reply_markup=klaviature)
  bot.register_next_step_handler(a, vopros2)

def vopros2(message):

  global msgtxt
  klaviature = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
  msgtxt = message.text
  global ochki
  ochki = 0
  if msgtxt=="Майнкрафт":
    bot.send_message(msg, "Молодец! Ответ правильный, ты получаешь пять очков")
    ochki+=5
  elif msgtxt=="Fortnite"or"GTA V"or"Марио":
    bot.send_message(msg, "Ответ неправильный.")
  btn = types.KeyboardButton("1975")
  btn1 = types.KeyboardButton("1990")
  btn2 = types.KeyboardButton("1985")
  btn3 = types.KeyboardButton("1995")
  klaviature.add(btn, btn1, btn2, btn3)
  b=bot.send_message(msg, "В каком году вышла игра Марио?", reply_markup=klaviature)
  bot.register_next_step_handler(b, vopros3)

def vopros3(message):
  klaviature = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
  msgtxt = message.text
  global ochki
  if msgtxt=="1985":
    bot.send_message(msg, "Молодец! Ответ правильный, ты получаешь пять очков")
    ochki+=5
  elif msgtxt=="1975"or"1990"or"1995":
    bot.send_message(msg, "Ответ неправильный.")
  btn = types.KeyboardButton("Крипер")
  btn1 = types.KeyboardButton("Ендермен")
  btn2 = types.KeyboardButton("Чешуйница")
  btn3 = types.KeyboardButton("Магма слизень")
  klaviature.add(btn, btn1, btn2, btn3)
  c=bot.send_message(msg, "Как зовут персонажа из игры Майнкрафт, который умеет взрываться?", reply_markup=klaviature)
  bot.register_next_step_handler(c, vopros4)

def vopros4(message):
  klaviature = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
  msgtxt = message.text
  global ochki
  if msgtxt=="Крипер":
    bot.send_message(msg, "Молодец! Ответ правильный, ты получаешь пять очков")
    ochki+=5
  elif msgtxt=="Ендермен"or"Чешуйница"or"Магма слизень":
    bot.send_message(msg, "Ответ неправильный.")
  btn = types.KeyboardButton("PUBG MOBILE")
  btn1 = types.KeyboardButton("STANDOFF2")
  btn2 = types.KeyboardButton("BHOP PRO")
  btn3 = types.KeyboardButton("QUAKE III")
  klaviature.add(btn, btn1, btn2, btn3)
  d=bot.send_message(msg, "Как называется самый популярный аналог Counter-Strike для мобильных устройств?", reply_markup=klaviature)
  bot.register_next_step_handler(d, vopros5)

def vopros5(message):
  klaviature = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
  msgtxt = message.text
  global ochki
  if msgtxt=="STANDOFF2":
    bot.send_message(msg, "Молодец! Ответ правильный, ты получаешь пять очков")
    ochki+=5
  elif msgtxt=="PUBG MOBILE"or"BHOP PRO"or"QUAKE III":
    bot.send_message(msg, "Ответ неправильный.")
  btn = types.KeyboardButton("Три в ряд")
  btn1 = types.KeyboardButton("Тетрис")
  btn2 = types.KeyboardButton("Geometry Dash")
  btn3 = types.KeyboardButton("Crossword mobile")
  klaviature.add(btn, btn1, btn2, btn3)
  e=bot.send_message(msg, "Как называется игра, в которой фигуры разной формы падают и складываются в ряды?",reply_markup=klaviature)
  bot.register_next_step_handler(e, vopros6)

def vopros6(message):
  klaviature = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
  msgtxt = message.text
  global ochki
  if msgtxt=="Тетрис":
    bot.send_message(msg, "Молодец! Ответ правильный, ты получаешь пять очков")
    ochki+=5
  elif msgtxt=="Три в ряд"or"Geometry Dash"or"Crossword mobile":
    bot.send_message(msg, "Ответ неправильный.")
  btn = types.KeyboardButton("Genshin Impact")
  btn1 = types.KeyboardButton("The Legend of Zelda: Breath of the Wild")
  btn2 = types.KeyboardButton("Five Nights at Freddy’s")
  btn3 = types.KeyboardButton("Pokémon X и Y")
  klaviature.add(btn, btn1, btn2, btn3)
  f=bot.send_message(msg, "Какая игра является эксклюзивной для Nintendo Switch?",reply_markup=klaviature)
  bot.register_next_step_handler(f, vopros7)

def vopros7(message):
  klaviature = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
  msgtxt = message.text
  global ochki
  if msgtxt=="The Legend of Zelda: Breath of the Wild":
    bot.send_message(msg, "Молодец! Ответ правильный, ты получаешь пять очков")
    ochki+=5
  elif msgtxt=="Genshin Impact"or"Five Nights at Freddy’s"or"Pokémon X и Y":
    bot.send_message(msg, "Ответ неправильный.")
  btn = types.KeyboardButton("The Elder Scrolls V: Skyrim")
  btn1 = types.KeyboardButton("Minecraft")
  btn2 = types.KeyboardButton("GTA V")
  btn3 = types.KeyboardButton("Cyberpunk 2077")
  klaviature.add(btn, btn1, btn2, btn3)
  j=bot.send_message(msg, "В какой видеоигре самый большой открытый мир?",reply_markup=klaviature)
  bot.register_next_step_handler(j, vopros8)

def vopros8(message):
  klaviature = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
  msgtxt = message.text
  global ochki
  if msgtxt=="Minecraft":
    bot.send_message(msg, "Молодец! Ответ правильный, ты получаешь пять очков")
    ochki+=5
  elif msgtxt=="The Elder Scrolls V: Skyrim"or"GTA V"or"Cyberpunk 2077":
    bot.send_message(msg, "Ответ неправильный.")
  btn = types.KeyboardButton("стратегические")
  btn1 = types.KeyboardButton("Экшен")
  btn2 = types.KeyboardButton("Аркады")
  btn3 = types.KeyboardButton("гонки")
  klaviature.add(btn, btn1, btn2, btn3)
  h=bot.send_message(msg, "Какой жанр видеоигр является самым популярным в мире?",reply_markup=klaviature)
  bot.register_next_step_handler(h, vopros9)

def vopros9(message):
  klaviature = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
  msgtxt = message.text
  global ochki
  if msgtxt=="Экшен":
    bot.send_message(msg, "Молодец! Ответ правильный, ты получаешь пять очков")
    ochki+=5
  elif msgtxt=="стратегические"or"Аркады"or"гонки":
    bot.send_message(msg, "Ответ неправильный.")
  btn = types.KeyboardButton("Quake")
  btn1 = types.KeyboardButton("DUKE NUKEM 3D")
  btn2 = types.KeyboardButton("DOOM")
  btn3 = types.KeyboardButton("Wolfenstein 3D")
  klaviature.add(btn, btn1, btn2, btn3)
  i=bot.send_message(msg, "Назовите первую видеоигру с трехмерной графикой:",reply_markup=klaviature)
  bot.register_next_step_handler(i, vopros10)

def vopros10(message):
  klaviature = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
  msgtxt = message.text
  global ochki
  if msgtxt=="Wolfenstein 3D":
    bot.send_message(msg, "Молодец! Ответ правильный, ты получаешь пять очков")
    ochki+=5
  elif msgtxt=="Quake"or"DUKE NUKEM 3D"or"DOOM":
    bot.send_message(msg, "Ответ неправильный.")
  btn = types.KeyboardButton("Atomic Heart")
  btn1 = types.KeyboardButton("The SIMS")
  btn2 = types.KeyboardButton("CS2")
  btn3 = types.KeyboardButton("Street Fighter")
  klaviature.add(btn, btn1, btn2, btn3)
  p=bot.send_message(msg, "Какая игра из предложенных была экранизирована?",reply_markup=klaviature)
  bot.register_next_step_handler(p, vopros11)

def vopros11(message):
  msgtxt = message.text
  global ochki
  if msgtxt=="Street Fighter":
    bot.send_message(msg, "Молодец! Ответ правильный, ты получаешь пять очков")
    ochki+=5
  elif msgtxt=="CS2"or"The SIMS"or"Atomic Heart":
    bot.send_message(msg, "Ответ неправильный.")
  bot.send_message(msg, "Викторина окончена, ты набрал "+str(ochki)+" очков",reply_markup=types.ReplyKeyboardRemove())
bot.polling(none_stop = True)
