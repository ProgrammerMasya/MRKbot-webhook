import command_system


def rasp(user_id, content):
    filepath = "images/"
    message = "Получай!"
    file = f"{filepath}5.jpeg"
    return message, "", file


rasp_command = command_system.Command()

rasp_command.keys = ['7к3791', '7к3291', 'страница 6']
rasp_command.description = "Расписание 6 страницы"
rasp_command.file = True
rasp_command.process = rasp
