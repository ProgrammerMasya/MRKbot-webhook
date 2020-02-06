import command_system


def rasp(user_id, content):
    filepath = "images/"
    message = "Получай!"
    file = f"{filepath}3.jpeg"
    return message, "", file


rasp_command = command_system.Command()

rasp_command.keys = ['8к1111', '7к1191', '7к1591', '7к1391', '7к1111', '61191', '61591', '61391', 'страница 4']
rasp_command.description = "Расписание 4 страницы"
rasp_command.file = True
rasp_command.process = rasp
