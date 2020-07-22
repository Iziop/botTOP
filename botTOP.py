import telebot
import random
 
from telebot import types
from string import Template 
bot = telebot.TeleBot("1107014943:AAH_4PpKGwsBlfGUXIcYIKJsA-F2g0BAonI")


user_dict = {}

class User:
    def __init__(self, city):
        self.city = city

        keys = ['fullname', 'phone', 'driverSeria', 
                'driverNumber', 'driverDate', 
                ]
        
        for key in keys:
            self.key = None

def process_city_step(message):
                try:
                    chat_id = message.chat.id
                    user_dict[chat_id] = User(message.text)

                    # удалить старую клавиатуру
                    markup = types.ReplyKeyboardRemove(selective=False)

                    msg = bot.send_message(chat_id, 'Фамилия Имя Отчество', reply_markup=markup)
                    bot.register_next_step_handler(msg, process_fullname_step)

                except Exception as e:
                    bot.reply_to(message, 'ooops!!')

def process_fullname_step(message):
                try:
                    chat_id = message.chat.id
                    user = user_dict[chat_id]
                    user.fullname = message.text

                    msg = bot.send_message(chat_id, 'Ваш номер телефона')
                    bot.register_next_step_handler(msg, process_phone_step)

                except Exception as e:
                    bot.reply_to(message, 'ooops!!')

def process_phone_step(message):
                try:
                    int(message.text)

                    chat_id = message.chat.id
                    user = user_dict[chat_id]
                    user.phone = message.text

                    msg = bot.send_message(chat_id, 'Почта')
                    bot.register_next_step_handler(msg, process_driverSeria_step)

                except Exception as e:
                    msg = bot.reply_to(message, 'Вы ввели что то другое. Пожалуйста введите номер телефона')
                    bot.register_next_step_handler(msg, process_phone_step)

def process_driverSeria_step(message):
                try:
                    chat_id = message.chat.id
                    user = user_dict[chat_id]
                    user.driverSeria = message.text

                    msg = bot.send_message(chat_id, 'Услуга которая Вам нужна')
                    bot.register_next_step_handler(msg, process_carDate_step)

                except Exception as e:
                    bot.reply_to(message, 'ooops!!')
def process_carDate_step(message):
                try:
                    chat_id = message.chat.id
                    user = user_dict[chat_id]
                    user.carDate = message.text
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

                    item1 = types.KeyboardButton("🧹 Услуги")
                    item2 = types.KeyboardButton("📈 Акции")
                    item3 = types.KeyboardButton("📞 Контакты")
                    item4 = types.KeyboardButton("📝 Анкета")

                    markup.add(item1, item2, item3, item4)
                    # ваша заявка "Имя пользователя"
                    bot.send_message(chat_id, getRegData(user, 'Ваша заявка', message.from_user.first_name), parse_mode="Markdown", reply_markup=markup)
                    # отправить в группу
                    bot.send_message(-1193429892, getRegData(user, 'Заявка от бота', bot.get_me().username), parse_mode="Markdown")

                except Exception as e:
                    bot.reply_to(message, 'ooops!!1')       
            # формирует вид заявки регистрации
            # нельзя делать перенос строки Template
            # в send_message должно стоять parse_mode="Markdown"
def getRegData(user, title, name):
                t = Template('$title *$name* \n Город: *$userCity* \n ФИО: *$fullname* \n Телефон: *$phone* \n Почта *$driverSeria* \n Услуга: *$carDate*')

                return t.substitute({
                  'title': title,
                  'name': name,
                  'userCity': user.city,
                  'fullname': user.fullname,
                  'phone': user.phone,
                  'driverSeria': user.driverSeria,
                  'carDate': user.carDate,
                 })
 
@bot.message_handler(commands=['start'])
def welcome(message):
    
        
    # keyboard









        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        item1 = types.KeyboardButton("🧹 Услуги")
        item2 = types.KeyboardButton("📈 Акции")
        item3 = types.KeyboardButton("📞 Контакты")
        item4 = types.KeyboardButton("📝 Анкета")
 
        markup.add(item1, item2, item3, item4)
 
        bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - {1.first_name} Bot, бот созданный, чтобы очистить Ваше понимаение о\nTop Cleaning Service.".format(message.from_user, bot.get_me()),
         reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🧹 Услуги':
        
            keyboard = types.InlineKeyboardMarkup()
            # По очереди готовим текст и обработчик для каждого знака зодиака
            key_oven = types.InlineKeyboardButton(text='Уборка после стротельства/ремонта', callback_data='usluga1')
            # И добавляем кнопку на экран
            keyboard.add(key_oven)
            key_telec = types.InlineKeyboardButton(text='Уборка прилегающей территории акватории', callback_data='usluga2')
            keyboard.add(key_telec)
            key_bliznecy = types.InlineKeyboardButton(text='Обслуживание мест ландшафтного озеленения', callback_data='usluga3')
            keyboard.add(key_bliznecy)
            key_rak = types.InlineKeyboardButton(text='Уборка подземных паркингов', callback_data='usluga4')
            keyboard.add(key_rak)
            key_lev = types.InlineKeyboardButton(text='Чистка остеленения и фасадов', callback_data='usluga5')
            keyboard.add(key_lev)
            key_deva = types.InlineKeyboardButton(text='Генеральная уборка', callback_data='usluga6')
            keyboard.add(key_deva)
            key_vesy = types.InlineKeyboardButton(text='Уборка офисных помещений ', callback_data='usluga7')
            keyboard.add(key_vesy)
            key_scorpion = types.InlineKeyboardButton(text='Уборка образовательных учреждений', callback_data='usluga8')
            keyboard.add(key_scorpion)
            key_strelec = types.InlineKeyboardButton(text='Уборка жилых комплексов', callback_data='usluga9')
            keyboard.add(key_strelec)
            key_strelec = types.InlineKeyboardButton(text='Дезинфекция', callback_data='usluga10')
            keyboard.add(key_strelec)

            bot.send_message(message.from_user.id, text='А вот и список услуг:',reply_markup=keyboard)
        elif message.text == '📈 Акции':
 
            #markup = types.InlineKeyboardMarkup(row_width=2)
            #item1 = types.InlineKeyboardButton("⬅️ Назад", callback_data='back')
            
 
            #markup.add(item1)
 
            bot.send_message(message.chat.id, "🔘 Каждая 5-ая чистка эскалаторов и траволаторов в подарок\n🔘 Постоянным клиентам скидка до 30%\n🔘 Ген Уборка и чистка мебели -20%\n🔘 Подарочный сертификат на любые услуги клининга", reply_markup=None)
        elif message.text == '📞 Контакты':
            bot.send_message(message.chat.id, "📲 +7 (727) 311 86 17\n📲 +7 (727) 269 54 00\n📲 +7 (771) 300 88 30\n📩 sales@topcs.kz\n🌎 topcs.kz", reply_markup=None)
        elif message.text == '📝 Анкета':

            
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Алматы')
            itembtn2 = types.KeyboardButton('Нур-Султан')
            markup.add(itembtn1, itembtn2)

            msg = bot.send_message(message.chat.id, 'Ваш город?', reply_markup=markup)
            bot.register_next_step_handler(msg, process_city_step)

            


            
        else:
            bot.send_message(message.chat.id, 'По всем вопросам звоните +77713008828 Балжан')
 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'usluga1':
                bot.send_message(call.message.chat.id, 'Спектр оказываемых нашей компанией услуг по уборке после строительства/ремонта:\n🔸 комплексное обслуживание оконных и металлопластиковых конструкций с обеих сторон\n🔸 полировка зеркал и стеклянных поверхностей\n🔸 глубокая чистка с удалением следов краски, затирки и других загрязнений с твердых поверхностей пола, стен, плинтусов\n🔸 при необходимости – глубокая чистка полов с твердым покрытием при помощи роторной/поломоечной машины\n🔸 комплексное обслуживание стен, дверей, дверных блоков\n🔸 комплексное обслуживание осветительных приборов\n🔸 комплексное обслуживание санузлов с дезинфекцией и устранением налетов и загрязнений на плитке, сантехнике, аксессуарах\n🔸 удаление загрязнений с горизонтальных и вертикальных поверхностей мебели и предметов интерьера\n🔸 вакуумная чистка ковровых покрытий\n🔸 при необходимости – химическая чистка ковровых покрытий и мягкой мебели\n🔸 комплексная чистка эскалаторов, лифтов')
            elif call.data == 'usluga2':
                bot.send_message(call.message.chat.id, 'Спектр оказываемых нашей компанией услуг по уборке прилегающей территории зависит от сезонности.\n🟦 Уборка в летний период:\n🔸 ручная/механизированная очистка территории, сбор мусора, листвы\n🔸 мытье внешней стороны дверей, мытье ступеней\n🔸 чистка внешних грязезадерживающих решеток\n🔸 влажная уборка детских и спортивных площадок, скамеек\n🔸 очистка  уличных пепельниц и урн на территории\n🔸 мойка фонарных столбов, ограждений, знаков высотой до 3 метров ежемесячно\n🔸 уборка зоны фонтана\n🔸 поддержание чистоты пожарных щитов, шлагбаумов, картридеров\n🔸 вынос мусора, складирование мусора в мусорные контейнеры\n🔸 поддержание чистоты зоны мусорных контейнеров\n🔸 уход за газоном и насаждениями: полив, удобрение, прополка, острижка газона, обрезка деревьев, проведение мер по борьбе с вредителями\n🔸 декоративное оформление сада цветами и пересадка зеленых растений\n🔸 постоянный мониторинг за чистотой территории в течение дня\n🟦 Уборка в зимний период:\n🔸 ручная/ механизированная очистка территории от снега и наледи и временное складирование  в обозначенные места до вывоза\n🔸 чистка внешних грязезадерживающих решеток\n🔸 обработка тротуаров реагентами против обледенения\n🔸 очистка уличных пепельниц и урн\n🔸 поддержание чистоты пожарных щитов, шлагбаумов, картридеров\n🔸 сбор и вынос мусора в мусорные контейнеры, складирование мусора в отведенных для этого местах\n🔸 вывоз снега при необходимости механизированным способом с привлечением снегоуборочной техники\n🔸 превентивные меры по уходу за садом')
            elif call.data == 'usluga3':
                bot.send_message(call.message.chat.id, 'Уход за газоном и насаждениями в летний период(с 1 апр по 31 окт):\n🔸 полив и покос газонов, насаждений\n🔸 прополка, уничтожение сорняков\n🔸 обрезка кустарников и деревьев\n🔸 реанимация насаждений\n🔸 удобрение, проведение мер по борьбе с вредителями')    
            elif call.data == 'usluga4':
                bot.send_message(call.message.chat.id, 'Ежедневные работы:\n🔸 влажная (механизированная) уборка поверхности пола с применением специальной химии\n🔸 очистка въездных/выездных пандусов от мусора, слякоти, (снега и льда в зимний период)\n🔸 влажная уборка оградительных упоров парковочных мест\n🔸 очистка от мусора и грязи сливных лотков\n🔸 поддержание в чистом виде пожарных лестниц и тамбуров\n🔸 поддержание в чистом состоянии поворотных зеркал и дорожных знаков на пандусах\n🔸 поддержание в чистом состоянии информационных табличек, дорожных знаков, шлагбаумов\n🔸 подметание, удаление мусора, песка, листвы с поверхности пола, сбор мусора из урн, вынос мусора в места складирования ТБО\n🔸 удаление пыли с пожарных щитов и коробов')
            elif call.data == 'usluga5':
                bot.send_message(call.message.chat.id, 'ТОО «Top Cleaning Service» предлагает профессиональную мойку фасадов и остекления зданий. Пыль, грязь, надписи, налет выхлопных газов автомобилей – все это портит внешний вид здания, вредит имиджу организации и вызывает неприязнь у большинства людей.')
            elif call.data == 'usluga6':
                bot.send_message(call.message.chat.id, 'Перечесь входящих работ:\n🔸 комплексное обслуживание оконных и металлопластиковых конструкций с обеих сторон, подоконников, стеклянных и зеркальных поверхностей и перегородок\n🔸 вакуумная чистка и мытье напольных покрытий любого типа\n🔸 вакуумная чистка ковровых покрытий и мягкой мебели, при необходимости – химическая чистка\n🔸 глубокая чистка с удалением локальных загрязнений с поверхностей пола, стен, плинтусов, дверей, проемов\n🔸 комплексная чистка осветительных приборов, кондиционеров, отопительных приборов\n🔸 удаление пыли с горизонтальных и вертикальных поверхностей мебели,  предметов интерьера\n🔸 комплексная уборка кухонной мебели и бытовой техники с чисткой кафельных покрытий\n🔸 комплексное обслуживание санузлов с дезинфекцией и устранением налетов и загрязнений на плитке, сантехнике, аксессуарах\n🔸 уборка на балконах, в кладовках\n🔸 чистка и мойка мусорных корзин, вынос мусора')
            elif call.data == 'usluga7':
                bot.send_message(call.message.chat.id, 'Ежедневная уборка офисов включает следующее:\n🔸 удаление пыли с поверхностей офисной мебели, оргтехники, элементов интерьера\n🔸 удаление загрязнений и пятен с дверей, ручек, замков\n🔸 чистка стеклянных поверхностей мебели, перегородок, зеркал\n🔸 вакуумная чистка ковровых покрытий, мягкой мебели\n🔸 влажная уборка пола\n🔸 чистка мусорных корзин\n🔸 влажная уборка и дезинфекция санузлов\n🔸 оснащение санузлов санитарно-гигиеническими средствами и материалами')
            elif call.data == 'usluga8':
                bot.send_message(call.message.chat.id, 'В уборку помещений(классов,холлов,аудиторий) входит:\n🔸 комплексное обслуживание входной группы\n🔸 удаление пыли с поверхностей парт, столов, шкафов и тд\n🔸 удаление загрязнений и пятен с дверей, ручек, замков\n🔸 чистка стеклянных поверхностей мебели, перегородок, зеркал\n🔸 вакуумная чистка ковровых покрытий, мягкой мебели\n🔸 влажная уборка пола\n🔸 чистка мусорных корзин\n🔸 влажная уборка и дезинфекция санузлов\n🔸 оснащение санузлов санитарно-гигиеническими средствами и материалами\n🔸 благоустройство и комплексная уборка прилегающей территории')    
            elif call.data == 'usluga9':
                bot.send_message(call.message.chat.id, 'В уборку ЖК входит:\n🔸 комплексное обслуживание входной группы\n🔸 комплексное обслуживание оконных и металлопластиковых конструкций, подоконников\n🔸 комплексное обслуживание плафонов осветительных приборов, радиаторов отопительной системы, почтовых ящиков\n🔸 промышленный альпинизм\n🔸 комплексная и поддерживающая уборки в помещениях, холлах, коридорах, лифтах, на лестничных клетках\n🔸 очистка технических помещений от неспецифических загрязнений\n🔸 сбор мусора и чистка мусорных корзин\n🔸 обслуживание грязезащитных ковров\n🔸 благоустройство и комплексная уборка прилегающей территории')        
            elif call.data == 'usluga10':
                bot.send_message(call.message.chat.id, 'Дезинфекция помещений')
            # remove inline buttons
            #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
            #    reply_markup=None)
 
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="Информация")
 
    except Exception as e:
        print(repr(e))
 
# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=1)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()
# RUN
bot.polling(none_stop=True)

if __name__ == '__main__':
    bot.polling(none_stop=True)
