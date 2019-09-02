import command_system


def rasp(user_id, content):
    filepath = "images/"
    message = "Получай!"
    file = f"{filepath}0.jpeg"
    return message, "", file


rasp_command = command_system.Command()

rasp_command.keys = ['9к9191', '9к9091', '9к9291', '9к9111', '8к1191', '8к1591', '8к1391', 'страница 1']
rasp_command.description = "Расписание 1 страницы"
rasp_command.file = True
rasp_command.process = rasp
