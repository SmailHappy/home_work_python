# Создать телеграмм бота ( самый простой можно(калькулятор или повторитель), главное логгирование испльзуйте)

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler

with open('token_bot.txt', 'r') as file_bot :
    TOKEN = file_bot.read()

updater = Updater(token = TOKEN)
dispatcher = updater.dispatcher

workspace, operator, number_one, number_two = range(4)

def log(update: Update, context: CallbackContext) :
    file = open('logger.txt', 'a')
    file.write(f'{update.effective_message.date} -/- {update.effective_user.first_name} -/- {update.effective_user.id} -/- {update.message.text}\n')
    file.close()

def start(update: Update, context: CallbackContext) :
    log(update, context)
    reply_keyboard = [['Calculator', 'End']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard = True)
    update.message.reply_text(f"Hello {update.effective_user.first_name}\nLet's go?", reply_markup = markup_key)
    return workspace
    
def workplace(update: Update, context: CallbackContext) :
    log(update, context)
    workplace = update.message.text
    if workplace == 'Calculator' :
        update.message.reply_text('What is your 1 number?')
        return number_one
    if workplace == 'End' :
        return end(update, context)

def first_number(update: Update, context: CallbackContext) :
    log(update, context)
    number = update.message.text
    if number.isdigit():
        number = float(number)
        context.user_data['number_one'] = number
        update.message.reply_text('What is your 2 number?')
        return number_two
    else:
        update.message.reply_text('Nooo! Need is number')

def second_number(update: Update, context: CallbackContext) :
    log(update, context)
    number = update.message.text
    if number.isdigit():
        number = float(number)
        context.user_data['number_two'] = number
        reply_keyboard = [['+\n\nsummation', '-\n\ndifference', '*\n\nmultiplication', '/\n\ndivision']]
        markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard = True)
        update.message.reply_text('What do you want?', reply_markup = markup_key)
        return operator

def operation(update: Update, context: CallbackContext) :
    log(update, context)
    number_one = context.user_data.get('number_one')
    number_two = context.user_data.get('number_two')
    user_choice_operator = update.message.text
    if user_choice_operator == '+\n\nsummation' : 
        result = number_one + number_two
        update.message.reply_text(f'Результат: {number_one} + {number_two} = {result}')
    if user_choice_operator == '-\n\ndifference' : 
        result = number_one - number_two
        update.message.reply_text(f'Результат: {number_one} - {number_two} = {result}')
    if user_choice_operator == '*\n\nmultiplication' : 
        result = number_one * number_two
        update.message.reply_text(f'Результат: {number_one} * {number_two} = {result}')
    if user_choice_operator == '/\n\ndivision' :
        try: 
            result = number_one / number_two
            update.message.reply_text(f'Результат: {number_one} / {number_two} = {result}')
        except: update.message.reply_text('Деление на ноль запрещено')
    return start(update, context)

def end(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Okay. I wait you next time, {update.effective_user.first_name}\nIf you want again, write me "/start"')
    return ConversationHandler.END

conversation_handler = ConversationHandler(entry_points = [CommandHandler('start', start)], 
    states = {workspace: [MessageHandler(Filters.text, workplace)],
              number_one: [MessageHandler(Filters.text, first_number)],
              number_two: [MessageHandler(Filters.text, second_number)],
              operator: [MessageHandler(Filters.text, operation)]},
    fallbacks=[CommandHandler('End', end)])

dispatcher.add_handler(conversation_handler)
updater.start_polling()
updater.idle()