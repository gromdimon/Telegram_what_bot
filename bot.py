import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sticker = open('pictures/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)

    # Keybord
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton('Найти идею!🦉')
    item2 = types.KeyboardButton('О боте🤖')
    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Добро пожаловать🖐️, {0.first_name}!\nЯ - '<b>{1.first_name}</b>', создан, чтобы помогать находить новые идеи и задавать себе интересные вопросы. Приятного пользования!😇".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def thema(message):
    if message.chat.type == 'private':
        if message.text == 'Найти идею!🦉':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Живые существа🌿', callback_data='bio')
            item2 = types.InlineKeyboardButton('Физика⚛️', callback_data='phys')
            item3 = types.InlineKeyboardButton('Банковское дело🪙', callback_data='bank')
            item4 = types.InlineKeyboardButton('Бизнес💸', callback_data='busin')
            item5 = types.InlineKeyboardButton('Лечебное дело⚕️', callback_data='medic')
            markup.add(item1, item2, item3, item4, item5)

            bot.send_message(message.chat.id, 'Выбери интересный раздел', reply_markup=markup)

        elif message.text == 'О боте🤖':
            bot.send_message(message.chat.id, 'Это бот проекта WAT. '
                                              'Идея родилась на StartUp Skills и в процессе обучения материализовалась в проект WAT (what to do?). '
                                              'Суть проекта в занятии свободного времени людей, которые хотят потратить их время с пользой, '
                                              'узнавая что-нибудь новое. '
                                              'А так же отличительным качеством сервиса является уникальная подача качественной информации на 3 разных ступенях. '
                                              'Попробуйте!🤗')



        # Second layer
        elif message.text == 'Читать больше про молекулы':
            # Keybord
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item1 = types.KeyboardButton('Читать  ещё больше про молекулы')
            markup.add(item1)
            bot.send_message(message.chat.id, 'Молекула - это электрически нейтральная группа из двух или более атомов, удерживаемых вместе химическими связями. Молекулы отличаются от ионов отсутствием электрического заряда.'
                                              'В квантовой физике, органической химии и биохимии различие между ионами отбрасывается, и молекула часто используется при обращении к многоатомным ионам.'
                                              'В кинетической теории газов термин молекула часто используется для обозначения любой газообразной частицы независимо от ее состава. Это нарушает определение, согласно которому молекула содержит два или более атомов, поскольку благородные газы являются отдельными атомами.'
                                              'Молекула может быть гомоядерной, то есть она состоит из атомов одного химического элемента, как в случае с двумя атомами в молекуле кислорода (O2); или она может быть гетероядерной, химическим соединением, состоящим из более чем одного элемента, как в случае с водой (два атома водорода и один атом кислорода; H2O).'
                                              'Атомы и комплексы, связанные нековалентными взаимодействиями, такими как водородные связи или ионные связи, обычно не считаются отдельными молекулами.', reply_markup=markup)
        elif message.text == 'Читать больше про ДНК':
            # Keybord
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item1 = types.KeyboardButton('Читать  ещё больше про ДНК')
            markup.add(item1)
            bot.send_message(message.chat.id, 'Дезоксирибонуклеиновая кислота (ДНК) представляет собой молекулу, состоящую из двух полинуклеотидных цепей, которые обвиваются друг вокруг друга, образуя двойную спираль, '
                                              'несущую генетические инструкции по развитию, функционированию, росту и размножению всех известных организмов и многих вирусов. '
                                              'ДНК и рибонуклеиновая кислота (РНК) являются нуклеиновыми кислотами. '
                                              'Наряду с белками, липидами и сложными углеводами (полисахаридами), нуклеиновые кислоты являются одним из четырех основных типов макромолекул, которые необходимы для всех известных форм жизни.', reply_markup=markup)
        elif message.text == 'Читать больше про атомы':
            # Keybord
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item1 = types.KeyboardButton('Читать  ещё больше про атом')
            markup.add(item1)
            bot.send_message(message.chat.id, 'Хотя слово атом в первоначальном значении обозначало частицу, которая не делится на меньшие части, согласно научным представлениям он состоит из более мелких частиц, называемых субатомными частицами. Атом состоит из электронов, протонов, все атомы, кроме водорода-1, содержат также нейтроны.'
'Электрон является самой лёгкой из составляющих атом частиц с массой 9,11⋅10−31 кг, отрицательным зарядом и размером, слишком малым для измерения современными методами. Эксперименты по сверхточному определению магнитного момента электрона (Нобелевская премия 1989 года) показывают, что размеры электрона не превышают 10−18 м.'
'Протоны обладают положительным зарядом и в 1836 раз тяжелее электрона (1,6726⋅10−27 кг). Нейтроны не обладают электрическим зарядом и в 1839 раз тяжелее электрона (1,6749⋅10−27 кг).'
'При этом масса ядра меньше суммы масс составляющих его протонов и нейтронов из-за явления дефекта массы. Нейтроны и протоны имеют сравнимый размер, около 2,5⋅10−15 м, хотя размеры этих частиц определены плохо.'
'В стандартной модели элементарных частиц как протоны, так и нейтроны состоят из элементарных частиц, называемых кварками. Наряду с лептонами, кварки являются одной из основных составляющих материи. И первые и вторые являются фермионами. Существует шесть типов кварков, каждый из которых имеет дробный электрический заряд, равный +2⁄3 или (−1⁄3) элементарного. Протоны состоят из двух u-кварков и одного d-кварка, а нейтрон — из одного u-кварка и двух d-кварков. Это различие объясняет разницу в массах и зарядах протона и нейтрона. Кварки связаны между собой сильными ядерными взаимодействиями, которые передаются глюонами.', reply_markup=markup)
        elif message.text == 'Читать больше про скорость света':
            # Keybord
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item1 = types.KeyboardButton('Читать  ещё больше про скорость света')
            markup.add(item1)
            bot.send_message(message.chat.id, 'Скорость света в вакууме, обычно обозначаемая c, является универсальной физической постоянной, важной во многих областях физики. Его точное значение определено как 299792458 метров в секунду (приблизительно 300000 км/с, или 186000 миль/с). Это точно, потому что по международному соглашению метр определяется как длина пути, пройденного светом в вакууме за промежуток времени 1⁄299792458 секунды. Согласно специальной теории относительности, c - это верхний предел скорости, с которой обычная материя, энергия или любой сигнал, несущий информацию, могут перемещаться в пространстве. '
'Хотя эта скорость чаще всего ассоциируется со светом, это также скорость, с которой все безмассовые частицы и возмущения поля перемещаются в вакууме, включая электромагнитное излучение (из которых свет представляет собой небольшой диапазон в частотном спектре) и гравитационные волны. Такие частицы и волны движутся со скоростью с независимо от движения источника или инерциальной системы отсчета наблюдателя. Частицы с ненулевой массой покоя могут приближаться к c, но на самом деле никогда не смогут достичь ее, независимо от системы отсчета, в которой измеряется их скорость. В специальной и общей теориях относительности c связывает пространство и время, а также фигурирует в знаменитом уравнении эквивалентности массы и энергии E = mc2. В некоторых случаях объекты или волны могут казаться движущимися быстрее света (например, фазовые скорости волн, появление некоторых высокоскоростных астрономических объектов и особые квантовые эффекты). Под расширением Вселенной понимается превышение скорости света за определенной границей.'
'Скорость, с которой свет распространяется через прозрачные материалы, такие как стекло или воздух, меньше c; аналогично, скорость электромагнитных волн в проводных кабелях медленнее, чем c. Соотношение между c и скоростью v, с которой свет распространяется в материале, называется показателем преломления n материала (n = c/v). Например, для видимого света показатель преломления стекла обычно составляет около 1,5, что означает, что свет в стекле распространяется со скоростью c/1,5 ≈ 200000 км/с (124000 миль/с); показатель преломления воздуха для видимого света составляет около 1,0003, поэтому скорость света в воздухе примерно на 90 км/с (56 миль/с) медленнее, чем c.', reply_markup=markup)
        elif message.text == 'Читать больше про кредиты':
            # Keybord
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item1 = types.KeyboardButton('Читать  ещё больше про кредиты')
            markup.add(item1)
            bot.send_message(message.chat.id, 'Кредит (от латинского credit, "(он/она/оно) верит") - это доверие, которое позволяет одной стороне предоставлять деньги или ресурсы другой стороне, при этом вторая сторона не возмещает первой стороне немедленно (тем самым создавая долг), но обещает либо погасить, либо вернуть эти ресурсы (или другие материалы равной ценности) позднее. Другими словами, кредит - это способ сделать взаимность формальной, юридически закрепленной и распространяемой на большую группу не связанных между собой людей.'
'Предоставляемые ресурсы могут быть финансовыми (например, предоставление кредита), или они могут состоять из товаров или услуг (например, потребительский кредит). Кредит включает в себя любую форму отсрочки платежа. Кредит предоставляется кредитором, также известным как кредитор, должнику, также известному как заемщик.', reply_markup=markup)
        elif message.text == 'Читать больше про банки':
            # Keybord
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item1 = types.KeyboardButton('Читать  ещё больше про банки')
            markup.add(item1)
            bot.send_message(message.chat.id, 'Банк - это финансовое учреждение, которое принимает депозиты от населения и создает депозит до востребования, одновременно выдавая кредиты. Кредитная деятельность может осуществляться непосредственно банком или косвенно через рынки капитала. ' 
'Поскольку банки играют важную роль в финансовой стабильности и экономике страны, большинство юрисдикций осуществляют высокую степень регулирования деятельности банков. Большинство стран институционализировали систему, известную как банковское дело с частичным резервированием, в соответствии с которой банки владеют ликвидными активами, равными лишь части их текущих обязательств. В дополнение к другим нормативным актам, предназначенным для обеспечения ликвидности, банки, как правило, подчиняются минимальным требованиям к капиталу, основанным на международном наборе стандартов капитала, Базельских соглашениях. '
'Банковское дело в его современном понимании возникло в четырнадцатом веке в процветающих городах Италии эпохи Возрождения, но во многих отношениях функционировало как продолжение идей и концепций кредита и кредитования, которые уходили своими корнями в древний мир. В истории банковского дела ряд банковских династий – в частности, Медичи, Фуггеры, Вельзеры, Беренберги и Ротшильды – играли центральную роль на протяжении многих столетий. Старейшим существующим розничным банком является Banca Monte dei Paschi di Siena (основан в 1472 году), а старейшим существующим торговым банком является Berenberg Bank (основан в 1590 году).', reply_markup=markup)
        elif message.text == 'Читать больше про стартапы':
            # Keybord
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item1 = types.KeyboardButton('Читать  ещё больше про стартапы')
            markup.add(item1)
            bot.send_message(message.chat.id, 'Стартап или стартап - это компания или проект, осуществляемый предпринимателем для поиска, разработки и проверки масштабируемой бизнес-модели. В то время как предпринимательство относится ко всем новым предприятиям, включая самозанятость и предприятия, которые никогда не собираются регистрироваться, стартапы относятся к новым предприятиям, которые намерены выйти за рамки сольного основателя. В начале стартапы сталкиваются с высокой неопределенностью и имеют высокий процент неудач, но меньшинство из них продолжают быть успешными и влиятельными. Некоторые стартапы становятся единорогами; это частные стартап-компании стоимостью более 1 миллиарда долларов США.', reply_markup=markup)
        elif message.text == 'Читать больше про финансовые отчеты':
            # Keybord
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item1 = types.KeyboardButton('Читать  ещё больше про финансовые отчеты')
            markup.add(item1)
            bot.send_message(message.chat.id, 'Финансовые отчеты состоят из десятков таблиц с результатами. Как правило, выделяют несколько базовых пунктов: капитал, выручка, чистая прибыль, EBITDA, прибыль на акцию, маржа операционной прибыли, рентабельность продаж, свободный денежный поток, долговые обязательства.', reply_markup=markup)
        elif message.text == 'Читать больше про коронавирусы':
            # Keybord
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item1 = types.KeyboardButton('Читать  ещё больше про короновирусы')
            markup.add(item1)
            bot.send_message(message.chat.id, 'Coronaviridae - это семейство оболочечных РНК-вирусов с положительной цепью, которые заражают амфибий, птиц и млекопитающих. В группу входят подсемейства Lentivirinae и Orthocoronavirinae; представители последних известны как коронавирусы. '
'Вирусный геном имеет длину 26-32 килобазы. Частицы, как правило, украшены крупными (~20 нм) выступами на поверхности в форме клубов или лепестков ("пепломеры" или "шипы"), которые на электронных микрофотографиях сферических частиц создают изображение, напоминающее солнечную корону.', reply_markup=markup)



        # Third layer
        elif message.text == 'Читать  ещё больше про молекулы':
            # Keybord
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item1 = types.KeyboardButton('Найти идею!🦉')
            item2 = types.KeyboardButton('О боте🤖')
            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Полезные ссылки: https://zen.yandex.ru/media/id/5a630d2c9b403c5442578563/pogovorim-o-molekulah-kak-obrazuiutsia-molekuly-5b0cfaee3c50f79e15532009', reply_markup=markup)
        elif message.text == 'Читать  ещё больше про ДНК':
            # Keybord
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item1 = types.KeyboardButton('Найти идею!🦉')
            item2 = types.KeyboardButton('О боте🤖')
            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Полезные ссылки: https://habr.com/ru/post/427153/', reply_markup=markup)
        elif message.text == 'Читать  ещё больше про атом':
            # Keybord
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item1 = types.KeyboardButton('Найти идею!🦉')
            item2 = types.KeyboardButton('О боте🤖')
            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Полезные ссылки: https://extremal.mirtesen.ru/blog/43570827621/Kak-vyiglyadit-samaya-malenkaya-chastitsa-vo-Vselennoy', reply_markup=markup)
        elif message.text == 'Читать  ещё больше про скорость света':
            # Keybord
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item1 = types.KeyboardButton('Найти идею!🦉')
            item2 = types.KeyboardButton('О боте🤖')
            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Полезные ссылки: https://masterok.livejournal.com/6776517.html', reply_markup=markup)
        elif message.text == 'Читать  ещё больше про кредиты':
            # Keybord
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item1 = types.KeyboardButton('Найти идею!🦉')
            item2 = types.KeyboardButton('О боте🤖')
            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Полезные ссылки: https://zen.yandex.ru/media/bankrotof_net/istoriia-kreditovaniia-gde-kogda-i-kak-poiavilis-pervye-kreditnye-zaimy-v-mire-5b62b5bbe9151400a9f49a2c', reply_markup=markup)
        elif message.text == 'Читать  ещё больше про банки':
            # Keybord
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item1 = types.KeyboardButton('Найти идею!🦉')
            item2 = types.KeyboardButton('О боте🤖')
            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Полезные ссылки: https://www.rankred.com/how-much-money-is-there-in-the-world/', reply_markup=markup)
        elif message.text == 'Читать  ещё больше про стартапы':
            # Keybord
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item1 = types.KeyboardButton('Найти идею!🦉')
            item2 = types.KeyboardButton('О боте🤖')
            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Полезные ссылки: https://vc.ru/finance/123807-biznes-modeli-dlya-startapa-obzor', reply_markup=markup)
        elif message.text == 'Читать  ещё больше про финансовые отчеты':
            # Keybord
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item1 = types.KeyboardButton('Найти идею!🦉')
            item2 = types.KeyboardButton('О боте🤖')
            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Полезные ссылки: https://vc.ru/marketing/209381-ne-roi-edinym-kak-primenyat-v-ocenke-kommunikaciy-finansovye-metriki', reply_markup=markup)
        elif message.text == 'Читать  ещё больше про короновирусы':
            # Keybord
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item1 = types.KeyboardButton('Найти идею!🦉')
            item2 = types.KeyboardButton('О боте🤖')
            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Полезные ссылки: https://biomolecula.ru/articles/otkuda-poiavilis-chelovecheskie-koronavirusy', reply_markup=markup)

        else:
            bot.send_message(message.chat.id, 'Я не знаю, что ответить. Выбери другую команду.')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            # Biology path
            if call.data == 'bio':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton('Как образуются молекулы?', callback_data='mol')
                item2 = types.InlineKeyboardButton('Как ДНК хранит информацию?', callback_data='dna')
                markup.add(item1, item2)

                bot.send_message(call.message.chat.id, 'Выбери интересную идею', reply_markup=markup)
            # Physics path
            elif call.data == 'phys':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton('Что бывает меньше атома?', callback_data='atom')
                item2 = types.InlineKeyboardButton('Возможно ли преодолеть скорость света?', callback_data='photon')
                markup.add(item1, item2)

                bot.send_message(call.message.chat.id, 'Выбери интересную идею', reply_markup=markup)
            # Bank path
            elif call.data == 'bank':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton('Кто придумал кредит?', callback_data='kred')
                item2 = types.InlineKeyboardButton('Сколько денег у банков?', callback_data='deng')
                markup.add(item1, item2)

                bot.send_message(call.message.chat.id, 'Выбери интересную идею', reply_markup=markup)
            # Business path
            elif call.data == 'busin':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton('Что такое стартап?', callback_data='start')
                item2 = types.InlineKeyboardButton('Что такое квартальный отчет?', callback_data='quart')
                markup.add(item1, item2)

                bot.send_message(call.message.chat.id, 'Выбери интересную идею', reply_markup=markup)
            # Medical path
            elif call.data == 'medic':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton('Кто такой COVID-19?', callback_data='cov')
                markup.add(item1)

                bot.send_message(call.message.chat.id, 'Выбери интересную идею', reply_markup=markup)



            # Items in biology path
            elif call.data == 'mol':
                # Keybord
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                item1 = types.KeyboardButton('Читать больше про молекулы')
                markup.add(item1)
                bot.send_message(call.message.chat.id, 'Молекулы - это мелкие частицы, образованные из атомов, которые связаны прочными ковалентными связями. '
                                                       'Атомы связываются в молекулы, когда их электроны начинают образовывать связи между собой.', reply_markup=markup)
            elif call.data == 'dna':
                # Keybord
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                item1 = types.KeyboardButton('Читать больше про ДНК')
                markup.add(item1)
                bot.send_message(call.message.chat.id, 'ДНК - это макромолекула, обеспечивающая хранение, передачу и реализацию генетической информации.', reply_markup=markup)



            # Items in physics path
            elif call.data == 'atom':
                # Keybord
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                item1 = types.KeyboardButton('Читать больше про атомы')
                markup.add(item1)
                bot.send_message(call.message.chat.id, 'Атом - это мельчайшая частица, которую нельзя разделить химическим путем. '
                                                       'Если прибегнуть к физическим квантовым способам, то можно получить такие частица, как кварки.', reply_markup=markup)
            elif call.data == 'photon':
                # Keybord
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                item1 = types.KeyboardButton('Читать больше про скорость света')
                markup.add(item1)
                bot.send_message(call.message.chat.id, 'Скорость света - это скорость распространения электро-магнитных волн. '
                                                       'Скорость света в вакууме считают наибольшей скоростью во всей вселенной. '
                                                       'Однако, есть 2 пути обогнать свет: замедлить его или двигаться действительно быстрее света.', reply_markup=markup)



            # Items in bank path
            elif call.data == 'kred':
                # Keybord
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                item1 = types.KeyboardButton('Читать больше про кредиты')
                markup.add(item1)
                bot.send_message(call.message.chat.id, 'Впервые термин «кредит» появилось еще в древности, однако по значению он немного отличался от современного кредита. Уже в за 3000 лет до нашей эры этот тип отношений существовал в развитых странах того времени: Вавилоне, Ассирии, Египте. Те, кто брал в долг, но не возвращал его вовремя, становились рабами кредитора.', reply_markup=markup)
            elif call.data == 'deng':
                # Keybord
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                item1 = types.KeyboardButton('Читать больше про банки')
                markup.add(item1)
                bot.send_message(call.message.chat.id, 'Через банк проходят в принципе все деньги. Всего в мире насчитывается: от 4,5 до 75 триллионов в долларовом эквиваленте. Однако банку невыгодно хранить наличку у себя, поэтому точного чилсла, сколько денег содержится у банка, нет.', reply_markup=markup)



            # Items in business path
            elif call.data == 'start':
                # Keybord
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                item1 = types.KeyboardButton('Читать больше про стартапы')
                markup.add(item1)
                bot.send_message(call.message.chat.id, 'Единого мнения на этот вопрос не существует, однако кое-какие факторы можно выделить. '
                                                       'Стартап - это бизнес обладающий новой идеей, структурой и простотой масштабирования.', reply_markup=markup)
            elif call.data == 'quart':
                # Keybord
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                item1 = types.KeyboardButton('Читать больше про финансовые отчеты')
                markup.add(item1)
                bot.send_message(call.message.chat.id, 'Квартальная отчетность - это публикация каких-либо результатов за прошедший квартал. Различают бухгалтерскую, финансовую и многие другие отчетности.', reply_markup=markup)



            # Items in medical path
            elif call.data == 'cov':
                # Keybord
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                item1 = types.KeyboardButton('Читать больше про коронавирусы')
                markup.add(item1)
                bot.send_message(call.message.chat.id, 'COVID-19 - это лишь один из видов (штаммов) коронавирусов. Их насчитывается около 43 видов и все они обладают своими особенностями.', reply_markup=markup)


            else:
                bot.send_message(message.chat.id, 'Я не знаю, что ответить. Выбери другую команду.')

    except Exception as e:
        print(repr(e))

# Run bot
bot.polling(none_stop=True)