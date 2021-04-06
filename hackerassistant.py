#!/usr/bin/python3.7
#-*-encoding: utf8 -*-

import subprocess
import telegram
from telegram.ext import *
from time import time, strftime, localtime
import string, random
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
__API_TOKEN__ = "1457372735:AAHG3xrwc18NvGPpLZUJJeW-SR5bt9J9GYg"
__LOG_PATH__ = "/home/h4niz/Downloads/"
__WORKSPACE_DIR__ = "/home/h4niz/Bond"
def test(cmd):
	result = subprocess.run(cmd, stdout=subprocess.PIPE)
	return result.stdout.decode()

def log_error(func, msg):
	logfile = "{}/{}.log".format(__LOG_PATH__, "errors")
	linelog = "\n{}:\t\t[{}] - {}".format(strftime("%Y-%m-%d %H:%M:%S", localtime()), func, msg)
	open(logfile, "a+").write(linelog)
def log_info(func, msg):
	logfile = "{}/{}.log".format(__LOG_PATH__, "info")
	linelog = "\n{}:\t\t[{}] - {}".format(strftime("%Y-%m-%d %H:%M:%S", localtime()), func, msg)
	open(logfile, "a+").write(linelog)

def random_str():
	return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# Send file, max 50MB for other files.
def sendfile(update,context):
	try:
		file_fd = open(context.args[0], "rb")
		context.bot.send_message(chat_id=update.effective_chat.id, text="File to download: {}".format(context.args[0]))
		context.bot.send_document(chat_id=update.effective_chat.id, document=file_fd)
	except Exception as ex:
		context.bot.send_message(chat_id=update.effective_chat.id, text=ex)

# Send file, max 50MB for other files.
def send_file_report(update,context,filepath):
	try:
		file_fd = open(filepath, "rb")
		context.bot.send_message(chat_id=update.effective_chat.id, text="File to download: {}".format(context.args[0]))
		context.bot.send_document(chat_id=update.effective_chat.id, document=file_fd)
	except Exception as ex:
		context.bot.send_message(chat_id=update.effective_chat.id, text=ex)

# Bot function reply
def start(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id, text="Hello h4niz, do you dig more vulnerabilities?")

def unknown(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id, text="Sogi, tui khong hieu lenh ban vua nhap!")

def echo(update, context):
	try:
		context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
	except Exception as ex:
		context.bot.send_message(chat_id=update.effective_chat.id, text=ex)

def haniz(update, context):
	try:
		content = "# small snipet to handle penetration tasks\n# h4niz\n\n# Option:\n/checkwaf [url]: to check waf\n/recon [target]: to recon target via sniper\n/subfinder [target]\n/nmap [target] [script]: to scan nmap\n/add_targets [targets line by line]: return file path to store targets line by line on server\n/sniper [option]: option as sniper commandline"
		context.bot.send_message(chat_id=update.effective_chat.id, text=content)
	except Exception as ex:
		context.bot.send_message(chat_id=update.effective_chat.id, text=ex)

def custom_command(update, context):
	try:
		context.bot.send_message(chat_id=update.effective_chat.id, text="Running {}".format(' '.join(context.args)))
		result = subprocess.run(context.args, stdout=subprocess.PIPE)
		context.bot.send_message(chat_id=update.effective_chat.id, text=result.stdout.decode())
		context.bot.send_message(chat_id=update.effective_chat.id, text="\nDone!\n =====* HAPPY HACKING! *====\n\n")
	except Exception as ex:
		print(ex)
		# context.bot.send_message(chat_id=update.effective_chat.id, text=ex)

# Sn1per recon
def recon(update, context):
	try:
		cmd = ['sniper', '-t', context.args[0], '-o', '-re']
		context.bot.send_message(chat_id=update.effective_chat.id, text="Running {}".format(' '.join(cmd)))
		result = subprocess.run(cmd, stdout=subprocess.PIPE)
		print(result.stdout)
		target = context.args[0]
		target = target.replace("/", "_")
		target = target.replace("\\", "_")
		target = target.replace(".", "_")
		filename = "{}/recon/recon_{}_{}.html".format(__WORKSPACE_DIR__, target, random_str())
		open(filename, "a+", encoding="utf-8").write(result.stdout.decode("utf-8"))
		context.bot.send_message(chat_id=update.effective_chat.id, text="Sending report....")
		send_file_report(update,context, filename)
		context.bot.send_message(chat_id=update.effective_chat.id, text="\nDone!\n =====* HAPPY HACKING! *====\n\n")
	except Exception as ex:
		context.bot.send_message(chat_id=update.effective_chat.id, text=ex)

# Sn1per normal
def sniper(update, context):
	try:
		cmd = ['sniper', '-t'] + context.args
		context.bot.send_message(chat_id=update.effective_chat.id, text="Running {}".format(' '.join(cmd)))
		result = subprocess.run(cmd, stdout=subprocess.PIPE)
		print(result.stdout)

		target = context.args[0]
		target = target.replace("/", "_")
		target = target.replace("\\", "_")
		target = target.replace(".", "_")
		filename = "{}/sniper/sniper{}_{}.html".format(__WORKSPACE_DIR__, target, random_str())
		open(filename, "a+", encoding="utf-8").write(result.stdout.decode("utf-8"))
		context.bot.send_message(chat_id=update.effective_chat.id, text="Sending report....")
		send_file_report(update,context, filename)
		context.bot.send_message(chat_id=update.effective_chat.id, text="\nDone!\n =====* HAPPY HACKING! *====\n\n")
	except Exception as ex:
		context.bot.send_message(chat_id=update.effective_chat.id, text=ex)

# Sn1per normal
def wsniper(update, context):
	try:
		cmd = ['sniper', '-m', 'webscan', '-t'] + context.args
		context.bot.send_message(chat_id=update.effective_chat.id, text="Running {}".format(' '.join(cmd)))
		result = subprocess.run(cmd, stdout=subprocess.PIPE)
		print(result.stdout)
		target = context.args[0]
		target = target.replace("/", "_")
		target = target.replace("\\", "_")
		target = target.replace(".", "_")
		filename = "{}/sniper/sniper{}_{}.html".format(__WORKSPACE_DIR__, target, random_str())
		open(filename, "a+", encoding="utf-8").write(result.stdout.decode("utf-8"))
		context.bot.send_message(chat_id=update.effective_chat.id, text="Sending report....")
		send_file_report(update,context, filename)
		context.bot.send_message(chat_id=update.effective_chat.id, text="\nDone!\n =====* HAPPY HACKING! *====\n\n")
	except Exception as ex:
		context.bot.send_message(chat_id=update.effective_chat.id, text=ex)

def subfinder(update, context):
	target = context.args[0]
	target = target.replace("/", "_")
	target = target.replace("\\", "_")
	target = target.replace(".", "_")
	try:
		filename = '{}/subfinder/subfinder_{}_{}.txt'.format(__WORKSPACE_DIR__, target, random_str())
		cmd = ['subfinder', '-d', context.args[0], '-o', filename]
		context.bot.send_message(chat_id=update.effective_chat.id, text="Running {}".format(' '.join(cmd)))
		result = subprocess.run(cmd, stdout=subprocess.PIPE)
		data = result.stdout.split(b"\n")
		data = set(data)
		print(b'\n'.join(data))
		context.bot.send_message(chat_id=update.effective_chat.id, text="Sending report...")
		send_file_report(update, context, filename)
		context.bot.send_message(chat_id=update.effective_chat.id, text="\nDone!\n =====* HAPPY HACKING! *====\n\n")
	except Exception as ex:
		context.bot.send_message(chat_id=update.effective_chat.id, text=ex)

def nmap(update, context):
	try:
		target = context.args[0]
		target = target.replace("/", "_")
		target = target.replace("\\", "_")
		target = target.replace(".", "_")
		filename = "{}/nmap/nmap_{}_{}.xml".format(__WORKSPACE_DIR__, context.args[0], random_str())
		cmd = ['nmap', '-T4', '-A', '-v ', ' '.join(context.args), '-oX={}'.format(filename)]
		# if(len(context.args) == 2):
		# 	cmd = ['nmap', '-T4', '-A', '-v', context.args[0], '--script={}'.format(context.args[1]), '-oX={}'.format(filename)]
		# else:
		# 	filename = "{}/nmap_{}_{}.xml".format(__WORKSPACE_DIR__, context.args[0], random_str())
		# 	cmd = ['nmap', '-T4', '-A', '-v', '-Pn', context.args[0], context.args[1], '-oX={}'.format(filename)]

		context.bot.send_message(chat_id=update.effective_chat.id, text="Running {}".format(' '.join(cmd)))
		result = subprocess.run(cmd, stdout=subprocess.PIPE)
		print(result.stdout)
		filenametxt = "{}/nmap/nmap_{}_{}.txt".format(__WORKSPACE_DIR__, target, random_str())
		open(filenametxt, "a+").write(result.stdout.decode())
		context.bot.send_message(chat_id=update.effective_chat.id, text="Sending report...")
		send_file_report(update, context, filenametxt)
		send_file_report(update, context, filename)
		context.bot.send_message(chat_id=update.effective_chat.id, text="\nDone!\n =====* HAPPY HACKING! *====\n\n")
	except Exception as ex:
		context.bot.send_message(chat_id=update.effective_chat.id, text=ex)

def checkwaf(update, context):
	try:
		domain = "http://{}".format(context.args[0].replace("https://", ""))
		cmd = ['wafw00f', '{}'.format(domain)]
		context.bot.send_message(chat_id=update.effective_chat.id, text="Running {}".format(' '.join(cmd)))
		result = subprocess.run(cmd, stdout=subprocess.PIPE)
		context.bot.send_message(chat_id=update.effective_chat.id, text=result.stdout.decode())
		context.bot.send_message(chat_id=update.effective_chat.id, text="\nDone!\n =====* HAPPY HACKING! *====\n\n")
	except Exception as ex:
		context.bot.send_message(chat_id=update.effective_chat.id, text=ex)

def add_targets(update, context):
	try:
		data = update.message.text.split("\n")
		data.pop(0)
		print(data)
		targetpath = "{}/targets/bond_{}.target".format(__WORKSPACE_DIR__, random_str())
		open(targetpath, "a+").write('\n'.join(data))
		context.bot.send_message(chat_id=update.effective_chat.id, text=targetpath)
	except Exception as ex:
		context.bot.send_message(chat_id=update.effective_chat.id, text=ex)

def bot_handler():
	try:
		updater = Updater(token=__API_TOKEN__, use_context=True)
		dispatcher = updater.dispatcher

		# Init bot with API token
		bot = telegram.Bot(token=__API_TOKEN__)
		bot_info = bot.get_me()
		log_info("bot_handler", "botname: {} (id={}) aka {} was deployed successful!".format(bot_info["username"], bot_info["id"], bot_info["first_name"]))
	except Exception as ex:
		log_error("bot_handler", "Load API failed! - {}".format(ex))




	# Command handler
	start_handler = CommandHandler('start', start)
	dispatcher.add_handler(start_handler)
	updater.start_polling()

	haniz_handler = CommandHandler('haniz', haniz)
	dispatcher.add_handler(haniz_handler)
	updater.start_polling()

	# Test getfile
	sendfile_handler = CommandHandler('getfile', sendfile)
	dispatcher.add_handler(sendfile_handler)
	updater.start_polling()

	# Custom command handler
	runcmd_handler = CommandHandler('rce', custom_command)
	dispatcher.add_handler(runcmd_handler)
	updater.start_polling()
	# Add target
	add_target_handler = CommandHandler('add_targets', add_targets)
	dispatcher.add_handler(add_target_handler)
	updater.start_polling()
	# Recon
	recon_handler = CommandHandler('recon', recon)
	dispatcher.add_handler(recon_handler)
	updater.start_polling()
	# Subfinder
	subfinder_handler = CommandHandler('subfinder', subfinder)
	dispatcher.add_handler(subfinder_handler)
	updater.start_polling()
	# Nmap scan 
	# arg 0: target
	# arg 1: script name
	nmap_handler = CommandHandler('nmap', nmap)
	dispatcher.add_handler(nmap_handler)
	updater.start_polling()
	# Sniper
	sniper_handler = CommandHandler('sniper', sniper)
	dispatcher.add_handler(sniper_handler)
	updater.start_polling()
	# Sniper WEbscan
	wsniper_handler = CommandHandler('wsniper', wsniper)
	dispatcher.add_handler(wsniper_handler)
	updater.start_polling()
	# Checkwaf
	checkwaf_handler = CommandHandler('checkwaf', checkwaf)
	dispatcher.add_handler(checkwaf_handler)
	updater.start_polling()

	unknown_handler = MessageHandler(Filters.command, unknown)
	dispatcher.add_handler(unknown_handler)


if __name__ == '__main__':
	# target = "testphp.vulnweb.com"
	# cmd = ['sniper', '-t', '{}'.format(target), '-o', '-re']
	# print(test(cmd))

	bot_handler()