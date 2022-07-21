import telebot
import os
import sys
token = sys.argv[1]
bot = telebot.TeleBot(token)
apk = os.listdir(path="bin")
apk = 'bin/' + str(apk[0])
f = open(str(apk), 'rb')
bot.send_document(646443633, f)

