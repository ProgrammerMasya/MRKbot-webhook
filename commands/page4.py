import command_system


def rasp(user_id, content):
    filepath = "images/"
    message = "Получай!"
    file = f"{filepath}4.jpeg"
    return message, "", file


rasp_command = command_system.Command()

rasp_command.keys = ['62491', '62492', '62493', '62411', '52491', '52492', '52493',
                     'страница 5'
                     ]
rasp_command.description = "Расписание 5 страницы"
rasp_command.file = True
rasp_command.process = rasp
