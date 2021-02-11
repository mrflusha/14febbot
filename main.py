import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

tok_ken = '61f66d4eebf3ecc7a4544811a56b1b7e544d4dc989d8358c99091e046f62b043f60c395d8d49fb62d9a06'

vk_session = vk_api.VkApi(token = tok_ken)
longpoll = VkLongPoll(vk_session)


def sender(id, text):
	vk_session.method("messages.send" , {'chat_id': id , 'message' : text , 'random_id': 0})



for event in longpoll.listen():
	if event.type == VkEventType.MESSAGE_NEW:
		if event.to_me:
			if event.from_chat:
				msg = event.text.lower()
				if msg != 0:
					#sender(id, "Я люблю тебя Катя!!!!!!")

					id = event.chat_id

					sender(id, "Я люблю тебя Катя!!!!!!")
					print(msg)

					if msg == ('yo'):
						sender(id, "HASTLE HASTLE")
					elif msg == "Хуй" or 'хуй':
						sender(id, "Нельзя ругаться")

