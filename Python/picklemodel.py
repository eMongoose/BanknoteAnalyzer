import pickle
import os

# store model object with the model name
def store_model(model_name, model):
  file_path = os.path.join('Models', f'{model_name}.mdl')
  file = open(file_path, 'wb')
  pickle.dump(model, file)
  file.close()

def load_model(model_name):
  file_path = os.path.join('Models', f'{model_name}.mdl')
  file = open(file_path, 'rb')
  loaded_model = pickle.load(file)
  file.close()
  return loaded_model