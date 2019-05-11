import vkapi


class Vk:
    def __init__(self, token):
        self.token = token

    def send_message(self, user_id, message, attachment, file=None):
        vkapi.send_message(user_id, self.token, message, attachment, file)
