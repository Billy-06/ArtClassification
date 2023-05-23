# Define the parent folder as a package and as the root of the application
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PARENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPLICATION_DIR = os.path.join(PARENT_DIR, 'application')
DATA_DIR = os.path.join(APPLICATION_DIR, 'data')
WEIGHTS_DIR = os.path.join(APPLICATION_DIR, 'weights')
MODELS_DIR = os.path.join(APPLICATION_DIR, 'models')

# print(PARENT_DIR)
# print(APPLICATION_DIR)
# print(DATA_DIR)
# print(WEIGHTS_DIR)
# print(MODELS_DIR)
