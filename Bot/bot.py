import telegram
import random


def send_test_message():
    try:
        random_number = random.randint(0, 1000)
        telegram_notify = telegram.Bot("5597243280:AAE4olHZvMmY-VsLyTNdr271guVziD8biDI")
        # message = "`Số random là {}`".format(random_number)
        message = "Hi Groups"
        telegram_notify.send_message(chat_id="-630349231", text=message,
                                     parse_mode='Markdown')
        telegram_notify.sendPhoto(chat_id="-630349231",photo = open('dog.jpg','rb'),caption = "Nhà có chó dữ vui lòng không chọc")
    except Exception as ex:
        print(ex)


send_test_message()
