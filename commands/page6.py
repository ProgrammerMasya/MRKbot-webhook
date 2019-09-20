import command_system


def rasp(user_id, content):
    filepath = "images/"
    message = "Получай!"
    file = f"{filepath}6.jpeg"
    return message, "", file


rasp_command = command_system.Command()

rasp_command.keys = ['7к3791', '7к3291', '63791', '63291', 'страница 7']
rasp_command.description = "Расписание 7 страницы"
rasp_command.file = True
rasp_command.process = rasp
