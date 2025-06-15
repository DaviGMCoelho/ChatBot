from src.Utils.ServiceUtils import ServiceUtils

class MessageValidation:
    @staticmethod
    def message_content(message):
        if message:
            status = True
            warning = ServiceUtils.generate_status_message(status, message)
            return warning
        else:
            status = False
            warning = ServiceUtils.generate_status_message(status, message)
            return warning