import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.Model.Entities.CurrentUser import CurrentUser
current_user = CurrentUser()

print('current_user ----->', current_user)