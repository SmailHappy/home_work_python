# Создайте программу (можно взять любой прошлый проект) при помощи виртуального окружения и PIP(в семинаре все обсудили по этому поводу.

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка.

from random import randint
from isOdd import isOdd
fill_numbers = [randint(0, 100) for i in range(4)]
print (f"Список - {fill_numbers}") 
print (f"Сумма  четных цифр = {sum(i for i in fill_numbers if not isOdd(i))}") 
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
print (f"Сумма цифр на нечётных позициях = {sum(fill_numbers[i] for i in range(len(fill_numbers)) if isOdd(i))}") 

# Создать телеграмм бота ( самый простой можно(калькулятор или повторитель), главное логгирование испльзуйте)

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

with open('token_bot.txt', 'r') as file_bot :
    TOKEN = file_bot.read()

updater = Updater(token = TOKEN, use_context = True)
dispatcher = updater.dispatcher

# logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
# logger = logging.getLogger('main.py')

def log(update: Update, context: CallbackContext) :
    file = open('logger.txt', 'a')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')
    file.close()

def start(update: Update, context: CallbackContext) :
    reply_keyboard = [['sum', 'diff', 'multy', 'dev']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard = True)
    log(update, context)
    update.message.reply_text(f"Hello {update.effective_user.first_name}\nI'm a bot - calculator!\nWhat you want?", reply_markup = markup_key)

def sum(update: Update, context: CallbackContext) :
    update.message.reply_text('Write your numbers for space')
    numbers = update.message.text
    numb = numbers.split()
    number_one = int(numb[1])
    number_two = int(numb[2])
    log(update, context)
    update.message.reply_text(f'Результат сложения: {number_one} + {number_two} = {number_one + number_two}')

def diff(update: Update, context: CallbackContext) :
    update.message.reply_text('Write your numbers for space')
    numbers = update.message.text
    numb = numbers.split()
    number_one = int(numb[1])
    number_two = int(numb[2])
    log(update, context)
    update.message.reply_text(f'Результат вычитания: {number_one} + {number_two} = {number_one - number_two}')
   
def multy(update: Update, context: CallbackContext) :
    update.message.reply_text('Write your numbers for space')
    numbers = update.message.text
    numb = numbers.split()
    number_one = int(numb[1])
    number_two = int(numb[2])
    log(update, context)
    update.message.reply_text(f'Результат умножения: {number_one} + {number_two} = {number_one * number_two}')

def dev(update: Update, context: CallbackContext) :
    update.message.reply_text('Write your numbers for space')
    numbers = update.message.text
    numb = numbers.split()
    number_one = int(numb[1])
    number_two = int(numb[2])
    log(update, context)
    update.message.reply_text(f'Результат деления: {number_one} + {number_two} = {number_one / number_two}')
    
    # update.message.reply_text(f"If you want more?")



updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('sum', sum))
updater.dispatcher.add_handler(CommandHandler('diff', diff))
updater.dispatcher.add_handler(CommandHandler('multy', multy))
updater.dispatcher.add_handler(CommandHandler('dev', dev))

updater.start_polling()
updater.idle()