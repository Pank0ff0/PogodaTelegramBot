import telebot

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

bot = telebot.TeleBot("<bot API token>")
config_dict = get_default_config()
config_dict['language'] = 'ru'  
owm = OWM('<PYOWM API>', config_dict)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Это бот показывающий погоду!")


@bot.message_handler(func=lambda message: True)
def send_message(message):
    owm.supported_languages
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(message.text)
    weather = observation.weather
    t = weather.temperature("celsius")
    t1 = round(t['temp'])
    dt = weather.detailed_status
    ans = "В городе " + message.text + "\n\n"
    ans += f"Сейчас  {t1}  С°,  {dt} \n\n"
    if 50 > t1 > 20:
        if (dt == "пасмурно") or (dt == "дождь") or (dt == "легкий дождь"):
            ans += ("Воозьми зонтик и \n")  
        ans += ("Одень шортики =)")
    if 20 > t1 > 15 :
        if (dt == "пасмурно") or (dt == "дождь") or (dt == "легкий дождь"): 
            ans += ("Воозьми зонтик и \n")    
        ans += ("Пора сменить шорты и юбки на штаны =)")
    elif 15 > t1 > 5:
        if (dt == "пасмурно") or (dt == "дождь") or (dt == "легкий дождь"):
            ans += ("Воозьми зонтик и \n") 
        ans += ("Накинь что-нибудь тепленькое =)")
    elif 5 > t1 > -5:
        if (dt == "пасмурно") or (dt == "дождь") or (dt == "легкий дождь"):
            ans += ("Воозьми зонтик и \n")
        ans += ("Не забудь надеть перчатки и куртку =)")
    elif t1 < -5:
        ans += ("Незабудь надеть теплую куртку =)")
    bot.send_message(message.chat.id, ans)


bot.infinity_polling()