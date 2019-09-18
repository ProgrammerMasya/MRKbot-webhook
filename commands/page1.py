import command_system


def rasp(user_id, content):
    filepath = "images/"
    message = "Получай!"
    file = f"{filepath}1.jpeg"
    return message, "", file


rasp_command = command_system.Command()

rasp_command.keys = ['9к9391', '9к9392', '9к9393', '9к9394', '9к9311', '8к2491', '8к2492', '8к2493', '8к2411', '7к2491',
                     '7к2492', '7к2493', 'страница 2']
rasp_command.description = "Расписание 2 страницы"
rasp_command.file = True
rasp_command.process = rasp
