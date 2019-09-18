import command_system


def rasp(user_id, content):
    filepath = "images/"
    message = "Получай!"
    file = f"{filepath}2.jpeg"
    return message, "", file


rasp_command = command_system.Command()

rasp_command.keys = ['9к9591', '9к9491', '8к3791', '8к3291', 'страница 3']
rasp_command.description = "Расписание 3 страницы"
rasp_command.file = True
rasp_command.process = rasp
