# import os
# from datetime import datetime
# import time


class Menu():
    # def __init__(self):
    #     if (os.name == 'posix'):
    #         os.system('clear')
    #     # else screen will be cleared for windows
    #     else:
    #         os.system('cls')
    pass


class View():
    """Get User input and preprocess """

    def get_user_input(self, msg_display, msg_error,
                       value_type, assertions=None,
                       default_value=None):
        # clear_screen()
        while True:
            value = input(msg_display)
            if value_type == "numeric":
                if value.isnumeric():
                    value = int(value)
                    return value
                else:
                    print(msg_error)
                    continue

            if value_type == "num_superior":
                if value.isnumeric():
                    value = int(value)
                    if value >= default_value:
                        return value
                    else:
                        print(msg_error)
                        continue
                else:
                    print(msg_error)
                    continue

            if value_type == "string":
                try:
                    float(value)
                    print(msg_error)
                    continue
                except ValueError:
                    return value

            elif value_type == "date":
                if self.verify_date(value):
                    return value
                else:
                    print(msg_error)
                    continue

            elif value_type == "selection":
                if value in assertions:
                    return value
                else:
                    print(msg_error)
                    continue

    @staticmethod
    def verify_date(value_tested):
        if "-" not in value_tested:
            return False
        else:
            format_date = value_tested.split("-")
            for date in format_date:
                if not date.isnumeric():
                    return False
            return True
