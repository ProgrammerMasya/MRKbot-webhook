import command_system


def rasp(user_id, content):
    filepath = "images/"
    message = "Получай!"
    file = f"{filepath}5.jpeg"
    return message, "", file


rasp_command = command_system.Command()

rasp_command.keys = ['63791', '63291', '53791', '53291', '53292', 'страница 6']
rasp_command.description = "Расписание 6 страницы"
rasp_command.file = True
rasp_command.process = rasp
