import command_system


def info(user_id, content):
    message = ""
    for c in command_system.command_list:
        print(c)
        message += c.keys[0] + " - " + c.description + "\n"
    return message, ""


info_command = command_system.Command()

info_command.keys = ["помощь", "help"]
info_command.description = "Покажу список команд"
info_command.process = info
