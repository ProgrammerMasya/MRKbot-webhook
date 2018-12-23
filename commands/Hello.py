import command_system


def info(user_id, content):
    message = "Привет, я МРК бот, напиши мне номер группы или страницы и я пришлю тебе расписание!"
    return message, ""


info_command = command_system.Command()

info_command.keys = ["привет", "hello"]
info_command.description = "Поздороваюсь с тобой и расскажу о себе!"
info_command.process = info
