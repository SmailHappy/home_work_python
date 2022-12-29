# Прикрутить бота к задачам с предыдущего семинара:
# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler

with open('token__bot.txt', 'r') as file_bot :
    TOKEN = file_bot.read()

updater = Updater(token = TOKEN)
dispatcher = updater.dispatcher

workspace, operator, operator_complex, complex_one, complex_two, number_one, number_two = range(7)

def log(update: Update, context: CallbackContext) :
    file = open('logger.txt', 'a')
    file.write(f'{update.effective_message.date} -/- {update.effective_user.first_name} -/- {update.effective_user.id} -/- {update.message.text}\n')
    file.close()

def start(update: Update, context: CallbackContext) :
    log(update, context)
    reply_keyboard = [['Calculator', 'Calculator complex', 'End']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard = True)
    update.message.reply_text(f"Hello {update.effective_user.first_name}\nLet's go?", reply_markup = markup_key)
    return workspace
    
def workplace(update: Update, context: CallbackContext) :
    log(update, context)
    workplace = update.message.text
    if workplace == 'Calculator' :
        update.message.reply_text('What is your 1 number?')
        return number_one
    if workplace == 'Calculator complex' :
        update.message.reply_text('What is your 1 complex number? Write Re & Im for space')
        return complex_one
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
    if user_choice_operator == '-\n\ndifference': 
        result = number_one - number_two
        update.message.reply_text(f'Результат: {number_one} - {number_two} = {result}')
    if user_choice_operator == '*\n\nmultiplication': 
        result = number_one * number_two
        update.message.reply_text(f'Результат: {number_one} * {number_two} = {result}')
    if user_choice_operator == '/\n\ndivision':
        try: 
            result = number_one / number_two
            update.message.reply_text(f'Результат: {number_one} / {number_two} = {result}')
        except: update.message.reply_text('Деление на ноль запрещено')
    return start(update, context)

def first_number_complex(update: Update, context: CallbackContext) :
    log(update, context)
    complex_number = update.message.text
    if ' ' in complex_number :
        if complex_number.count(' ') == 1 :
            complex_number = complex_number.split()
            if complex_number[0].isdigit() and complex_number[1].isdigit() :
                num_1 = int(complex_number[0])
                num_2 = int(complex_number[1])
                context.user_data['complex_one'] = num_1, num_2
                update.message.reply_text('What is your 2 complex number? Write Re & Im for space')
                return complex_two
            else : update.message.reply_text("Space nice, but need is number")
        else : update.message.reply_text("Wooow, need only 2 numbers.")
    else : update.message.reply_text('Nooo! Need space between numbers!')

def second_number_complex(update: Update, context: CallbackContext) :
    log(update, context)
    complex_number = update.message.text
    if ' ' in complex_number :
        if complex_number.count(' ') == 1 :
            complex_number = complex_number.split()
            if complex_number[0].isdigit() and complex_number[1].isdigit() :
                num_1 = int(complex_number[0])
                num_2 = int(complex_number[1])
                context.user_data['complex_two'] = num_1, num_2
                reply_keyboard = [['+\n\nsummation', '-\n\ndifference', '*\n\nmultiplication', '/\n\ndivision']]
                markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard = True)
                update.message.reply_text('What do you want?', reply_markup = markup_key)
                return operator_complex
            else : update.message.reply_text("Space nice, but need is number")
        else : update.message.reply_text("Wooow, need only 2 numbers.")
    else : update.message.reply_text('Nooo! Need space!')

def operation_complex(update: Update, context: CallbackContext) :
    log(update, context)
    number_one = context.user_data.get('complex_one')
    number_two = context.user_data.get('complex_two')
    user_choice_operator = update.message.text
    if user_choice_operator == '+\n\nsummation' : 
        res_one = number_one[0] + number_two[0]
        res_two = number_one[1] + number_two[1]
        result = str(res_one) + ' + ' + str(res_two) + 'i'
        update.message.reply_text(f'Результат сложения - {result}')
    if user_choice_operator == '-\n\ndifference': 
        res_one = number_one[0] - number_two[0]
        res_two = number_one[1] - number_two[1]
        result = str(res_one) + ' + ' + str(res_two) + 'i'
        update.message.reply_text(f'Результат вычитания - {result}')
    if user_choice_operator == '*\n\nmultiplication': 
        res_one = number_one[0] * number_two[0]
        res_two = number_one[1] * number_two[1]
        result = str(res_one) + ' * ' + str(res_two) + 'i'
        update.message.reply_text(f'Результат умножения - {result}')
    if user_choice_operator == '/\n\ndivision':
        try: 
            res_one = number_one[0] / number_two[0]
            res_two = number_one[1] / number_two[1]
            result = str(res_one) + ' / ' + str(res_two) + 'i'
            update.message.reply_text(f'Результат деления - {result}')
        except: update.message.reply_text('Деление на ноль запрещено')
    return start(update, context)

def end(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Okay. I wait you next time, {update.effective_user.first_name}\nIf you want again, write me "/start"')
    return ConversationHandler.END

conversation_handler = ConversationHandler(entry_points = [CommandHandler('start', start)], 
    states = {workspace: [MessageHandler(Filters.text, workplace)],
              complex_one: [MessageHandler(Filters.text, first_number_complex)],
              complex_two: [MessageHandler(Filters.text, second_number_complex)],
              operator_complex: [MessageHandler(Filters.text, operation_complex)],
              number_one: [MessageHandler(Filters.text, first_number)],
              number_two: [MessageHandler(Filters.text, second_number)],
              operator: [MessageHandler(Filters.text, operation)]},
    fallbacks=[CommandHandler('End', end)])

dispatcher.add_handler(conversation_handler)
updater.start_polling()
updater.idle()