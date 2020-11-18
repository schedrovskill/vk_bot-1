import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
key = "c6bfd599e93b11b43f2a46aa9bdb17ed8502b191f5d4ef733fe389e597608ca4937a3cfe0ebdd47625474"
# Авторизуемся как сообщество
vk = vk_api.VkApi(token=key)

def send_message(user_id, message):
                from random import randint
                vk.method('messages.send',
                          {'user_id': user_id,
                           "random_id":randint(1,1000) ,
                           'message': message,}
                          )

# Работа с сообщениями
longpoll = VkLongPoll(vk)
# Основной цикл
for event in longpoll.listen():
    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
            text = event.text.lower()
            user_id = event.user_id
            if "привет" in text:
              send_message(user_id, "привет")
              print(text)
            
