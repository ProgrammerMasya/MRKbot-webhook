import command_system


def info(user_id, content):
    message = "https://vk.com/id141177799"
    return message, ""


info_command = command_system.Command()

info_command.keys = ["Создатель"]
info_command.description = "Пришлю ссылку Творца!"
info_command.process = info
