import nltk
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
import json
import pickle
import numpy as np
words=[]
classes = []
word_tags_list = []
ignore_words = ['?', '!',',','.', "'s", "'m"]
train_data_file = open('/content/c137_1/intents.json').read()
intents = json.loads(train_data_file)
# Función para añadir palabras raíz (stem words)





        # Agregar todas las palabras de los patrones a una lista
        



        # Agregar todas las etiquetas a la lista de clases
       





# Crear un corpus de palabras para el chatbot

