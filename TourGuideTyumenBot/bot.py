import telebot

from telebot import types

from dotenv import load_dotenv
import os

load_dotenv()

bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))

user_roles = {}

current_location = {}

tour_data = {
    "Школьники": {
        "Набережная реки Туры": {
            "description": "Друзья мои, представьте себе… Тюмень стоит на берегу великой реки Туры! Четыре уровня набережной, мраморные лестницы и величественные памятники… Настоящая жемчужина города!",
            "photo": "photos/1.jpg",
            "question": "Какие памятники можно встретить на набережной?",
            "answer": "Это загадка! Но я подскажу: тут есть и великие купцы, и образы прошлого!"
        },
        "Мост Влюбленных": {
            "description": "Ну что, ребята, готовы к романтике? Этот мост носит символичное название! Но так было не всегда…",
            "photo": "photos/2.jpg",
            "question": "Почему мост назвали 'Мостом Влюбленных'?",
            "answer": "Ах, 2003 год… Конкурс на самый долгий поцелуй! Вы можете представить, сколько влюбленных сердец нашли здесь свой символ верности?"
        },
        "Знаменский кафедральный собор": {
            "description": "А вот и сердце духовной Тюмени! Представьте себе… XVIII век, возведение величественного собора! Вдохните воздух истории!",
            "photo": "photos/3.jpg",
            "question": "А в каком году был построен этот собор?",
            "answer": "Знаменский кафедральный собор в Тюмени строили в период с 1768 по 1801 год."
        },
        "Дом Машарова": {
            "description": "О, друзья мои! А вот и дом Машарова. Не просто здание, а настоящая история, спрятанная в стенах этого особняка!",
            "photo": "photos/4.jpg",
            "question": "Что произошло с особняком в 1919 году?",
            "answer": "В бурном 1919 году дом был национализирован и долгие годы служил детской консультацией."
        },
        "Тюменский драматический театр": {
            "description": "Дети, представьте, как поднимается занавес, звучит музыка… Перед нами один из крупнейших театров России!",
            "photo": "photos/5.jpg",
            "question": "Когда был поставлен первый спектакль в Тюмени?",
            "answer": "В далеком XIX веке!"
        },
        "Сквер Сибирских кошек": {
            "description": "Мяу! А вот и наши герои! Вы знали, что эти кошки спасли Ленинград во время блокады?",
            "photo": "photos/6.jpg",
            "question": "Почему сквер посвящен кошкам?",
            "answer": "Они сражались с нашествием крыс и помогли сохранить запасы продовольствия!"
        },
        "Цветной бульвар": {
            "description": "Аттракционы, фонтаны, музыка… Чувствуете, как оживает бульвар?",
            "photo": "photos/7.jpg",
            "question": "Почему Цветной бульвар получил такое название?",
            "answer": "Яркие краски, фонтаны, цветы — вся палитра жизни здесь!"
        },
        "Тюменский цирк": {
            "description": "Друзья, цирк — это волшебство!",
            "photo": "photos/8.jpg",
            "question": "В каком году был построен цирк?",
            "answer": "В 1971 году."
        },
        "Музей имени Словцова": {
            "description": "Здесь хранятся настоящие сокровища прошлого! Но знаете ли вы, какие именно?",
            "photo": "photos/9.jpg",
            "questions": [
                {"q": "Какие археологические находки можно увидеть в музее?", "answer": "Древние орудия труда, бронзовые украшения, предметы быта коренных народов Сибири."},
                {"q": "Есть ли в музее редкие экспонаты?", "answer": "Да! Здесь хранятся старинные иконы XVI-XVIII веков, а также уникальные рукописные книги."}
            ]
        },
        "Памятник первопроходцам Сибири": {
            "description": "Друзья, перед вами монумент в честь тех, кто первыми отправился покорять бескрайние просторы Сибири!",
            "photo": "photos/10.jpg",
            "question": "Кто такие первопроходцы, и чем они занимались?",
            "answer": "Это были казаки, купцы, исследователи и путешественники, прокладывавшие новые торговые пути и осваивавшие неизведанные земли."
        }
    },
    "Студенты": {
        "Набережная реки Туры": {
            "description": "Коллеги, перед нами набережная реки Туры — не просто прогулочная зона, а место, где история встречается с современностью.",
            "photo": "photos/1.jpg",
            "question": "Какую роль река Тура играла в истории Тюмени?",
            "answer": "В 17-18 веках она была важнейшей торговой артерией, соединявшей Сибирь с Россией."
        },
        "Мост Влюбленных": {
            "description": "А теперь, друзья, взгляните на этот элегантный мост. Его изящные линии словно созданы для встреч, признаний и романтических прогулок.",
            "photo": "photos/2.jpg",
            "question": "Какое название мост носил до переименования?",
            "answer": "Исторически он именовался Комсомольским. Но, как вы знаете, названия меняются, а любовь — вечна."
        },
        "Знаменский кафедральный собор": {
            "description": "Посмотрите направо, и перед нами — Знаменский кафедральный собор. Это не просто храм, это свидетель эпох, переживший десятки поколений.",
            "photo": "photos/3.jpg",
            "question": "Какую роль собор сыграл в истории Тюмени?",
            "answer": "На протяжении веков он был духовным центром города, местом молитв и укрытием для верующих."
        },
        "Дом Машарова": {
            "description": "Купеческий особняк, выдержавший испытание временем… Машаров был не просто купцом, а пионером промышленности в Тюмени.",
            "photo": "photos/4.jpg",
            "question": "Какую роль особняк играл в развитии промышленности?",
            "answer": "Здесь решались судьбы местной торговли и производства."
        },
        "Тюменский драматический театр": {
            "description": "Театр — отражение эпохи, голос народа… Этот зал видел блестящие постановки и великих артистов.",
            "photo": "photos/5.jpg",
            "question": "Какие известные постановки проходили в этом театре?",
            "answer": "Здесь ставили классику и новаторские спектакли, открывая миру таланты."
        },
        "Сквер Сибирских кошек": {
            "description": "История хранит имена не только людей, но и животных… Сибирские кошки стали символом выносливости и верности.",
            "photo": "photos/6.jpg",
            "question": "Что символизируют Сибирские кошки?",
            "answer": "Символ героизма, стойкости и спасения."
        },
        "Цветной бульвар": {
            "description": "Сердце города, где сочетаются история и современность это и есть Цветной Бульвар.",
            "photo": "photos/7.jpg",
            "question": "Какие культурные мероприятия проходят на бульваре?",
            "answer": "Концерты, фестивали, выставки… Вечно живущая сцена."
        },
        "Тюменский цирк": {
            "description": "Форма купола, светящийся шар… Архитектурный символ целой эпохи.",
            "photo": "photos/8.jpg",
            "question": "Какие знаменитые цирковые артисты выступали здесь?",
            "answer": "Великие мастера арены, Аскольд и Эдгард Запашные. Братья выступали в цирке в 2012 году, подарившие городу незабываемые шоу. А также Валерий Леонтьев, Юра Шатунов, Сергей Лазарев. Также в цирке выступали звёзды 90-х и проекта «Фабрика звёзд»."
        },
        "Музей имени Словцова": {
            "description": "Этот музей — ключ к пониманию истории Тюменского края. Его экспозиции охватывают разные эпохи.",
            "photo": "photos/9.jpg",
            "question": "Какие значимые экспонаты можно здесь найти?",
            "answer": "Оригинальные документы сибирских первопроходцев, картины местных художников XIX века и старинное оружие казаков."
        },
        "Памятник первопроходцам Сибири": {
            "description": "Перед нами монумент, символизирующий не только освоение Сибири, но и силу человеческого духа.",
            "photo": "photos/10.jpg",
            "question": "Какие фигуры изображены на памятнике, и что они означают?",
            "answer": "Памятник изображает казака с ружьем, крест, знаменующий распространение православия, и караван с обозами, символизирующий развитие торговли."
        }
    }
}

destinations = list(tour_data["Школьники"].keys())


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Школьники")
    btn2 = types.KeyboardButton("Студенты")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Добро пожаловать! Выберите свою категорию:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in ["Школьники", "Студенты"])
def set_role(message):
    user_roles[message.chat.id] = message.text
    bot.send_message(message.chat.id, f"Вы выбрали: {message.text}.",
                     reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add(types.KeyboardButton("В путь!")))


@bot.message_handler(func=lambda message: message.text == "В путь!")
def tour(message):
    role = user_roles.get(message.chat.id)
    if not role:
        bot.send_message(message.chat.id, "Сначала выберите категорию, используя команду /start")
        return

    current_location[message.chat.id] = 0
    send_location_info(message)


def send_location_info(message):
    role = user_roles[message.chat.id]
    locations = list(tour_data[role].keys())
    location = locations[current_location[message.chat.id]]
    data = tour_data[role][location]

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    if "question" in data:
        btn_question = types.KeyboardButton(data["question"])
        markup.add(btn_question)
    elif "questions" in data:
        for q in data["questions"]:
            btn_question = types.KeyboardButton(q["q"])
            markup.add(btn_question)

    btn_next = types.KeyboardButton('Следующая достопримечательность')
    markup.add(btn_next)

    if "photo" in data:
        try:
            with open(data["photo"], "rb") as photo:
                bot.send_photo(message.chat.id, photo)
        except FileNotFoundError:
            bot.send_message(message.chat.id, "Фото не найдено, но экскурсия продолжается!")

    bot.send_message(message.chat.id, f"{location}: {data['description']}", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Следующая достопримечательность')
def next_loc(message):
    role = user_roles[message.chat.id]

    if not role:
        bot.send_message(message.chat.id, "Сначала выберите категорию, используя команду /start")
        return

    locations = list(tour_data[role].keys())
    if current_location[message.chat.id] + 1 < len(locations):
        current_location[message.chat.id] += 1
        send_location_info(message)
    else:
        bot.send_message(message.chat.id, 'Эксурсия звершена! Спасибо за участие!')

@bot.message_handler(func=lambda message: True)
def answer_question(message):
    role = user_roles.get(message.chat.id)
    if not role:
        return

    locations = list(tour_data[role].keys())
    location = locations[current_location[message.chat.id]]
    data = tour_data[role][location]

    if "question" in data and message.text == data["question"]:
        bot.send_message(message.chat.id, data["answer"])
        return

    if "questions" in data and isinstance(data["questions"], list):
        for q in data["questions"]:
            if message.text == q["q"]:
                bot.send_message(message.chat.id, q["answer"])
                return

    bot.send_message(message.chat.id, "Интересный вопрос! Обязательно изучу его на досуге")


bot.polling(none_stop=True)
