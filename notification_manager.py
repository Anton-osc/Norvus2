import telebot
import os
import sys
import argparse
parser = argparse.ArgumentParser(description='Notification-Manager')
parser.add_argument('token', type=str, help='Bot Token')
parser.add_argument('chat_Id', type=str, help='Member chat_id')
parser.add_argument('text', type=str, help='Message text')
args = parser.parse_args()
token = args.token
chat_id = args.chat_Id
text = args.text
bot = telebot.TeleBot(token)


def send_message(chat_id, text):
	bot.send_message(chat_id, text)

send_message(chat_id, text)