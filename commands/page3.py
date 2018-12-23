import command_system


def rasp(user_id, content):
    filepath = "images/"
    message = "Получай!"
    file = f"{filepath}3.jpeg"
    return message, "", file


rasp_command = command_system.Command()

rasp_command.keys = ['7к1111', '61191', '61591', '61111', '51191', '51591',
                     '51592', '51391', '51392', 'страница 4'
                     ]
rasp_command.description = "Расписание 4 страницы"
rasp_command.file = True
rasp_command.process = rasp
