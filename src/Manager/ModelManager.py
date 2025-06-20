import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import ollama
from src.Constants.Messages import Messages
from src.Utils.Utilities import Utilities

class ModelManager:
    @staticmethod
    def show_installed_models():
        models_installed = []
        try:
            models = ollama.list()
            if 'models' in models:
                for model in models['models']:
                    model_name = model.get('model', model.get('name', 'Unknow'))
                    models_installed.append(model_name)
                return Utilities.generate_status_message(True, models_installed)
            else:
                return Utilities.generate_status_message(False, Messages.MODEL_LOAD_ERROR)
        except Exception as e:
            return Utilities.generate_status_message(False, e)
        
if __name__ == '__main__':
    print(ModelManager.show_installed_models())