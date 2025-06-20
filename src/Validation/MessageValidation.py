from Utils.Utilities import Utilities

class MessageValidation:
    @staticmethod
    def message_content(message):
        if message:
            status = True
            warning = Utilities.generate_status_message(status, message)
            return warning
        else:
            status = False
            warning = Utilities.generate_status_message(status, message)
            return warning