import command_system


def rasp(user_id, content):
    filepath = "images/"
    message = "Получай!"
    file = f"{filepath}1.jpeg"
    return message, "", file


rasp_command = command_system.Command()

rasp_command.keys = ['8к2491', '8к2492', '8к2493', '7к2491', '7к2492',
                     '7к2493', '8к2411', 'страница 2'
                     ]
rasp_command.description = "Расписание 2 страницы"
rasp_command.file = True
rasp_command.process = rasp
