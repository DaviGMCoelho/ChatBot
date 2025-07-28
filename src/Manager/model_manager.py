import ollama
from src.Constants.Messages import Messages
from src.utils.utilities import Utilities

class ModelManager:
    def get_installed_models(self):
        utils = Utilities()
        models_installed = []
        try:
            models = ollama.list()
            if 'models' in models:
                for model in models['models']:
                    model_name = model.get('model', model.get('name', 'Unknow'))
                    models_installed.append(model_name)
                return utils.generate_message(True, models_installed)
            else:
                return utils.generate_message(False, Messages.MODEL_LOAD_ERROR)
        except Exception as e:
            return utils.generate_message(False, e)
