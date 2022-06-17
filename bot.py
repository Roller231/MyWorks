import telebot
import os
import config
from telebot import types
import random

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def privet(message):
    help1=types.ReplyKeyboardMarkup(resize_keyboard=True)
    helpi=types.KeyboardButton('/help')
    help1.add(helpi)
    bot.send_message(message.chat.id,'Привет, я бот помощник в игровой индустрии.\nНапиши "/help", и мы начнем', reply_markup=help1)
    
@bot.message_handler(commands=['help'])#Возможности бота
def funci(message):
    if message.text=='/help':
        funci1=types.InlineKeyboardMarkup()
        scrin=types.InlineKeyboardButton(text='1.Скрины', callback_data='scrin')
        audio=types.InlineKeyboardButton(text='2.Музыка', callback_data='audio')
        silka=types.InlineKeyboardButton(text='3.Ссылка', callback_data='silka')
        news=types.InlineKeyboardButton(text='4.Новости', callback_data='news')
        funci1.add(scrin, audio, silka, news)
        bot.send_message(message.chat.id, '1.Скрин из игры на выбор из списка \n 2.Музыка из игры, из списка \n 3.Новости об игровой индустрии \n 4.Ссылка на автора бота.', reply_markup=funci1)

@bot.callback_query_handler(func = lambda call: True)##Выбор из какой игры будет действие выбранное выше
def scrin(call):
    if call.data=='audio':
        audio2=types.ReplyKeyboardMarkup(resize_keyboard=True)
        Tlou=types.KeyboardButton('/TLOU_au')
        Cuphead=types.KeyboardButton('/Cuphead_au')
        Witcher=types.KeyboardButton('/Witcher_au')
        NFS=types.KeyboardButton('/NFS_au')
        Doom=types.KeyboardButton('/Doom_au')
        RDR=types.KeyboardButton('/RDR_au')
        Fortnite=types.KeyboardButton('/Fortnite_au')
        GTA=types.KeyboardButton('/GTA_au')
        FarCry=types.KeyboardButton('/FarCry_au')
        Help1=types.KeyboardButton('/help')
        audio2.add(Tlou,Cuphead,Witcher,NFS,Doom,RDR,Fortnite,GTA,FarCry,Help1)
        bot.send_message(call.message.chat.id,'Скрин из какой игры вы хотите?', reply_markup=audio2)

    if call.data=='scrin':
        scrin2=types.ReplyKeyboardMarkup(resize_keyboard=True)
        Tlou=types.KeyboardButton('/TLOU_sc')
        Cuphead=types.KeyboardButton('/Cuphead_sc')
        Witcher=types.KeyboardButton('/Witcher_sc')
        NFS=types.KeyboardButton('/NFS_sc')
        Doom=types.KeyboardButton('/Doom_sc')
        RDR=types.KeyboardButton('/RDR_sc')
        Fortnite=types.KeyboardButton('/Fortnite_sc')
        GTA=types.KeyboardButton('/GTA_sc')
        FarCry=types.KeyboardButton('/FarCry_sc')
        Help=types.KeyboardButton('/help')
        scrin2.add(Tlou,Cuphead,Witcher,NFS,Doom,RDR,Fortnite,GTA,FarCry,Help)
        bot.send_message(call.message.chat.id,'Скрин из какой игры вы хотите?', reply_markup=scrin2)
        
@bot.message_handler(commands=['TLOU_sc', 'Cuphead_sc', 'Witcher_sc', 'NFS_sc','Doom_sc','RDR_sc','GTA_sc','FarCry_sc','Fortnite_sc'])##скрины из игр
def get_scrin(message):
    if message.text=='/TLOU_sc':
        scrintlou=open('tlou_sc/' + random.choice(os.listdir('tlou_sc')), 'rb')
        bot.send_photo(message.from_user.id, scrintlou)
        bot.send_message(message.chat.id, 'Лови скрины из 2 и 1 части')
    elif message.text=="/Cuphead_sc":
        scrintlou=open('Cuphead_sc/' + random.choice(os.listdir('Cuphead_sc')), 'rb')
        bot.send_photo(message.from_user.id, scrintlou)
        bot.send_message(message.chat.id, 'Лови разнообразных босов капхеда')
    elif message.text=="/Witcher_sc":
        scrintlou=open('Witcher_sc/' + random.choice(os.listdir('Witcher_sc')), 'rb')
        bot.send_photo(message.from_user.id, scrintlou)
        bot.send_message(message.chat.id, 'Лови Геральта с Плотвой')
    elif message.text=="/NFS_sc":
        scrintlou=open('NFS_sc/' + random.choice(os.listdir('NFS_sc')), 'rb')
        bot.send_photo(message.from_user.id, scrintlou)
        bot.send_message(message.chat.id, 'Лови крутые кадры с дороги')
    elif message.text=="/Doom_sc":
        scrintlou=open('Doom_sc/' + random.choice(os.listdir('Doom_sc')), 'rb')
        bot.send_photo(message.from_user.id, scrintlou)
        bot.send_message(message.chat.id,'Лови крутые кадры из самой преисподнии')
    elif message.text=="/RDR_sc":
        scrintlou=open('RDR_sc/' + random.choice(os.listdir('RDR_sc')), 'rb')
        bot.send_photo(message.from_user.id, scrintlou)
        bot.send_message(message.chat.id,'Лови скрин, также как ковбои ловят лассом')
    elif message.text=="/Fortnite_sc":
        scrintlou=open('Fortnite_sc/' + random.choice(os.listdir('Fortnite_sc')), 'rb')
        bot.send_photo(message.from_user.id, scrintlou)
        bot.send_message(message.chat.id,'Лови скрин из Fortnite')
    elif message.text=="/GTA_sc":
        scrintlou=open('GTA_sc/' + random.choice(os.listdir('GTA_sc')), 'rb')
        bot.send_photo(message.from_user.id, scrintlou)
        bot.send_message(message.chat.id,'Лови скрин из GTA')
    elif message.text=="/FarCry_sc":
        scrintlou=open('FarCry_sc/' + random.choice(os.listdir('FarCry_sc')), 'rb')
        bot.send_photo(message.from_user.id, scrintlou)
        bot.send_message(message.chat.id,'Лови скрин из FarCry')

@bot.message_handler(commands=['TLOU_au','Cuphead_au'])
def get_audio(message):
    if message.text=='/TLOU_au':
        audio=open(r'C:\Users\lelyi\Desktop\Nice_Game_News\TLOU_au/' + random.choice(os.listdir('TLOU_au')), 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_audio(message.from_user.id,audio)

    elif message.text=='/Cuphead_au':
        audio=open(r'C:\Users\lelyi\Desktop\Nice_Game_News\Cuphead_au/' + random.choice(os.listdir('Cuphead_au')), 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_audio(message.from_user.id,audio)
bot.polling(none_stop = True)

