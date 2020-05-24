import command_system


def rasp(user_id, content):
    filepath = "images/"
    message = "Получай!"
    file = f"{filepath}4.jpeg"
    return message, "", file


rasp_command = command_system.Command()

rasp_command.keys = ['8к1111', '7к1191', '7к1591', '7к1391', 'страница 5']
rasp_command.description = "Расписание 5 страницы"
rasp_command.file = True
rasp_command.process = rasp
